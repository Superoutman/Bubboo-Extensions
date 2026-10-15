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
EN_DESCRIPTIONS = {
 'Baidu':'Baidu search', 'Bing':'Bing search', 'DuckDuckGo':'Private web search',
 'GoogleSearch':'Google search with regional sites', 'GoogleTranslate':'Web translation with regional sites',
 'GoogleMaps':'Map search', 'GoogleScholar':'Scholarly search', 'YouTube':'Video search',
 'Wikipedia':'Wikipedia search with language options', 'Uppercase':'Convert to uppercase',
 'Lowercase':'Convert to lowercase', 'URLEncode':'URL encoding / decoding', 'CharCount':'Character count',
 'TitleCase':'Single-line English title case (adapted)', 'Base64':'UTF-8 encoding / decoding, standard / URL-safe (adapted)',
 'Capitalize':'Capitalize words', 'SentenceCase':'Sentence case', 'JoinLines':'Join lines',
 'RemoveSpaces':'Remove whitespace', 'Reverse':'Reverse line order', 'Sort':'Natural line sorting',
 'CommaList':'Convert between comma-separated lists and lines', 'FullHalfWidth':'Full-width / half-width conversion',
 'GoogleImages':'Google Images search', 'PubMed':'PubMed search', 'IMDb':'IMDb search',
 'Amazon':'Amazon search', 'Ebay':'eBay search', 'Goodreads':'Goodreads search',
 'StartPage':'StartPage search', 'UrbanDictionary':'Urban Dictionary lookup'
}
def render(app_repo=None):
 entries=json.loads((ROOT/'catalog/entries.json').read_text())
 published={e['identifier']:e for e in json.loads((ROOT/'catalog/updates.json').read_text())['extensions']}
 headers={
  'mixed':'| 扩展 / Extension | 用途 | 版本 | 最低 Bubboo | 作者 / 许可证 | 下载 |',
  'en':'| Extension | Purpose | Version | Minimum Bubboo | Author / License | Download |',
  'zh':'| 扩展 | 用途 | 版本 | 最低 Bubboo 版本 | 作者 / 许可证 | 下载 |'
 }
 rows={language:[header,'| --- | --- | --- | --- | --- | --- |'] for language,header in headers.items()}
 labels={'mixed':'下载 / Download','en':'Download','zh':'下载'}
 for e in sorted(entries,key=lambda e:e['name'].casefold()):
  if e['status']!='verified':continue
  feed=published[e['identifier']]
  if feed['version']!=e['version']:raise ValueError('Publish and verify the feed before advertising a new version')
  package=e['package'];name=package.removesuffix('.popclipext')
  for language in rows:
   description=EN_DESCRIPTIONS[name] if language=='en' else (e.get('summary') or DESCRIPTIONS[name])
   rows[language].append(f"| [{e['name']}](extensions/{package}/NOTICE.md) | {description} | {e['version']} | {e['minimumBubbooVersion']} | [{e['author']}](extensions/{package}/NOTICE.md) · [MIT](extensions/{package}/LICENSE.txt) | [{labels[language]}]({feed['downloadURL']}) |")
 p=ROOT/'README.md';s=p.read_text();body='\n'.join(rows['mixed'])
 if START not in s:s=s.replace('## Validate and build',START+'\n'+END+'\n\n## Validate and build')
 left,rest=s.split(START,1);_,right=rest.split(END,1);p.write_text(left+START+'\n'+body+'\n'+END+right)
 if app_repo is not None:
  # Read and validate both destinations before writing either file.
  documents=[]
  app_tables={language:'\n'.join(rows[language]).replace('(extensions/', '(https://github.com/Superoutman/Bubboo-Extensions/blob/main/extensions/') for language in ('en','zh')}
  count=sum(e['status']=='verified' for e in entries)
  intros={
   'README.md': f"""Bubboo extensions give you more ways to work with selected text: search different services, translate, reformat text, or connect a task to a tool you already use. Choose the actions that suit your workflow and keep your toolbar focused on what you need.

This collection makes extensions easier to discover, compare and install. It brings downloads, minimum App versions, original authors and adaptation notes into one place, reducing the effort of finding packages and checking whether they work. The aim is to offer more useful choices while preserving the original creators' work and making sources and changes easy to inspect.

**{count} tested extensions are available below.** Packages are included after compatibility review and real-use testing in Bubboo; this is a curated starting point, not a complete catalog of PopClip extensions. Some packages need adaptations. Open an extension's name to review its source, changes and tested limitations before installing.

**Install and update:** Download a `.popclipextz` package below, import it in Settings and enable it. Configure available options there. Bubboo 0.1.4 checks for extension updates when Settings opens, with a six-hour cache. Upgrade manually; your settings are retained and changed content requires renewed approval. Extension versions are independent of App versions; check the minimum App version in the table.

**Compatibility:** Testing does not cover every OS, regional site or third-party service. Required apps must be installed, and websites may require sign-in or restrict availability. Web searches send selected text to the destination site; scripts can perform local operations. Enable extensions you trust. See the [extension guide](https://github.com/Superoutman/Bubboo-Extensions#current-stable-collection) for details.

""",
   'README.zh-CN.md': f"""扩展让 Bubboo 不止于内置动作：你可以为选中的文字选择不同的搜索服务、进行翻译和文本处理，或连接自己常用的工具。按工作习惯选择所需动作，就能组合出更适合自己的划词工具栏。

整理这份列表，是为了让扩展更容易被发现、比较和安装。下载入口、最低 App 版本、原作者及适配说明集中在同一处，减少四处寻找下载包、判断兼容性和反复试装的成本。项目希望在尊重原作者工作的基础上，为用户提供更多实用选择，也让每个扩展的来源与改动清晰可查。

**下表提供 {count} 个已验收扩展。** 收录前会检查兼容性并在 Bubboo 中实际测试；它是一份便于上手的精选目录，并非 PopClip 扩展的完整集合。部分扩展需要适配，点击名称即可了解来源、改动及已验证的使用范围，再决定是否安装。

**安装与更新：** 下载下表中的 `.popclipextz` 文件，在设置中导入并启用；有选项的扩展也在设置中配置。Bubboo 0.1.4 打开设置时检查扩展更新，结果缓存 6 小时。手动升级会保留配置，内容变化后需重新启用授权。扩展版本与 App 版本独立，升级前请检查表格中的最低 App 版本。

**兼容性与权限：** 验收不代表所有系统、地区站点和第三方服务均可用。依赖其他 App 的扩展需先安装对应应用，网站可能要求登录或受地区限制。网页搜索会将选中文字发送给对应网站，脚本可能执行本地操作，请仅启用可信扩展。详情见[扩展使用说明](https://github.com/Superoutman/Bubboo-Extensions#current-stable-collection)。

"""
  }
  copyright_sections={
   'README.md': """## Copyright and attribution

Extension copyright remains with the original authors and respective rights holders. Bubboo's inclusion, compatibility adaptations and distribution do not transfer ownership or imply endorsement or participation by the original authors or PopClip. Bubboo and PopClip are independent projects.

Each package retains original author attribution, applicable licenses and source records; adaptations are documented in `NOTICE.md`. Code, icons and other resources may have different licenses. Review the package files before reuse or redistribution. MIT in the download table refers to extension code; for example, the Amazon icon by Dave Gandy is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

If you find an attribution, licensing or inclusion error, please report it through [Issues](https://github.com/Superoutman/Bubboo-Extensions/issues), including the extension name, relevant source information and a description of the concern so it can be reviewed.
""",
   'README.zh-CN.md': """## 版权与来源

扩展版权归原作者及相应权利人所有。Bubboo 对扩展的收录、兼容适配和分发，不代表拥有原作版权，也不表示原作者或 PopClip 官方认可或参与本项目。Bubboo 与 PopClip 是独立项目。

每个包保留原作者署名、适用许可证和来源记录；适配改动在 `NOTICE.md` 中说明。代码、图标等资源可能适用不同许可，使用或再分发时请查看包内文件。下载表格中的 MIT 指扩展代码；例如 Amazon 图标由 Dave Gandy 创作，适用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。

如发现署名、许可或收录有误，请通过[问题反馈](https://github.com/Superoutman/Bubboo-Extensions/issues)提供扩展名称、相关来源和问题说明，以便核查处理。
"""
  }
  for filename in ('README.md','README.zh-CN.md'):
   path=app_repo/filename
   content=path.read_text()
   if content.count(START)!=1 or content.count(END)!=1 or '<a id="extensions"></a>' not in content:
    raise ValueError(f'{path}: expected one table block and fixed extensions anchor')
   before,rest=content.split(START,1);_,after=rest.split(END,1)
   documents.append((path,before+START+'\n'+intros[filename]+app_tables['en' if filename=='README.md' else 'zh']+'\n\n'+copyright_sections[filename].rstrip()+'\n\n'+END+after))
  for path,content in documents:path.write_text(content)
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--app-repo',type=Path,help='Also sync both public App READMEs from the same published catalog')
 render(parser.parse_args().app_repo)
