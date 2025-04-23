import platform
import pytest


def some_cross_platform_func():
    '''Какая то кросплатформенная функция(работает на всех системах)'''
    return True
    
def some_linux_func():
    if 'linux' in platform.architecture()[1].lower():
        return "Linux specific code"
    else:
        return Exception("Not linux system")

@pytest.mark.skipif(
    'linux' not in platform.architecture()[1].lower(),
    reason = "Тест поддерживается только на системах Linux"
    )
def test_linux_only_funcionality():
    assert some_linux_func() == "Linux specific code"

@pytest.mark.skip(reason='Функция не готова')
def test_windows_only_functionality():
    assert some_cross_platform_func()