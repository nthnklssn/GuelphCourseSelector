Automated Course Enroller For University Of Guelph.
This code was made by Nathan Klassen, UoG
Use this program at your own risk, as I am not responsible for any errors you make to your schedule.

Usernames and Passwords you enter in the program are in no way stored or sent back to me.

Requires Geckodriver, Selenium and python.

***********
USAGE
***********
This program will auto enroll you in up to 6 courses in a given semester.
You must enter your WebAdvisor username and password and then the details of the courses you are taking,
including section number.

The program will continuosly try and enroll you in the courses.

To run the program just type:

    python webadvisorScript.py in the terminal

Values such as username, passwords and course detailes can be hardcoded for speed/ testing.
Uncomment line 49 in the web_utils file for the program to be functional otherwise it is just for demo purposes.
***************
Code BreakDown
***************
The code is seperated into two sections, web_utils contains the utilities used for the script.
The code in web_utils could be re-used for more automation services on WebAdvisor.
Code located in webadvisorScript is just used to automate and enroll in the desired courses.


************
Dependancies
************

Must have Geckodriver, Python 2.7, Selenium and Firefox installed on your computer.
