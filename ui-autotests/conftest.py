
def pytest_addoption(parser):
    parser.addoption(
        "--browser",  action='store', default="chrome", help="Config browser for run tests"
    )
