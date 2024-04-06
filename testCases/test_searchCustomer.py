import time

import pytest

from Utilities.readProperties import readConfig
from Utilities.customLogger import LogGen
# from conftest import setup
from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomer_Page import AddCustomer
from PageObjects.SearchCustomer_Page import SearchCustomer

class Test_004_SearchCust():
    baseUrl=readConfig.getUrl()
    username=readConfig.getEmail()
    password=readConfig.getPassword()
    logger=LogGen.loggen()


    @pytest.mark.regression
    def testSearchCustomer(self,setup):
        self.driver=setup

        self.logger.info("TC004_Search Customer testcase started")
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.ln=LoginPage(self.driver)

        self.logger.info("LOgin ")
        self.ln.setUserName(self.username)
        self.ln.setPassword(self.password)
        self.ln.clickLogin()
        time.sleep(3)

        self.logger.info("Go to cutomer Menu")
        self.addCust=AddCustomer(self.driver)
        self.addCust.clickOnCustomrMenu()
        self.addCust.clickOnCustomerMenuItem()
        time.sleep(2)

        self.logger.info("Search customer")
        self.search=SearchCustomer(self.driver)
        self.search.setEmail("kiyjcycyhjc676008@gmail.com")

        time.sleep(2)
        self.search.clickBtn()
        time.sleep(3)

        status=self.search.searchCustomerByEmail("kiyjcycyhjc676008@gmail.com")
        assert True==status
        self.logger.info("Search customer test end")

        self.driver.close()



