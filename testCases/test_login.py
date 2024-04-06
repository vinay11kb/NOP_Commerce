import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import readConfig
from Utilities.customLogger import LogGen


class Test_001_Login:
    base_url=readConfig.getUrl()
    username=readConfig.getEmail()
    password=readConfig.getPassword()
    logger=LogGen.loggen() #return logger obect




    
    @pytest.mark.regression
    def test_homePageTitle(self,setup):  #setup is fixture here for driver
        self.logger.info("********Test_001_Login******")
        self.logger.info("********Verify homePage title******")
        self.driver=setup
        self.driver.get(self.base_url)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Your store. Login":
            assert True
            self.logger.info("*******HomePageTitle Passed******")
        else:
           # self.driver.save_screenshot("D:\selenium_python\NOP_Commerce\Screenshots\test_homeTitle.png")
            assert False
            self.logger.info("*******HomePageTitle Failed******")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("*******Verify login test******")

        self.driver=setup
        self.driver.get(self.base_url)
        time.sleep(2)
        #create object loginPage
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        time.sleep(1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        self.driver.close()

        if act_title=="Dashboard / nopCommerce administration":
            assert True
            # self.driver.close()
            self.logger.info("*******Login Test Passed******")

        else:
            #take screenshot for failure
           # self.driver.save_screenshot("D:\selenium_python\NOP_Commerce\Screenshots\test_login.png")
            assert False
            #self.driver.close()
            self.logger.info("*******Login test Failed******")



