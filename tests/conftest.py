import pytest, boto3
import selenium
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote

#AWS_ACCESS_KEY_ID= "AKIAWZV2OPV3QAF4JFGT"
#AWS_SECRET_ACCESS_KEY="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"
driver = None   #Aula 103

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")


@pytest.fixture(scope="class")
def setup(request):

    global driver

    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        pass

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = False
        driver = webdriver.Firefox(options=options)

    driver.implicitly_wait(8)
    driver.get("https://www.eu-startups.com/directory/")
    driver.maximize_window()

    request.cls.driver = driver


    yield           #teardown
    #driver.quit()