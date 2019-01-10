from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



class newDriver:
    def __init__(self):
        self.webdriver = webdriver.Firefox()

    def teardown(self):
        self.webdriver.close()

    def goBacktoSelect(self):
        self.webdriver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/ul/li[2]").click()
        self.webdriver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/ul[1]/li[2]").click()
    def search(self, searchTerm):
        elem = self.webdriver.find_element_by_xpath("//*[@id='lst-ib']")
        elem.click()
        elem.send_keys(searchTerm)
        elem.send_keys(Keys.ENTER)
        #print self.webdriver.find_elements_by_xpath("/html/body/div[6]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/div/h3/a")[0].text

    def login(self, username, password):
        self.webdriver.find_element_by_xpath("//*[@id='acctLogin']").click()
        time.sleep(1)
        elem = self.webdriver.find_element_by_xpath('//*[@id="USER_NAME"]')
        elem.click()
        elem.send_keys(username)
        elem = self.webdriver.find_element_by_xpath('//*[@id="CURR_PWD"]')
        elem.click()
        elem.send_keys(password)
        elem.send_keys(Keys.ENTER)
        time.sleep(2)
        self.webdriver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/ul/li[2]").click()
        self.webdriver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/ul[1]/li[2]").click()

    def enterTextValue(self, xpath, text):
        elem = self.webdriver.find_elements_by_xpath(xpath)[0]
        elem.send_keys(text)
        elem.send_keys(Keys.ENTER)

    def findSelectElement(self, xpath, text, number=0):
        if number == 0:
            for element in self.webdriver.find_elements_by_xpath(xpath):
                if text in element.text:
                    element.click()

    def findCheckElement(self, xpath, text):
        pass


    def loadWebPage(self, webpageString):
        self.webdriver.get(webpageString)
