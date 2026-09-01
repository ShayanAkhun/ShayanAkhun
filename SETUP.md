# Setup — Shayan's profile README

This repo is a fork of [Andrew6rant](https://github.com/Andrew6rant/Andrew6rant)'s
"neofetch" GitHub profile README. `today.py` pulls live GitHub stats each day and
writes them into `light_mode.svg` / `dark_mode.svg`; `README.md` embeds those SVGs.

## What's already done

- `README.md` points at `ShayanAkhun/ShayanAkhun`
- `today.py` birthday set to **2000-02-21**
- Both SVGs rebuilt: name `shayan@ghori`, OS `Windows 11`, role `Full Stack Developer`,
  languages `Kotlin, TypeScript, JavaScript, Node.js`, new ASCII portrait, canvas widened to 1160px
- Workflow bumped to `actions/checkout@v4` + `setup-python@v5` + Python 3.12, added
  `permissions: contents: write` and a manual `workflow_dispatch` trigger
- Andrew's stale LOC cache removed; `cache/repository_archive.txt` is inert (guarded by an
  owner-ID check in `today.py` that only matches Andrew)

## TODO — fill in your real values

Edit **both** `light_mode.svg` and `dark_mode.svg` (same lines in each). Only the
plain-text `<tspan class="value">` bits — the `id="..."` ones are filled by the script.

Everything is filled in. Nothing left to do here — just publish (below).

If a value gets longer/shorter, tweak the dot count in the preceding
`<tspan class="cc"> ... </tspan>` so it still lines up (or just leave it — it's cosmetic).

## Publish it

1. Create a **public** repo named exactly `ShayanAkhun` (GitHub shows its README on your profile).
2. Push these files to the `main` branch.
3. Repo → Settings → Secrets and variables → Actions → add:
   - `USER_NAME` = `ShayanAkhun`
   - `ACCESS_TOKEN` = a fine-grained Personal Access Token (Settings → Developer settings →
     Fine-grained tokens), all repositories, read-only:
     - Account permissions: Followers, Starring, Watching
     - Repository permissions: Commit statuses, Contents, Issues, Metadata, Pull requests
4. Repo → Settings → Actions → General → Workflow permissions → **Read and write permissions**.
5. Actions tab → "README build" → **Run workflow** to trigger the first build, then it runs
   daily at 04:00 UTC.

## Regenerate the ASCII portrait

`tools/ascii.py` (Pillow — `pip install Pillow`) converts an image to the `<tspan>` block.
Set `SRC` to your image path first. Adjust `W`
(character width — keep ≤ 40 so it doesn't overlap the text panel at x=420) and the
`g` gamma, run it, paste the output over the `class="ascii"` block in both SVGs.
