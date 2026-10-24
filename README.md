# SCP: Containment Breach 3DS - website

Static retro-style site for the 3DS fan port, served by GitHub Pages: https://serqay.github.io/3dsScpSite/

- `index.html`, `screenshots.html`, `download.html`, `style.css`: plain HTML/CSS, no build step
- `img/`: images; `tools/make_decor.py` redraws the decorative ones (needs Pillow)
- Game builds live in this repo's Releases under fixed names (`scpcb3ds_old.3dsx/.cia`, `scpcb3ds_new.3dsx/.cia`),
  the download page links to `releases/latest/download/<name>`
