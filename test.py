import unittest
from selenium import webdriver
import scaper 


class ScraperTest(unittest.TestCase):
    def setUp(self):
        PATH = "/Users/yamz/Desktop/chromedriver"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get('https://www.hsamuel.co.uk/webstore/l/mens-jewellery/')
    
    def test_cookies(self):
        self.driver.find_element_by_xpath('//*[@id="js-cookie-consent-overlay"]/div[1]/div/button[1]')
    
    def test_getting_product_information(self):
        self.scaper()
        time.sleep(5)

        actual = self.driver.current_url
        expected = 'https://www.hsamuel.co.uk/webstore/l/mens-jewellery/'
        self.assertEqual(actual, expected)
        


    def test(self):
        print("test")
        assert True

    def not_test(self):
        print('not working')

    def shutdown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()