# conftest.py
import pytest
import logging

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Type in browser type"
    )

@pytest.fixture(scope="session")
def driver(request):
    browser_type = request.config.getoption("browser")
    if browser_type == "firefox":
        # Initialize FirefoxOptions
        firefox_options = FirefoxOptions()
        #firefox_options.add_argument("--headless")  # Add any other options you need
        # Create Firefox service
        firefox_service = FirefoxService(GeckoDriverManager().install())
        # Initialize WebDriver
        driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
    elif browser_type == "chrome":
        # Initialize ChromeOptions
        chrome_options = ChromeOptions()
        #chrome_options.add_argument("--headless")  # Add any other options you need
        # Create Chrome service
        chrome_service = ChromeService(ChromeDriverManager().install())
        # Initialize WebDriver
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    else:
        raise pytest.UsageError("--browser option should be firefox or chrome")
    yield driver
    driver.quit()

# Create a fixture for the logger
@pytest.fixture(scope="session")
def logger():
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create a file handler
    file_handler = logging.FileHandler('logs/logs.log')
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    # Create a stream handler (for console output)
    stream_handler = logging.StreamHandler()
    stream_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(stream_formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger