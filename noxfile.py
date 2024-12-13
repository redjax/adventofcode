from __future__ import annotations
import logging

import socket
import nox

log = logging.getLogger("nox")
logging.basicConfig(level="DEBUG", format="%(asctime)s %(levelname)s %(name)s:%(lineno)d %(message)s", datefmt="%Y-%m-%d %H:%M:%S")


@nox.session(name="ruff-lint")
def ruff_lint(session: nox.Session):
    log.info("Installing ruff")
    session.install("ruff")
    
    log.info("Checking code with ruff")
    session.run("ruff", "check", "--fix", "years", "noxfile.py")
