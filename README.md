# Portfolio

My developer portfolio — a single page in plain HTML, CSS and JavaScript,
no framework and no build tooling beyond one small Python script.

**Live:** https://portfolio.web-globus.de/

## What's in it

- **Two modes.** The page opens on the portfolio; a small two-button switch in
  the header flips to an "atmosphere" view (a zen-garden gallery) and back.
  Either button flips the mode.
- **Project cards** with their own text / images switch. In images mode the
  card turns light so the dark screenshots stay readable.
- **Hand-rolled EN/DE i18n** — a dictionary per language and `data-i18n`
  attributes, no library.
- **Lightbox as a real dialog** — `role="dialog"`, focus moves in on open, is
  kept inside while open (Tab cycles), and returns to the thumbnail on close.
  Keyboard: Enter/Space to open, arrows to navigate, Esc to close.
- **No third-party requests.** Fonts are self-hosted (latin subset from
  Fontsource) instead of Google Fonts, so no visitor IP leaves the page.
- Respects `prefers-reduced-motion`.

## Structure

```
src/index.html   the page: markup, styles and script in one readable file
src/assets/      screenshots, garden images, logo
src/fonts/       Shippori Mincho, Manrope, JetBrains Mono (woff2, latin)
build.py         inlines assets and fonts -> dist/index.html (one portable file)
```

`src/index.html` works directly in a browser. The single-file build exists so
the whole site can be sent or hosted as one file:

```bash
python3 build.py                                  # -> dist/index.html
python3 -m http.server 8000 --directory src       # local preview
```

Deployment: `dist/index.html` is copied to the web root of my VPS.

## Credits

Fonts: Shippori Mincho, Manrope, JetBrains Mono — SIL Open Font License,
packaged by [Fontsource](https://fontsource.org).
