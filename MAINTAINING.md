# Maintaining the extension collection

## Acceptance records

Only entries marked `verified` are packaged. `candidate` and `blocked` entries are review material, not supported downloads. Import tests alone do not establish end-to-end compatibility.

- [Batch 1](acceptance/bubboo-0.1.2/README.md)
- [Batch 2](acceptance/bubboo-0.1.4-batch2/README.md)
- [Batch 3](acceptance/bubboo-0.1.4-batch3/README.md)

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
