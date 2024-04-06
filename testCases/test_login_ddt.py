import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import readConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils

class Test_002_Login_ddt:
    base_url=readConfig.getUrl()
    path=".//testData/beta.xlsx"

    # username=readConfig.getEmail()
    # password=readConfig.getPassword()
    logger=LogGen.loggen() #return logger obect





    # def test_homePageTitle(self,setup):  #setup is fixture here for driver
    #     self.logger.info("********Test_001_Login******")
    #     self.logger.info("********Verify homePage title******")
    #     self.driver=setup
    #     self.driver.get(self.base_url)
    #     act_title=self.driver.title
    #     self.driver.close()
    #     if act_title=="Your store. Login":
    #         assert True
    #         self.logger.info("*******HomePageTitle Passed******")
    #     else:
    #        # self.driver.save_screenshot("D:\selenium_python\NOP_Commerce\Screenshots\test_homeTitle.png")
    #         assert False
    #
    #         self.logger.info("*******HomePageTitle Failed******")

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("*******Verify login test******")

        self.driver=setup
        self.driver.get(self.base_url)
        time.sleep(2)

        #create object loginPage
        self.lp=LoginPage(self.driver)

        #rows
        rows=XLUtils.getRowCount(self.path,"Sheet1")
        self.logger.info(rows)

        lst_status=[]  #emt list
        for r in range(2,rows-1):
            self.user=XLUtils.readData(self.path,"Sheet1",r,1)
            self.password=XLUtils.readData(self.path,"Sheet1",r,2)
            self.exp=XLUtils.readData(self.path,"Sheet1",r,3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            time.sleep(2)
            self.lp.clickLogin()
            time.sleep(4)

            act_title=self.driver.title
            if act_title=="Dashboard / nopCommerce administration":
                if self.exp=="Pass":
                    assert True
                    self.logger.info("*****Passed******")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    assert False
                    self.logger.info("*******Failed******")
                    #self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title!="Dashboard / nopCommerce administration":
                if self.exp=="Pass":
                    assert False
                    self.logger.info("*******Failed******")
                   # self.lp.clickLogout()
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    assert True
                    self.logger.info("*******Passed******")
                   # self.lp.clickLogout()
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("ddt test passed")
            self.driver.close()
            assert True

        else:
            self.logger.info("ddt test failed")
            self.driver.close()
            assert False


        self.logger.info("End of test")








