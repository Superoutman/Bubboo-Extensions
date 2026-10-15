#!/usr/bin/env python3
"""Render verified downloads from the published update feed; no network requests."""
import argparse
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
START, END = '<!-- extension-table:start -->', '<!-- extension-table:end -->'
DESCRIPTIONS = {
 'Baidu':'百度搜索', 'Bing':'Bing 搜索', 'DuckDuckGo':'隐私搜索', 'GoogleSearch':'Google 搜索，可选地区站点',
 'GoogleTranslate':'网页翻译，可选地区站点', 'GoogleMaps':'地图搜索', 'GoogleScholar':'学术搜索', 'YouTube':'视频搜索',
 'Wikipedia':'维基百科，可选语言站点', 'Uppercase':'转大写', 'Lowercase':'转小写', 'URLEncode':'URL 编码 / 解码', 'CharCount':'字符计数',
 'TitleCase':'英文单行标题大小写（适配版）', 'Base64':'UTF-8 编解码，标准 / URL-safe（适配版）'
}
def render(app_repo=None):
 entries=json.loads((ROOT/'catalog/entries.json').read_text())
 published={e['identifier']:e for e in json.loads((ROOT/'catalog/updates.json').read_text())['extensions']}
 rows=['| 扩展 / Extension | 用途 | 版本 | 最低 Bubboo | 作者 / 许可证 | 下载 |','| --- | --- | --- | --- | --- | --- |']
 for e in sorted(entries,key=lambda e:e['name'].casefold()):
  if e['status']!='verified':continue
  feed=published[e['identifier']]
  if feed['version']!=e['version']:raise ValueError('Publish and verify the feed before advertising a new version')
  package=e['package'];name=package.removesuffix('.popclipext')
  rows.append(f"| [{e['name']}](extensions/{package}/NOTICE.md) | {e.get('summary') or DESCRIPTIONS[name]} | {e['version']} | {e['minimumBubbooVersion']} | [{e['author']}](extensions/{package}/NOTICE.md) · [MIT](extensions/{package}/LICENSE.txt) | [下载 / Download]({feed['downloadURL']}) |")
 p=ROOT/'README.md';s=p.read_text();body='\n'.join(rows)
 if START not in s:s=s.replace('## Validate and build',START+'\n'+END+'\n\n## Validate and build')
 left,rest=s.split(START,1);_,right=rest.split(END,1);p.write_text(left+START+'\n'+body+'\n'+END+right)
 if app_repo is not None:
  # Read and validate both destinations before writing either file.
  documents=[]
  absolute_body=body.replace('(extensions/', '(https://github.com/Superoutman/Bubboo-Extensions/blob/main/extensions/')
  count=sum(e['status']=='verified' for e in entries)
  intro=(f'**{count} verified extensions / 已验收扩展。** Download a package and import it in Bubboo Settings, then enable it explicitly. 下载后在设置中导入并启用。\n\n'
         'Package versions are independent of App versions. 原作者、许可证和适配说明见各扩展名称链接。'
         'Amazon code: MIT; icon: Dave Gandy, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). '
         '[Acceptance and limitations / 验收范围与限制](https://github.com/Superoutman/Bubboo-Extensions#current-stable-collection).\n\n')
  for filename in ('README.md','README.zh-CN.md'):
   path=app_repo/filename
   content=path.read_text()
   if content.count(START)!=1 or content.count(END)!=1 or '<a id="extensions"></a>' not in content:
    raise ValueError(f'{path}: expected one table block and fixed extensions anchor')
   before,rest=content.split(START,1);_,after=rest.split(END,1)
   documents.append((path,before+START+'\n'+intro+absolute_body+'\n'+END+after))
  for path,content in documents:path.write_text(content)
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--app-repo',type=Path,help='Also sync both public App READMEs from the same published catalog')
 render(parser.parse_args().app_repo)
