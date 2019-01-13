from web_utils import newDriver
import time

'''
testDriver: webdriver element.
semester: value of w, s or f for which semester
course: dictionary containing details related to the course
'''
def searchforCourse(testDriver, semester, course):

    testDriver.findSelectElement('//*[@id="VAR1"]/option', term)
    testDriver.findSelectElement('//*[@id="LIST_VAR1_1"]/option', course["discipline"])
    testDriver.enterTextValue('//*[@id="LIST_VAR3_1"]', course["code"])
    testDriver.enterTextValue('//*[@id="LIST_VAR4_1"]', course["section"])
    testDriver.webdriver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[3]/form/div/input").click()
    time.sleep(2)
    return testDriver.enrollInCourse(course)

num_courses = 0
courseDict = {}
courses = []
testDriver = newDriver()

testDriver.loadWebPage("https://webadvisor.uoguelph.ca/WebAdvisor/WebAdvisor?TYPE=M&PID=CORE-WBMAIN&TOKENIDX=8290532176")
time.sleep(5)
testDriver.login(raw_input("Enter Login: "), raw_input("Enter Password: "))
#Uncomment lines 29-31 if you wish to hard code values for easier login
#username = "temp"
#password = "temp"
#testDriver.login(username, password)
while( num_courses > 6) or (num_courses < 1):
    num_courses = input("Enter number of courses you are searching for: ")
term = raw_input("Enter (F)all, (W)inter or (S)ummer: ").upper()
for i in range(num_courses):
    print "Course " + str(i + 1) + " :"

    courseDict["discipline"] = raw_input("Enter 2-4 letter discipline code Example: 'ENGG', 'HK', 'CIS': ").upper()
    courseDict["code"] = raw_input("Enter 4 number course code Example: '1500' '2120': ")
    courseDict["section"] = raw_input("Enter section number Example: '0101': ")
    courses.append(courseDict.copy())

while courses:
    for course in courses:
        if searchforCourse(testDriver, term, course):
            courses.remove(course)
        time.sleep(10)
        testDriver.goBacktoSelect()



testDriver.teardown()
