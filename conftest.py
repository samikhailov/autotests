import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language") or 'en'
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print("\nStart Chrome for test.")
    browser = webdriver.Chrome(options=options)
        
    yield browser
    print("\nQuit browser.")
    browser.quit()
