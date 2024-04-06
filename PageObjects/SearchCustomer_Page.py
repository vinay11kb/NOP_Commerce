from selenium.webdriver.common.by import By


class SearchCustomer:
    email_id="SearchEmail"
    fname_id="SearchFirstName"
    lname_id="SearchLastName"
    btnSearch_id="search-customers"
        #table
    tblSearchResult_xpath="//table[@roles='grid']"
    table_xpath="//table[@id='customers-grid']"
    tableRows_xpath="//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath="//table[@id='customers-grid']//tbody/tr/td"


    def __init__(self, driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.email_id).clear()
        self.driver.find_element(By.ID,self.email_id).send_keys(email)

    def setFname(self,fname):
        self.driver.find_element(By.ID,self.fname_id).clear()
        self.driver.find_element(By.ID, self.fname_id).send_keys(fname)

    def setLname(self,lname):
        self.driver.find_element(By.ID, self.lname_id).clear()
        self.driver.find_element(By.ID, self.lname_id).send_keys(lname)

    def clickBtn(self):
        self.driver.find_element(By.ID,self.btnSearch_id).click()

    def getRows(self):
        return self.driver.find_elements(By.XPATH,self.tableRows_xpath)

    def getColumns(self):
        return self.driver.find_elements(By.XPATH,self.tableColumns_xpath)

    def searchCustomerByEmail(self,email):
        flag=False

        for r in range(1,len(self.getRows())+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            emailId=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text()
            if emailId==email:
                flag=True
                break

        return flag

    def searchCustomerByName(self,name):
        flag=False
        for r in range(1,len(self.getRows())+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            nameId=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text()

            if name==nameId:
                flag=True
                break

        return flag

