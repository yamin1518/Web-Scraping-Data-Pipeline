import unittest
from selenium import webdriver
import page 


class ScraperTest(unittest.TestCase):
    def setUp(self):
        PATH = "/Users/yamz/Desktop/chromedriver"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get('https://www.hsamuel.co.uk/webstore/l/mens-jewellery/')
    
    def test(self):
        print("test")
        assert True

    def not_test(self):
        print('not working')

    def shutdown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()