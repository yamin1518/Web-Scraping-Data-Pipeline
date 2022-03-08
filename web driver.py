#%% 
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By 
import requests
import time
import os
import uuid
import json
"""
List of things that I have tried to  implement

1) accept cookies 
2) navigate through the website
3) get the product name, price, sku 
4) set the sku number as the unique id using uuid4
5) download the images and the store them in a file
6) store the information in a JSON file
7) Added all the relevant Docstring (Please let me know on any improvements i sshould make on my doctstring)

I am having some issues with steps 4-6
started testing not sure if i am doing it right

"""

#%% 
#get data


class Scraper:

    """This class will runn all the functions that is needed for the Scraper to work

        Args:
            It only takes int he self argument

        Returns:
            All of the functions that is needed to make the Scraper work
    """
    def __init__(self):
        """This will initialise the class and it will load up the webpage

            Args:
                 Takes in the self argument

            Returns:
                It will load up the page and then return the product details
        """
        PATH = "/Users/yamz/Desktop/chromedriver"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get('https://www.hsamuel.co.uk/webstore/l/mens-jewellery/')
        self.get_product_details()


    def cookies(self):
        """This function will accept any cookies one the page

            Args:
                 Takes in the self argument

            Returns:
                It will load up the page and then accept any cookies
        """
        time.sleep(2) 
        accept_cookies_button = self.driver.find_element_by_xpath('//*[@id="js-cookie-consent-overlay"]/div[1]/div/button[1]')
        accept_cookies_button.click()

    
    def get_info(self):
        """This will gett he product information 

            Args:
                 Takes in the self argument

            Returns:
                It will use the _get_products function
        """
        self._get_products()

    def _get_products(self):
        """This will look at the website nad look for ht products

            Args:
                 Takes in the self argument

            Returns:
                It will load up the page and then look for the products and the details required
        """
        product_infos = self.driver.find_elements(By.XPATH, '//*[@id="access-content"]/div[1]/div/div[4]/div[2]/div/div[1]/div[2]/a[1]')
        for product_info in product_infos:
            product = self._get_product_info(product_info)
            print(product)
            break

    def _get_product_info(self, product_info):
        """This will get all the relevant information needed for the producst such as the name, price, sku and image

            Args:
                 Takes in the self argument
                 produc_info : str
                               Get the relevant product information

            Returns:
                It will return allt he relevant information about the product that is required
        """
        product = {}

        name = product_info.find_element(By.XPATH, '//*[@id="access-content"]/div[1]/div/div[4]/div[2]/div/div[1]/div[2]/a[2]/div/span[1]')
        print(name.text)
        product['name'] = name


        price = product_info.find_element(By.XPATH, '//*[@id="access-content"]/div[1]/div/div[4]/div[2]/div/div[1]/div[2]/a[2]/div/span[1]')
        print(price.text)
        product['price'] = price

        sku = product_info.find_element(By.XPATH, '//*[@id="access-content"]/div[1]/div/div[4]/div[2]/div/div[1]/div[2]/div[1]/a/div/a/picture/img')
        print(sku.text)
        product['sku'] = sku 


        img = product_info.find_element(By.XPATH , '//*[@id="access-content"]/div[1]/div/div[4]/div[2]/div/div[1]/div[2]/div[1]/a/div/a/picture/img')
        src = img.get_attribute('src')
        product_link = src.strip('https://www.hsamuel.co.uk/webstore/').split('/')[2]
        product_folder = f'images{product_link}'
        if os.path.isdir(product_folder):
            pass
        else: 
            os.makedirs(product_folder)
            
        self.get_image(src, f'{product_folder}/0.jpg')

        product['img_src'] = src
        return product

    def create_dictionary(self, get_info):

        #I tried to use the product informationt hat i created beofre to gett he name, price, sku and image and tried to pass it intot his function

        #I then tried to put these information into a JSON file with the SKU have a unique ID
        product_dictionary =  {}

        product_dictonary.update(
            {
                "product_name": name, 
                "sku": str(uuid.uuid4()), 
                "price": price,
                "image": image

            })
        return product_dictionary

    def save_product_dictionary(self, product_dictionary):
        with open("", 'w') as outfile:
            json.dump(f"product_{SKU}", outfile)
            
    @staticmethod
    def get_image(url, path):
        """This will download the images for the product

            Args:
                 Takes in the self argument
                 path : str
                        Gets the path of the folder

            Returns:
                It Will save the image in the desired folder
        """
        img_data = requests.get(url).content
        with open (path, 'wb') as handler : 
            handler.write(img_data)


    def navigate_website():

        nav_bar = driver.find_elements_by_xpath("//ul[@id='js-main-nav-container']//a")

        category_list = []

        for link in nav_bar:
            category_list.append(link.get_attribute("href"))

        def search_specific_category(search_term):
            
            for idx, search_term in category_list:
                if search_term in category_list:
                    link = category_list[idx]
                    driver.get(link)
            return


# %%
if __name__ == '__main__':
    scraper = Scraper()
    Scraper.cookies
    Scraper.get_image
    Scraper.get_info
    
import pandas as pd 
pd.DataFrame(product_dictionary)