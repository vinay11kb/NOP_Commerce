#put common things here

import pytest
from selenium import webdriver

from pytest_metadata.plugin import metadata


#when we call the fixture it will return the driver for us
@pytest.fixture
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
    else:
        driver=webdriver.Edge()
    return driver

#this will get value from cli
def pytest_addoption(parser):
    parser.addoption("--browser")


#this will return the browser value to setupmethod
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



############Pytest HTML report#########
#hook to add enviroment info to html report
# def pytest_configuration(config):
#     config._metadata['Project Name']='Nop Commerce'
#     config._metadata['Module Name']='Customers'
#     config._metadata['Tester']='Vinay'

#hook for delete/modify enviroment info to html
# @pytest.hookimpl(optionalhook=True)
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME",None)
#     metadata.pop("Plugins",None)
