import pytest
SYSTEM_VERSION = "v1.2.0"

@pytest.mark.skipif(
    SYSTEM_VERSION == "v3.3.3"
)
def test_system_version_valid():
    ...

@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.2.0"
)
def test_system_version_invalid():
    ...
