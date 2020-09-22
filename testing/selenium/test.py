'''
   TESTING FILE FOR GUI
   -uses Selenium to test gui cases through our demos
'''

import unittest
import pytest
#import allure
import time
import requests
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
 
class GhostDemo(unittest.TestCase):
    @classmethod
    def setUpClass(self):

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options, desired_capabilities=d)
        self.JOB = os.environ['BUILD_DEFINITIONNAME']
        self.BUILD_NUMBER = os.environ['BUILD_BUILDNUMBER']
        self.SENSOR_IP = os.environ['SENSOR_IP']


    '''
        Login username 
    '''
    #@allure.step("Username")
    def test_a_login_username(self):

        try:
            self.driver.get("http://"+self.SENSOR_IP+":80/ghost/")
        except TimeoutException:
            self.driver.get("http://"+self.SENSOR_IP+":80/ghost/")

        time.sleep(5) 

        try:
            WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.NAME,'identification'))).send_keys("tking@curtail.com")
        except TimeoutException:
            WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.NAME,'identification'))).send_keys("tking@curtail.com")

        self.assertTrue(self.is_element_present(By.NAME, 'identification'))


    '''
        Login password 
    '''
    #@allure.step("Password")
    def test_b_login_password(self):

        self.assertTrue(self.is_element_present(By.NAME, 'password'))
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.NAME,'password'))).send_keys('HS,d1^SF":ot')


    '''
        Login click
    '''
    #@allure.step("Login Click")
    def test_c_login_click(self):

        self.assertTrue(self.is_element_clickable(By.ID, 'ember484'))

        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,'ember484'))).click()
        time.sleep(2) # let web page load

    '''
        Page scroll 
    '''
    #@allure.step("Page scroll")
    def test_d_page_scroll(self):

        try:
            node = WebDriverWait(self.driver,30).until(EC.presence_of_all_elements_located((By.XPATH,
                                             "//*[starts-with(@class,'gh-posts-list-item ember-view')]")))
        except TimeoutException:
            node = WebDriverWait(self.driver,30).until(EC.presence_of_all_elements_located((By.XPATH,
                                             "//*[starts-with(@class,'gh-posts-list-item ember-view')]")))

        for n in node:
            print(n.text)
            actions = ActionChains(self.driver)
            actions.move_to_element(n).perform()
        
        time.sleep(1)

        self.driver.find_element_by_tag_name('body').click()
        self.driver.find_element_by_tag_name('body').send_keys(Keys.END)


    '''
    
       Activates Ghost webpage, prompting taffic to sensor
    
    def activate_ghost(self):

        driver2 = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options, desired_capabilities=d)
        driver2.get("http://curt_"+self.JOB+self.BUILD_NUMBER+":80/ghost/")
        #driver2.get("http://curtail:80/ghost/")
        #driver2.get("http://127.0.0.1:10080/ghost/")
        #driver2.get("http://127.0.0.1:2369/ghost/")

        WebDriverWait(driver2,10).until(EC.element_to_be_clickable((By.NAME,'identification'))).send_keys("tking@curtail.com")
        WebDriverWait(driver2,10).until(EC.element_to_be_clickable((By.NAME,'password'))).send_keys('HS,d1^SF":ot')
        WebDriverWait(driver2,10).until(EC.element_to_be_clickable((By.ID,'ember484'))).click()

        time.sleep(2)
        WebDriverWait(driver2,10).until(EC.element_to_be_clickable((By.TAG_NAME,'body'))).click()
        WebDriverWait(driver2,10).until(EC.element_to_be_clickable((By.TAG_NAME,'body'))).send_keys(Keys.END)
        time.sleep(.5)
        WebDriverWait(driver2,10).until(EC.element_to_be_clickable((By.TAG_NAME,'body'))).click()
        WebDriverWait(driver2,10).until(EC.element_to_be_clickable((By.TAG_NAME,'body'))).send_keys(Keys.END)
        time.sleep(.5)
        WebDriverWait(driver2,10).until(EC.element_to_be_clickable((By.TAG_NAME,'body'))).click()
        WebDriverWait(driver2,10).until(EC.element_to_be_clickable((By.TAG_NAME,'body'))).send_keys(Keys.END)

        #driver2.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(.5)
        #driver2.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #time.sleep(2)

        driver2.close()
        driver2.quit() 
    '''
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
        #self.display.stop()

class ReGrade(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options, desired_capabilities=d)
        self.JOB = os.environ['BUILD_DEFINITIONNAME']
        self.BUILD_NUMBER = os.environ['BUILD_BUILDNUMBER']
        self.SENSOR_IP = os.environ['SENSOR_IP']
        self.SENSOR_ID = os.environ['SENSOR_ID']
        self.CURTUI = os.environ['CURTUI']


        #self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options, desired_capabilities=d)
        #self.JOB = os.environ['JOB_NAME']
        #self.BUILD_NUMBER = os.environ['BUILD_NUMBER']

        #with open("/var/jenkins_home/jobs/"+self.JOB+"/builds/"+self.BUILD_NUMBER+"/DEMO.txt") as file:
            #self.SENSOR_ID = file.read().replace('\n', '')

    '''
        Login for Curtail UI
    '''
    #def test_a(self):
    def test_regrade(self):
       
        self.updateKnownAlerts()
        #self.driver.get("https://curtui:4430/#/reports?sensor="+self.SENSOR_ID)
        try:
            self.driver.get("https://"+self.CURTUI+"/#/reports?sensor="+self.SENSOR_ID)
        except TimeoutException:
            self.driver.get("https://"+self.CURTUI+"/#/reports?sensor="+self.SENSOR_ID)


       # CHECK FOR EXISTANCE
        #self.assertTrue(self.is_element_clickable(By.NAME, 'username'))
        #self.assertTrue(self.is_element_clickable(By.NAME, 'password'))
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

    def updateKnownAlerts(self, cert=False):
    #def udpdateKnownAlerts(sensorID, curtui, cert=False):

        url = 'https://'+self.CURTUI+'/api/update-known-all?setname=default&sensorID='+self.SENSOR_ID
        #url = f'https://{self.CURTUI}/api/update-known-all?setname=default&sensorID={self.SENSOR_ID}'

        request = requests.Session()
        request.auth = ('admin', 'Curtail')

        if cert:
            request.post(url, verify="certfile")
        else:
            request.post(url, verify=False)

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
    runner = unittest.TextTestRunner()
    runner.run(suite())
    #unittest.main()

