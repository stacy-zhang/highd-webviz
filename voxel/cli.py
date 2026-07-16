"""Command-line entry point for the Voxel web application.

Kept inside the package so the app is launched idiomatically with
``python -m voxel`` (see ``voxel/__main__.py``) and via the ``pixi run start``
task.
"""

import argparse
from typing import Optional, Sequence

from voxel.app.server import run_server


def main(argv: Optional[Sequence[str]] = None) -> None:
    parser = argparse.ArgumentParser(
        description="Launch the Voxel (Napari ResView) web application using Trame."
    )
    parser.add_argument(
        "--port",
        type=int,
        default=0,
        help="Port to bind the Trame server (0 = auto).",
    )
    parser.add_argument(
        "--host",
        type=str,
        default="localhost",
        help="Host address to bind the server.",
    )
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Do not open the browser automatically.",
    )
    args = parser.parse_args(argv)

    run_server(port=args.port, host=args.host, open_browser=not args.no_browser)


if __name__ == "__main__":
    main()
