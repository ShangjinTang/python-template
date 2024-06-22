import nox

nox.options.sessions = ["pytest"]


@nox.session(tags=["test"])
def pytest(session):
    session.install("pytest")
    session.run("pytest")


@nox.session(tags=["fix"])
def black(session):
    session.install("black")
    session.run("black", "src", "tests")


@nox.session(tags=["fix"])
def isort(session):
    session.install("isort")
    session.run("isort", "src", "tests")
