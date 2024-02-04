import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language")



@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language == "ru":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
        browser = webdriver.Chrome(options=options)
    elif language == "en-gb":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en-gb'})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be ru or en-gb")
    yield browser
    print("\nquit browser..")
    browser.quit()