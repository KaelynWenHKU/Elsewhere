# Edit Python Version

This folder contains the Python entrypoint for the current application.

Run from the project root:

```bash
python3 edit/app.py
```

Then open:

```text
http://127.0.0.1:8092/index.html
```

The Python server intentionally serves the parent project folder so the app can still use:

- `index.html`
- `presence_unified.html`
- `kaelyn_mesh_embed.js`
- `kaelyn_iteration_lod.js`
- `绿色样板房/Output/...`

This avoids duplicating the very large 3D files while preserving the full app.
