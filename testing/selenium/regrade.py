'''
   TESTING FILE FOR GUI
   -uses Selenium to test gui cases through our demos
'''

import unittest
import pytest
#import allure
import time
import os
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager 
 
 
unittest.TestLoader.sortTestMethodsUsing = None

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')

d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'browser':'ALL' } 
 
class ReGrade(unittest.TestCase):
    @classmethod
    def setUpClass(self):


        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options, desired_capabilities=d)
        self.JOB = os.environ['BUILD_DEFINITIONNAME']
        self.BUILD_NUMBER = os.environ['BUILD_BUILDNUMBER']
        self.SENSOR_IP = os.environ['SENSOR_IP']
        self.SENSOR_ID = os.environ['SENSOR_ID']
        self.CURTUI = os.environ['CURTUI']


        #self.JOB = os.environ['JOB_NAME']
        #self.BUILD_NUMBER = os.environ['BUILD_NUMBER']

        #with open("/var/jenkins_home/jobs/"+self.JOB+"/builds/"+self.BUILD_NUMBER+"/DEMO.txt") as file:
            #self.SENSOR_ID = file.read().replace('\n', '')

    '''
        Login for Curtail UI
    '''
    def test_a(self):
        '''       
        self.driver.get("https://curtui:4430/#/reports?sensor="+self.SENSOR_ID)

       # CHECK FOR EXISTANCE
        self.assertTrue(self.is_element_clickable(By.NAME, 'username'))
        self.assertTrue(self.is_element_clickable(By.NAME, 'password'))

        # Here we wait to be interactable and then proceed to login
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.NAME,'username'))).send_keys("admin")
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.NAME,'password'))).send_keys("Curtail")
 
        self.assertTrue(self.is_element_present(By.XPATH, "//*[contains(text(), 'Login')]"))
        elem = self.driver.find_elements_by_xpath("//*[contains(text(), 'Login')]")
        elem[1].click()

        time.sleep(5) #let page load
  
        result = self.are_elements_present(By.XPATH, 
                                             "//*[starts-with(@style,'fill: rgb(255, 255, 255); stroke: rgb(221, 4, 4);')]")
    
        if result:
            self.assertTrue(result)
            print("regrade.py says that there is nothing wrong, success")
        else:
            self.assertTrue(result)
            print("regrade.py says that there is something wrong, unstable")

        #self.assertTrue(self.are_elements_present(By.XPATH, 
                                             #"//*[starts-with(@style,'fill: rgb(255, 255, 255); stroke: rgb(221, 4, 4);')]"))
        ''' 

        try:
            self.driver.get("https://"+self.CURTUI+"/#/reports?sensor="+self.SENSOR_ID)
        except TimeoutException:
            self.driver.get("https://"+self.CURTUI+"/#/reports?sensor="+self.SENSOR_ID)


        time.sleep(5)
        # Here we wait to be interactable and then proceed to login
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.NAME,'username'))).send_keys("admin")
        except TimeoutException:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.NAME,'username'))).send_keys("admin")
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.NAME,'password'))).send_keys("Curtail")
        except TimeoutException:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.NAME,'username'))).send_keys("admin")

        self.assertTrue(self.is_element_present(By.XPATH, "//*[contains(text(), 'Login')]"))
        elem = self.driver.find_elements_by_xpath("//*[contains(text(), 'Login')]")
        elem[1].click()

        time.sleep(5) #let page load

        self.assertTrue(self.are_elements_present(By.XPATH,
                                             "//*[starts-with(@style,'fill: rgb(255, 255, 255); stroke: rgb(221, 4, 4);')]"))
        #self.assertTrue(len(node) == 0) #If there are nodes that are red we will return false and fail this case


    def is_element_clickable(self, how, what):
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((how,what)))
        except TimeoutException:
            return False
        except NoSuchElementException:
            return False
        return True

    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((how,what)))
        except TimeoutException:
            return False
        except NoSuchElementException:
            return False
        return True

    def are_elements_present(self, how, what):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((how,what)))
            #WebDriverWait(self.driver,30).until(EC.presence_of_all_elements_located((how,what)))
        except TimeoutException:
            return True 
            #return False
        except NoSuchElementException:
            return True 
            #return False
        return False 

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()



 
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('GhostDemo'))
    suite.addTest(WidgetTestCase('ReGrade'))
    return suite

if __name__ == "__main__":
    #runner = unittest.TextTestRunner()
    #runner.run(suite())
    unittest.main()

