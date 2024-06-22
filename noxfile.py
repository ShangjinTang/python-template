import nox


@nox.session(tags=["test"])
def pytest(session):
    session.install("pytest")
    session.run("pytest")
