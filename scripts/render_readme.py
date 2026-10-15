#!/usr/bin/env python3
"""Render verified downloads from the published update feed; no network requests."""
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
def render():
 entries=json.loads((ROOT/'catalog/entries.json').read_text())
 published={e['identifier']:e for e in json.loads((ROOT/'catalog/updates.json').read_text())['extensions']}
 rows=['| 扩展 / Extension | 用途 | 版本 | 最低 Bubboo | 作者 / 许可证 | 下载 |','| --- | --- | --- | --- | --- | --- |']
 for e in sorted(entries,key=lambda e:e['name'].casefold()):
  if e['status']!='verified':continue
  feed=published[e['identifier']]
  if feed['version']!=e['version']:raise ValueError('Publish and verify the feed before advertising a new version')
  package=e['package'];name=package.removesuffix('.popclipext')
  rows.append(f"| [{e['name']}](extensions/{package}/NOTICE.md) | {DESCRIPTIONS[name]} | {e['version']} | {e['minimumBubbooVersion']} | [{e['author']}](extensions/{package}/NOTICE.md) · [MIT](extensions/{package}/LICENSE.txt) | [下载 / Download]({feed['downloadURL']}) |")
 p=ROOT/'README.md';s=p.read_text();body='\n'.join(rows)
 if START not in s:s=s.replace('## Validate and build',START+'\n'+END+'\n\n## Validate and build')
 left,rest=s.split(START,1);_,right=rest.split(END,1);p.write_text(left+START+'\n'+body+'\n'+END+right)
if __name__=='__main__':render()
