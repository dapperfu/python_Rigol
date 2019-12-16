import sys
from time import sleep
from uuid import uuid4

import pytest

import rigol
import rigol.usbtmc
import rigol.rigol

import rigol.key


@pytest.yield_fixture(scope="module")
def module_uuid():
    """
    Unit Test Module UUID.
    Yields:
        uuid.uuid4()
    """
    yield uuid.uuid4()


@pytest.yield_fixture(scope="session")
def session_uuid():
    """
    Unit Test Session UUID.
    Yields:
        uuid.uuid4()
    """    
    yield uuid.uuid4()


@pytest.yield_fixture(scope="function")
def function_uuid():
    """
    Unit Test Function UUID.
    Yields:
        uuid.uuid4()
    """
    yield uuid.uuid4()

def pytest_addoption(parser):
    parser.addoption(
        "--device_path",
        action="store",
        default="",
        help="Device Path.",
    )


@pytest.fixture(scope='session')
def device_path(request):
    cfg_port = request.config.getoption("--device_path")
    if len(cfg_port) == 0:
        cfg_port = "/dev/usbtmc0"
    return cfg_port

@pytest.fixture(scope='function')
def device(device_path):
    """Return Usbtmc object"""
    return rigol.usbtmc.Usbtmc(device_path)


@pytest.fixture(scope='function')
def device_gen(device_path):
    """Usbtmc generator in context manager."""
    with rigol.usbtmc.Usbtmc(device_path) as device:
        yield device

@pytest.fixture(scope='function')
def scope(device):
    """Return RigolScope object."""
    return rigol.rigol.RigolScope(device=device)

def scope_gen(device):
    """RigolScope generator in context manager."""
    with rigol.rigol.RigolScope(device=device) as scope:
        yield scope
