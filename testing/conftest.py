import pytest


@pytest.fixture(scope='function', autouse=True)
def login():
    print("\n[计算开始]")
    yield
    print("[计算结束]\n")
