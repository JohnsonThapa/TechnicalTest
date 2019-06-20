from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, urllib, hashlib

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://images.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        # "Opening Browser"
        driver.get(self.base_url)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Sign out'])[1]/following::span[1]").click()
        driver.find_element_by_link_text("Upload an image").click()
        driver.find_element_by_id("qbfile").click()
        driver.find_element_by_id("qbfile").clear()
        # Uploading File
        driver.find_element_by_id("qbfile").send_keys("E:\\images\\test.jpeg")
        #Opening Third Image
        driver.find_element_by_id("dimg_5").click()
        driver.find_element_by_id("dr8RJsvHgKct-M:").click()
        #Taking screenshot as it is without cropping
        driver.get_screenshot_as_file('Last_visited_page.jpeg')
        

    #Validating images using hash values
    def hash_it(path):
        with open(path,'rb') as f:
            hasher = hashlib.md5()
            hasher.update(f.read())
            return hasher.hexidigest()
        
    directory = "E:/Image_comparision"
    downloaded_image = "{}/{}".format(directory,"downloaded.jpeg")
    local_image = "{}/{}".format(directory,"local.jpeg")
    image = chrome.find_element_by_xpath("//img[@alt='Test Logo']").get_attribute("src)

    urllib.request.urlretrieve(logo, downloaded_image)

    local_image_hash = hash_it(local_image)
    downloaded_image_hash = hash_it(downloaded_image)                                                                
    assert local_image_hash == downloaded_image_hash "Hashes do not match. {} vs {}".format(local_image_hash, downloaded_image_hash)                
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
