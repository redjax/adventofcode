from __future__ import annotations

import nox

@nox.session(name="ruff-lint")
def ruff_lint(session: nox.Session):
    session.install("ruff")
    session.run("ruff", "check", "--fix", "years", "noxfile.py")
