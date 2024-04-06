import random
import string
import time

import pytest
from selenium.webdriver.common.by import By

from PageObjects.AddCustomer_Page import AddCustomer
from Utilities import readProperties
from Utilities.customLogger import LogGen
from PageObjects.LoginPage import LoginPage

class Test_003_AddCustomer():
    baseUrl=readProperties.readConfig.getUrl()
    username=readProperties.readConfig.getEmail()
    password=readProperties.readConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("Test_003_AddCustomer")

        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)

        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("Login Successful")

        self.logger.info("start_AddCustomer")
        self.addCust=AddCustomer(self.driver)

        self.addCust.clickOnCustomrMenu()
        self.addCust.clickOnCustomerMenuItem()
        time.sleep(3)

        self.addCust.clickAddfCustomer()

        self.logger.info("Provide customer details")

        self.email=random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("hjhjh78#")
        self.addCust.setFname("Raju")
        self.addCust.setlname("Kumar")
        self.addCust.setGender("Male")
        self.addCust.setDOB("11/02/1998")
        self.addCust.setCompany("Euroo")
        self.addCust.setTaxExempt()
        self.addCust.setNewsletter("Your store name")
        self.addCust.setCustomerRole("Guests")
        #self.addCust.setCustomerRole("Administrator")
        self.addCust.setManagerVendor("Vendor 1")
        self.addCust.SaveCustomer()
        time.sleep(3)

        self.logger.info("Saving customer Info")

        self.msg=self.driver.find_elements(By.TAG_NAME,"body")

        if "The new customer has been added successfully." in self.msg:
            assert True==True
            self.logger.info("add customer test case passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer.png")
            self.logger.info("Add customer testcase failed")
            assert True == False

        self.driver.close()
        self.logger.info("Ending add customer test")



def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return "".join(random.choice(chars) for x in range(size))