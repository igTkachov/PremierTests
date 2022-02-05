
def pytest_addoption(parser):
    parser.addoption('--browser', action="append", default=[], choices=['chrome', 'firefox'],
                     help='Config browser for run tests')