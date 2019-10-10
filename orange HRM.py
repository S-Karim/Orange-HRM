import unittest
from selenium import webdriver
import HtmlTestRunner
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/admin4/Desktop/chromedriverforselenium/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_loginIn(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        links = self.driver.find_elements_by_tag_name("a")
        print("Number of links present: ", len(links))
        self.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
        self.driver.find_element_by_xpath("//input[@id='btnLogin']").click()
        links = self.driver.find_elements_by_tag_name("a")
        print("Number of links present: ", len(links))
        self.assertEqual(len(links), 90)
        self.driver.implicitly_wait(5)
        self.driver.get_screenshot_as_file("C:/Users/admin4/Desktop/report.png")
        self.driver.implicitly_wait(5)

    def test_logout(self):
        self.driver.find_element_by_xpath("//a[@id='welcome']").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
        links = self.driver.find_elements_by_tag_name("a")
        print("Number of links present: ", len(links))
        self.assertEqual(len(links), 6)

        self.driver.close()
    @classmethod
    def teardownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HtmlTestRunner(output="Users/admin4/Desktop/report"),verbosity=2)

