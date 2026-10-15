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
  intros={
   'README.md': f"""**{count} tested extensions.** Not every PopClip extension works in Bubboo. This list brings tested downloads, minimum App versions and author information together, so you can choose compatible tools without repeated trial installs. Adaptations and limitations are documented through each extension's name link.

**Install and update:** Download a `.popclipextz` package below, import it in Settings and enable it. Configure available options there. Bubboo 0.1.4 checks for extension updates when Settings opens, with a six-hour cache. Upgrade manually; your settings are retained and changed content requires renewed approval. Extension versions are independent of App versions; check the minimum App version in the table.

**Compatibility:** Testing does not cover every OS, regional site or third-party service. Required apps must be installed, and websites may require sign-in or restrict availability. Web searches send selected text to the destination site; scripts can perform local operations. Enable extensions you trust. See the [extension guide](https://github.com/Superoutman/Bubboo-Extensions#current-stable-collection) for details.

""",
   'README.zh-CN.md': f"""**{count} 个已验收扩展。** 并非所有 PopClip 扩展都能直接用于 Bubboo。这份列表集中提供经过验收的下载包、最低 App 版本和作者信息，减少自行寻找、判断兼容性和反复试装的麻烦。点击扩展名称可查看适配说明及使用限制。

**安装与更新：** 下载下表中的 `.popclipextz` 文件，在设置中导入并启用；有选项的扩展也在设置中配置。Bubboo 0.1.4 打开设置时检查扩展更新，结果缓存 6 小时。手动升级会保留配置，内容变化后需重新启用授权。扩展版本与 App 版本独立，升级前请检查表格中的最低 App 版本。

**兼容性与权限：** 验收不代表所有系统、地区站点和第三方服务均可用。依赖其他 App 的扩展需先安装对应应用，网站可能要求登录或受地区限制。网页搜索会将选中文字发送给对应网站，脚本可能执行本地操作，请仅启用可信扩展。详情见[扩展使用说明](https://github.com/Superoutman/Bubboo-Extensions#current-stable-collection)。

"""
  }
  copyright_notes={
   'README.md': """

**Copyright and attribution:** Extension copyright remains with the original authors and respective rights holders. Inclusion and adaptation do not transfer ownership or imply endorsement by the authors or PopClip. Packages retain attribution, applicable licenses, provenance and change notes. MIT in the table refers to code; artwork may have separate terms—for example, Amazon's icon by Dave Gandy uses [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Review package files before reuse or redistribution. Report [attribution or licensing concerns](https://github.com/Superoutman/Bubboo-Extensions/issues) with the extension name and relevant source information.
""",
   'README.zh-CN.md': """

**版权与来源：** 扩展版权归原作者及相应权利人所有。Bubboo 的收录、适配和分发不代表拥有原作版权，也不表示原作者或 PopClip 官方认可本项目。每个包保留署名、适用许可证、来源及改动说明。表格中的 MIT 指代码，图标可能适用其他许可，例如 Amazon 图标由 Dave Gandy 创作，适用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。再使用或分发前请查看包内文件；署名或许可有误可通过[扩展仓库 Issues](https://github.com/Superoutman/Bubboo-Extensions/issues)提供扩展名称和相关来源，以便核查。
"""
  }
  for filename in ('README.md','README.zh-CN.md'):
   path=app_repo/filename
   content=path.read_text()
   if content.count(START)!=1 or content.count(END)!=1 or '<a id="extensions"></a>' not in content:
    raise ValueError(f'{path}: expected one table block and fixed extensions anchor')
   before,rest=content.split(START,1);_,after=rest.split(END,1)
   documents.append((path,before+START+'\n'+intros[filename]+absolute_body+copyright_notes[filename]+'\n'+END+after))
  for path,content in documents:path.write_text(content)
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--app-repo',type=Path,help='Also sync both public App READMEs from the same published catalog')
 render(parser.parse_args().app_repo)
