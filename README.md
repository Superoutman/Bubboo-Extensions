# Bubboo Extensions

A curated collection of original-format PopClip extensions for Bubboo. Authors, licenses and upstream provenance stay with each package. OpenClip support is a future runtime milestone; no new extension format is introduced here.

## Current stable collection

**13 extensions verified with Bubboo 0.1.2 or later.** [Release acceptance](acceptance/bubboo-0.1.2/README.md). Things 3 is skipped and not included.

Download [Bubboo 0.1.2](https://github.com/Superoutman/Bubboo/releases/tag/v0.1.2), then download individual `.popclipextz` files from [extension Releases](https://github.com/Superoutman/Bubboo-Extensions/releases/latest). Import through Bubboo Settings and explicitly enable each extension. `SHA256SUMS` verifies download integrity.

**Acceptance is a release gate.** `candidate` and `blocked` entries are review material, not verified downloads. Only entries explicitly marked `verified` in [`catalog/entries.json`](catalog/entries.json) are packaged. Store/import tests alone do not establish real browser, selection replacement, Settings UI or target-app compatibility. Things 3 requires real installed-app acceptance.

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

**当前正式合集：13 项已在 Bubboo 0.1.2（build 3）正式构建完成端到端复验，最低兼容版本为 0.1.2；Things 3 暂不包含。**

这是 Bubboo 的精选扩展源码与下载仓库，保留 PopClip 原格式、原作者及许可证。未来可以纳入经过独立验收的 OpenClip 原格式扩展，当前不声称已支持。

- `candidate`：等待端到端验收；`blocked`：验收条件缺失；`verified`：已完成记录中的验收，允许打包。
- 仅验证导入成功不等于正式兼容，浏览器跳转、配置生效、焦点回填和目标 App 都需按实际能力验收。
- 构建只读取显式清单中 `verified` 的条目；零通过条目时拒绝生成发布附件，不伪造通过状态。
- 每个归档都带 `LICENSE.txt`、`NOTICE.md`、`UPSTREAM.json`，修改需说明来源和差异。根目录脚本使用 MIT；各扩展以各自许可证为准，不能把第三方代码称为自有原创。
- 公共 PR 自动执行只读校验；发布需先完成验收、合并审核、打 tag，再将该 tag 构建出的附件上传 GitHub Release。当前没有自动上传权限或发布任务。
- 每次上游更新重新验收；扩展版本、目录和下载与 Bubboo App/Sparkle 更新分开维护。

## Manual extension updates (Bubboo 0.1.3 development build)

The app checks the small static `catalog/updates.json` only on request. It caches the catalog for six hours and uses ETag revalidation. It downloads a selected archive only when the user clicks Update. There is no automatic installation.

The feed maps exact package content hashes to curated versions. Modified or unknown third-party packages are excluded; older recognized versions can upgrade without changing identifiers or original package formats. Application settings remain outside packages and survive replacement. Changed content always needs fresh approval.

After publishing a stable extension Release:
1. Download its `catalog.json` and archives using `gh release download <tag>`.
2. Run `python3 scripts/update_feed.py --assets <download-directory> --tag <tag>`.
3. Run `python3 scripts/test_update_feed.py`, review the generated history, and commit `catalog/updates.json` only after verifying the public downloads. Do not delete historical content hashes; they identify older installations.
4. Changed package content must increment its curated version. Never overwrite an existing Release archive.

All release preparation remains local. The public Ubuntu validation job uploads no artifacts or cache; repository Actions paid usage is capped at $0.
