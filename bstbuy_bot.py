import os
from time import sleep
from dotenv import load_dotenv, main
from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager


def main():
    load_dotenv()
    uname = os.environ['BSTBUY_USER']
    key = os.environ['BSTBUY_PASS']

    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(
        'https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6432400.p?skuId=6432400')

    price = float((browser.find_element_by_xpath(
        '/html/body/div[3]/main/div[2]/div/div[1]/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div/div[2]/div/div[1]/div/span[1]').text)[1:])

    print(price)

    # browser.find_element_by_xpath(
    #     '//*[@id="fulfillment-add-to-cart-button-67194041"]/div/div/div/button').click()

    sleep(3000)
    browser.close()


if __name__ == '__main__':
    main()
