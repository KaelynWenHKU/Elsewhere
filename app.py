#!/usr/bin/env python3
"""
Python entrypoint for Kaelyn's Presence app.

Run:
    python3 edit/app.py

Then open:
    http://127.0.0.1:8092/index.html

This serves the application from the project root so the HTML, JS, images,
LCC manifest, and iteration_100 3D resources keep their existing paths.
"""

from __future__ import annotations

import argparse
import functools
import http.server
import socketserver
from pathlib import Path


APP_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = APP_DIR.parent
DEFAULT_PORT = 8092


class AppRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        super().end_headers()

    def do_GET(self) -> None:
        if self.path == "/":
            self.path = "/index.html"
        super().do_GET()


def main() -> None:
    parser = argparse.ArgumentParser(description="Serve Kaelyn's Presence app.")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Local port to serve on.")
    args = parser.parse_args()

    handler = functools.partial(AppRequestHandler, directory=str(PROJECT_ROOT))
    with socketserver.TCPServer(("127.0.0.1", args.port), handler) as httpd:
        print("Kaelyn's Presence app is running.")
        print(f"Project root: {PROJECT_ROOT}")
        print(f"Open: http://127.0.0.1:{args.port}/index.html")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
