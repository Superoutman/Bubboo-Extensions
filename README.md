# Bubboo Extensions

A curated collection of original-format PopClip extensions for Bubboo. Authors, licenses and upstream provenance stay with each package. OpenClip support is a future runtime milestone; no new extension format is introduced here.

## Current stable collection

**31 verified extensions.** The original 13 require Bubboo 0.1.2 or later; the 18 additions require 0.1.4. [First-batch acceptance](acceptance/bubboo-0.1.2/README.md) · [Second-batch acceptance and limits](acceptance/bubboo-0.1.4-batch2/README.md). [Third-batch acceptance: 16 passed, 9 blocked](acceptance/bubboo-0.1.4-batch3/README.md). Things 3 is skipped and not included.

Download [Bubboo 0.1.4](https://github.com/Superoutman/Bubboo/releases/tag/v0.1.4), then download individual `.popclipextz` files from [extension Releases](https://github.com/Superoutman/Bubboo-Extensions/releases/latest). Import through Bubboo Settings and explicitly enable each extension. `SHA256SUMS` verifies download integrity.

**Acceptance is a release gate.** `candidate` and `blocked` entries are review material, not verified downloads. Only entries explicitly marked `verified` in [`catalog/entries.json`](catalog/entries.json) are packaged. Store/import tests alone do not establish real browser, selection replacement, Settings UI or target-app compatibility. Things 3 requires real installed-app acceptance.

## Extension downloads / 扩展下载

Versions below are curated package versions, independent of the Bubboo App version. Each download is an immutable Release asset. Click an extension name for authorship and adaptation details.

表中版本是扩展包版本，不是 App 版本；点击名称查看来源及适配说明。Title Case 仅处理单行英文标题；Base64 使用三个动作按钮，不等同于上游完整选项界面。新增扩展均沿用当前 Bubboo 0.1.4，无需升级主 App。网页扩展验收覆盖默认站点，其他地区站点及 IMDbPro 尚未认证。Amazon 代码为 MIT，图标为 Dave Gandy 的 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，详情见包内署名。

<!-- extension-table:start -->
| 扩展 / Extension | 用途 | 版本 | 最低 Bubboo | 作者 / 许可证 | 下载 |
| --- | --- | --- | --- | --- | --- |
| [Amazon](extensions/Amazon.popclipext/NOTICE.md) | Amazon 检索 | 0.1.0 | 0.1.4 | [Nicholas Moore and contributors](extensions/Amazon.popclipext/NOTICE.md) · [MIT](extensions/Amazon.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/Amazon-0.1.0.popclipextz) |
| [Baidu](extensions/Baidu.popclipext/NOTICE.md) | 百度搜索 | 0.1.0 | 0.1.2 | [Junxue Zhang; Nicholas Moore and contributors](extensions/Baidu.popclipext/NOTICE.md) · [MIT](extensions/Baidu.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/Baidu-0.1.0.popclipextz) |
| [Base64](extensions/Base64.popclipext/NOTICE.md) | UTF-8 编解码，标准 / URL-safe（适配版） | 0.1.0 | 0.1.4 | [Nicholas Moore and contributors](extensions/Base64.popclipext/NOTICE.md) · [MIT](extensions/Base64.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/Base64-0.1.0.popclipextz) |
| [Bing](extensions/Bing.popclipext/NOTICE.md) | Bing 搜索 | 0.1.0 | 0.1.2 | [Morton Fox; Nicholas Moore and contributors. Icon acknowledged upstream as Simple Icons.](extensions/Bing.popclipext/NOTICE.md) · [MIT](extensions/Bing.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/Bing-0.1.0.popclipextz) |
| [Capitalize Words](extensions/Capitalize.popclipext/NOTICE.md) | 单词首字母大写 | 0.1.0 | 0.1.4 | [Nicholas Moore and contributors](extensions/Capitalize.popclipext/NOTICE.md) · [MIT](extensions/Capitalize.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/Capitalize-0.1.0.popclipextz) |
| [Character Count](extensions/CharCount.popclipext/NOTICE.md) | 字符计数 | 0.1.0 | 0.1.2 | [Nicholas Moore and contributors](extensions/CharCount.popclipext/NOTICE.md) · [MIT](extensions/CharCount.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/CharCount-0.1.0.popclipextz) |
| [Comma List](extensions/CommaList.popclipext/NOTICE.md) | 逗号列表与多行互转 | 0.1.0 | 0.1.4 | [Nicholas Moore and contributors](extensions/CommaList.popclipext/NOTICE.md) · [MIT](extensions/CommaList.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/CommaList-0.1.0.popclipextz) |
| [DuckDuckGo](extensions/DuckDuckGo.popclipext/NOTICE.md) | 隐私搜索 | 0.1.0 | 0.1.2 | [Nicholas Moore and contributors](extensions/DuckDuckGo.popclipext/NOTICE.md) · [MIT](extensions/DuckDuckGo.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/DuckDuckGo-0.1.0.popclipextz) |
| [Ebay](extensions/Ebay.popclipext/NOTICE.md) | Ebay 检索 | 0.1.0 | 0.1.4 | [Nicholas Moore and contributors](extensions/Ebay.popclipext/NOTICE.md) · [MIT](extensions/Ebay.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/Ebay-0.1.0.popclipextz) |
| [Full/Half Width](extensions/FullHalfWidth.popclipext/NOTICE.md) | 全角 / 半角转换 | 0.1.0 | 0.1.4 | [Lucifr; Nicholas Moore and contributors](extensions/FullHalfWidth.popclipext/NOTICE.md) · [MIT](extensions/FullHalfWidth.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/FullHalfWidth-0.1.0.popclipextz) |
| [Goodreads](extensions/Goodreads.popclipext/NOTICE.md) | Goodreads 检索 | 0.1.0 | 0.1.4 | [Nicholas Moore and contributors](extensions/Goodreads.popclipext/NOTICE.md) · [MIT](extensions/Goodreads.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/Goodreads-0.1.0.popclipextz) |
| [Google](extensions/GoogleSearch.popclipext/NOTICE.md) | Google 搜索，可选地区站点 | 0.1.0 | 0.1.2 | [Nicholas Moore and contributors](extensions/GoogleSearch.popclipext/NOTICE.md) · [MIT](extensions/GoogleSearch.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/GoogleSearch-0.1.0.popclipextz) |
| [Google Images](extensions/GoogleImages.popclipext/NOTICE.md) | Google Images 检索 | 0.1.0 | 0.1.4 | [Nicholas Moore and contributors](extensions/GoogleImages.popclipext/NOTICE.md) · [MIT](extensions/GoogleImages.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/GoogleImages-0.1.0.popclipextz) |
| [Google Maps](extensions/GoogleMaps.popclipext/NOTICE.md) | 地图搜索 | 0.1.0 | 0.1.2 | [Nicholas Moore and contributors](extensions/GoogleMaps.popclipext/NOTICE.md) · [MIT](extensions/GoogleMaps.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/GoogleMaps-0.1.0.popclipextz) |
| [Google Scholar](extensions/GoogleScholar.popclipext/NOTICE.md) | 学术搜索 | 0.1.0 | 0.1.2 | [Nicholas Moore and contributors](extensions/GoogleScholar.popclipext/NOTICE.md) · [MIT](extensions/GoogleScholar.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/GoogleScholar-0.1.0.popclipextz) |
| [Google Translate](extensions/GoogleTranslate.popclipext/NOTICE.md) | 网页翻译，可选地区站点 | 0.1.0 | 0.1.2 | [Nicholas Moore and contributors](extensions/GoogleTranslate.popclipext/NOTICE.md) · [MIT](extensions/GoogleTranslate.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/GoogleTranslate-0.1.0.popclipextz) |
| [IMDb](extensions/IMDb.popclipext/NOTICE.md) | IMDb 检索 | 0.1.0 | 0.1.4 | [Nicholas Moore and contributors](extensions/IMDb.popclipext/NOTICE.md) · [MIT](extensions/IMDb.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/IMDb-0.1.0.popclipextz) |
| [Join Lines](extensions/JoinLines.popclipext/NOTICE.md) | 合并多行 | 0.1.0 | 0.1.4 | [Nicholas Moore and contributors](extensions/JoinLines.popclipext/NOTICE.md) · [MIT](extensions/JoinLines.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/JoinLines-0.1.0.popclipextz) |
| [Lowercase](extensions/Lowercase.popclipext/NOTICE.md) | 转小写 | 0.1.0 | 0.1.2 | [Nicholas Moore and contributors](extensions/Lowercase.popclipext/NOTICE.md) · [MIT](extensions/Lowercase.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/Lowercase-0.1.0.popclipextz) |
| [PubMed](extensions/PubMed.popclipext/NOTICE.md) | PubMed 检索 | 0.1.0 | 0.1.4 | [Pierre Wizla; Nicholas Moore and contributors](extensions/PubMed.popclipext/NOTICE.md) · [MIT](extensions/PubMed.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/PubMed-0.1.0.popclipextz) |
| [Remove Spaces](extensions/RemoveSpaces.popclipext/NOTICE.md) | 删除空白 | 0.1.0 | 0.1.4 | [Nicholas Moore and contributors](extensions/RemoveSpaces.popclipext/NOTICE.md) · [MIT](extensions/RemoveSpaces.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/RemoveSpaces-0.1.0.popclipextz) |
| [Reverse](extensions/Reverse.popclipext/NOTICE.md) | 反转行序 | 0.1.0 | 0.1.4 | [Nicholas Moore and contributors](extensions/Reverse.popclipext/NOTICE.md) · [MIT](extensions/Reverse.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/Reverse-0.1.0.popclipextz) |
| [Sentence Case](extensions/SentenceCase.popclipext/NOTICE.md) | 句首大写 | 0.1.0 | 0.1.4 | [Nicholas Moore and contributors](extensions/SentenceCase.popclipext/NOTICE.md) · [MIT](extensions/SentenceCase.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/SentenceCase-0.1.0.popclipextz) |
| [Sort](extensions/Sort.popclipext/NOTICE.md) | 自然排序文本行 | 0.1.0 | 0.1.4 | [Agassi; Nicholas Moore and contributors](extensions/Sort.popclipext/NOTICE.md) · [MIT](extensions/Sort.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/Sort-0.1.0.popclipextz) |
| [StartPage](extensions/StartPage.popclipext/NOTICE.md) | StartPage 检索 | 0.1.0 | 0.1.4 | [Nicholas Moore and contributors](extensions/StartPage.popclipext/NOTICE.md) · [MIT](extensions/StartPage.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/StartPage-0.1.0.popclipextz) |
| [Title Case](extensions/TitleCase.popclipext/NOTICE.md) | 英文单行标题大小写（适配版） | 0.1.0 | 0.1.4 | [John Gruber; Aristotle Pagaltzis; Nicholas Moore and contributors](extensions/TitleCase.popclipext/NOTICE.md) · [MIT](extensions/TitleCase.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/TitleCase-0.1.0.popclipextz) |
| [Uppercase](extensions/Uppercase.popclipext/NOTICE.md) | 转大写 | 0.1.0 | 0.1.2 | [Nicholas Moore and contributors](extensions/Uppercase.popclipext/NOTICE.md) · [MIT](extensions/Uppercase.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/Uppercase-0.1.0.popclipextz) |
| [Urban Dictionary](extensions/UrbanDictionary.popclipext/NOTICE.md) | Urban Dictionary 检索 | 0.1.0 | 0.1.4 | [zhiyelee; Nicholas Moore and contributors](extensions/UrbanDictionary.popclipext/NOTICE.md) · [MIT](extensions/UrbanDictionary.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/UrbanDictionary-0.1.0.popclipextz) |
| [URL Encode](extensions/URLEncode.popclipext/NOTICE.md) | URL 编码 / 解码 | 0.1.0 | 0.1.2 | [Nicholas Moore and contributors; original Perl extension by Brett Terpstra.](extensions/URLEncode.popclipext/NOTICE.md) · [MIT](extensions/URLEncode.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/URLEncode-0.1.0.popclipextz) |
| [Wikipedia](extensions/Wikipedia.popclipext/NOTICE.md) | 维基百科，可选语言站点 | 0.1.0 | 0.1.2 | [Nicholas Moore and contributors](extensions/Wikipedia.popclipext/NOTICE.md) · [MIT](extensions/Wikipedia.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/Wikipedia-0.1.0.popclipextz) |
| [YouTube](extensions/YouTube.popclipext/NOTICE.md) | 视频搜索 | 0.1.0 | 0.1.2 | [Nicholas Moore and contributors](extensions/YouTube.popclipext/NOTICE.md) · [MIT](extensions/YouTube.popclipext/LICENSE.txt) | [下载 / Download](https://github.com/Superoutman/Bubboo-Extensions/releases/download/v0.1.3/YouTube-0.1.0.popclipextz) |
<!-- extension-table:end -->

## Validate and build

Requires Python 3.10+; standard library only.

```sh
python3 scripts/build.py --check
python3 scripts/test_build.py
python3 scripts/build.py --output dist
```

When no entries are verified, the final command fails without producing artifacts. Output must be absent or empty to avoid carrying old downloads into a release. Build results are deterministic `.popclipextz` ZIPs, `catalog.json`, and `SHA256SUMS`. Each archive retains the original package directory, `LICENSE.txt`, `NOTICE.md` and `UPSTREAM.json`. SHA-256 hashes detect content changes; they do not establish publisher identity or replace Bubboo's explicit trust approval.

## Maintenance and publication

1. Submit a PR with one focused package change, upstream commit, author, license and adaptation notes. Keep the original source format. Do not include Bubboo private application sources, user preferences, credentials or personal acceptance data.
2. Review provenance and licensing; record each modification in the package's `NOTICE.md` and `UPSTREAM.json`. Adapted extension identity is documented there; no package is represented as an unmodified upstream release unless it is one.
3. Run import/trust tests and real end-to-end acceptance on the stated minimum Bubboo version. Record evidence in `acceptance`, set a verified `minimumBubbooVersion` (or an exact `testedBubbooBuild` for development-only prereleases), and only then change status to `verified`. Review every updated package again and bump its curated `version`.
4. PR CI runs validation and isolated build tests with read-only permissions. It never executes extension code, publishes a release or reads release secrets.
5. Publication plan: after maintainer approval, tag the reviewed commit, run the deterministic build from that exact tag, verify `SHA256SUMS`, then attach the generated archives, index and checksums to its GitHub Release. A future tag workflow should use a protected release environment and `contents: write` only in that publication job. **Automatic release publishing is not enabled in this repository.**

The generated catalog records artifact filenames relative to the same Release, author/license/provenance, minimum app version, acceptance reference and archive hash. Keep application/Sparkle releases separate. Raw candidate folders remain available for review and should not be advertised as compatible downloads.

## 中文说明

**当前正式合集：15 项。原有 13 项最低兼容 Bubboo 0.1.2；新增 Title Case、Base64 在 Bubboo 0.1.4（build 5）通过端到端验收。Things 3 暂不包含。**

这是 Bubboo 的精选扩展源码与下载仓库，保留 PopClip 原格式、原作者及许可证。未来可以纳入经过独立验收的 OpenClip 原格式扩展，当前不声称已支持。

- `candidate`：等待端到端验收；`blocked`：验收条件缺失；`verified`：已完成记录中的验收，允许打包。
- 仅验证导入成功不等于正式兼容，浏览器跳转、配置生效、焦点回填和目标 App 都需按实际能力验收。
- 构建只读取显式清单中 `verified` 的条目；零通过条目时拒绝生成发布附件，不伪造通过状态。
- 每个归档都带 `LICENSE.txt`、`NOTICE.md`、`UPSTREAM.json`，修改需说明来源和差异。根目录脚本使用 MIT；各扩展以各自许可证为准，不能把第三方代码称为自有原创。
- 公共 PR 自动执行只读校验；发布需先完成验收、合并审核、打 tag，再将该 tag 构建出的附件上传 GitHub Release。当前没有自动上传权限或发布任务。
- 每次上游更新重新验收；扩展版本、目录和下载与 Bubboo App/Sparkle 更新分开维护。

## Manual extension updates (Bubboo 0.1.3 or later)

Bubboo 0.1.4 checks the small static `catalog/updates.json` when Settings opens (0.1.3 uses a manual check button). It caches the catalog for six hours and uses ETag revalidation. It downloads a selected archive only when the user clicks Update. There is no automatic installation.

The feed maps exact package content hashes to curated versions. Modified or unknown third-party packages are excluded; older recognized versions can upgrade without changing identifiers or original package formats. Application settings remain outside packages and survive replacement. Changed content always needs fresh approval.

After publishing a stable extension Release:
1. Download its `catalog.json` and archives using `gh release download <tag>`.
2. Run `python3 scripts/update_feed.py --assets <download-directory> --tag <tag>`.
3. Run `python3 scripts/test_update_feed.py`, review the generated history, and commit `catalog/updates.json` only after verifying the public downloads. Do not delete historical content hashes; they identify older installations.
4. Run `python3 scripts/render_readme.py` to refresh the download table from the verified feed. Review and commit the table with the feed so versions and links stay consistent.
5. Changed package content must increment its curated version. Never overwrite an existing Release archive.

All release preparation remains local. The public Ubuntu validation job uploads no artifacts or cache; repository Actions paid usage is capped at $0.

### Sync the App download page

After verifying release assets and regenerating `catalog/updates.json`, run locally:

```sh
python3 scripts/render_readme.py --app-repo ../Bubboo-public
```

This updates the extension table here and both public App READMEs from the same catalog, rewriting attribution links to absolute URLs. Commit and push the documentation changes in both repositories. Keep the public App anchor `#extensions` stable; the App download button targets it. No GitHub workflow or App release is needed for table updates.
