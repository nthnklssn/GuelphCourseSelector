from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time



class newDriver:
    def __init__(self):
        self.webdriver = webdriver.Firefox()

    def teardown(self):
        self.webdriver.close()

    '''
    Function to return to the course selection page.
    '''
    def goBacktoSelect(self):
        self.webdriver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/ul/li[2]").click()
        self.webdriver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/ul[1]/li[2]").click()

    '''
    Logins to the WebAdvisor website using username and password you provide.
    '''
    def login(self, username, password):
        self.webdriver.find_element_by_xpath("//*[@id='acctLogin']").click()
        time.sleep(3)
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

    '''
    Attempts to enroll in the course described by the course dictionary passed inself.
    Will return true if succesfully enrolled in the course
    '''
    def enrollInCourse(self, course):
        try:
            for i in range(30):
                element = self.webdriver.find_element_by_id("SEC_SHORT_TITLE_" + str(i+1))

                if course["code"] + "*" + course["section"] in element.get_attribute("innerHTML"):
                    if self.webdriver.find_element_by_id("LIST_VAR2_" + str(i+1)).get_attribute("innerHTML").lower() == "open":
                        print "Course not full, enrolled!"
                        self.webdriver.find_element_by_id("LIST_VAR1_" + str(i+1)).click()
                        #Uncomment the following line for functionality, I do not want to mess up courses while testing
                        #self.webdriver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[3]/form/div/input").click()
                        return True
                    else:
                        print "Could not enroll in the course at the time, trying later"
                        return False

        except NoSuchElementException:
            return False

    def enterTextValue(self, xpath, text):
        elem = self.webdriver.find_elements_by_xpath(xpath)[0]
        elem.send_keys(text)
        elem.send_keys(Keys.ENTER)

    def findSelectElement(self, xpath, text, number=0):
        if number == 0:
            for element in self.webdriver.find_elements_by_xpath(xpath):
                if text in element.text:
                    element.click()


    def loadWebPage(self, webpageString):
        self.webdriver.get(webpageString)
