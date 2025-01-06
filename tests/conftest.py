import pytest


def pytest_addoption(parser):
    parser.addoption("--domain", action="store", default="document.invoice", help="Domain to test")


@pytest.fixture
def domain_arg(request):
    """Domain fixture for testing"""
    return request.config.getoption("--domain")
