import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer():

    #add customer page
    lnkCustomer_menu_xpath="//a[@href='#']/p[contains(text(),'Customers')]"
    lnkCustomer_menuItem_xpath="//a[@href='/Admin/Customer/List']/p[contains(text(),'Customers')]"
    btnAddnew_xpath="//a[@class='btn btn-primary']"

    email_xpath="//input[@name='Email']"
    password_xpath="//input[@name='Password']"
    fname_xpath="//input[@name='FirstName']"
    lname_xpath="//input[@name='LastName']"
    genderMale_id="Gender_Male"
    genderFemale_id="Gender_Female"
    dob_xpath="//input[@name='DateOfBirth']"
    companyName_xpath="//input[@name='Company']"
    taxExempt_id="IsTaxExempt"
    newsletter_xpath="//div[@class='k-widget k-multiselect k-multiselect-clearable']"
    yourName_xpath="//li[contains(text(),'Your store name')]"
    testStore_xpath="//li[contains(text(),'Test store 2')]"
    customerRoles_xpath="//div[@class='k-multiselect-wrap k-floatwrap']"
    Administrator_xpath="//li[contains(text(),'Administrators')]"
    Registered_xpath="//li[contains(text(),'Registered')]"
    ForumModerators_xpath="//li[contains(text(),'Forum Moderators')]"
    guest_xpath="//li[contains(text(),'Guests')]"
    vendors_xpath="//li[contains(text(),'Vendors')]"

    managerVendor_ddl_id="VendorId"
    active_id="Active"
    button_save_xpath="//button[@name='save']"


    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomrMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomer_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomer_menuItem_xpath).click()

    def clickAddfCustomer(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.email_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(password)

    def setFname(self,fname):
        self.driver.find_element(By.XPATH,self.fname_xpath).send_keys(fname)

    def setlname(self,lname):
        self.driver.find_element(By.XPATH,self.lname_xpath).send_keys(lname)


    def setGender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.ID,self.genderMale_id)
        else:
            self.driver.find_element(By.ID,self.genderFemale_id)


    def setDOB(self,dob):
        self.driver.find_element(By.XPATH,self.dob_xpath).send_keys(dob)

    def setCompany(self,name):
        self.driver.find_element(By.XPATH,self.companyName_xpath).send_keys(name)

    def setTaxExempt(self):
        self.driver.find_element(By.ID,self.taxExempt_id).click()

    def setNewsletter(self,newsletter):
        self.driver.find_element(By.XPATH,self.newsletter_xpath).click()

        if newsletter=="Your store name":
            self.lst=self.driver.find_element(By.XPATH,self.yourName_xpath)
        else:
            self.lst=self.driver.find_element(By.XPATH,self.testStore_xpath)

        self.driver.execute_script("arguments[0].click();",self.lst)

    def setCustomerRole(self,role):
        self.driver.find_element(By.XPATH,self.customerRoles_xpath).click()
        time.sleep(3)
        if role=="Registered":
            self.list=self.driver.find_element(By.XPATH,self.Registered_xpath)
        elif role=="Administrator":
            self.list=self.driver.find_element(By.XPATH,self.Administrator_xpath)

        elif role=="Guests":
            self.driver.find_element(By.XPATH,"//span[@title='delete']").click()
            self.list=self.driver.find_element(By.XPATH,self.guest_xpath)
        elif role=="Registered":
            self.list=self.driver.find_element(By.XPATH,self.Registered_xpath)
        elif role=="Vendors":
            self.list=self.driver.find_element(By.XPATH,self.vendors_xpath)
        else:
            self.list=self.driver.find_element(By.XPATH,self.guest_xpath)
        time.sleep(3)

        #self.list.click()
        #if click not works use execute javascript
        self.driver.execute_script("arguments[0].click();",self.list)

    def setManagerVendor(self,value):
        drp=self.driver.find_element(By.ID,self.managerVendor_ddl_id)
        Select(drp).select_by_visible_text(value)  #dropdown
        time.sleep(3)

    def setActive(self):
        self.driver.find_element(By.ID,self.active_id).click()

    def SaveCustomer(self):
        self.driver.find_element(By.XPATH,self.button_save_xpath).click()





