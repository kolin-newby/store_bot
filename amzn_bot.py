import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager


def start_amzn_bot(item_url, trigger_price):

    load_dotenv()
    uname = os.environ['AMZN_USER']
    key = os.environ['AMZN_PASS']

    browser = webdriver.Chrome(ChromeDriverManager().install())

    browser.get(item_url)
    browser.find_element_by_id('nav-link-accountList').click()

    browser.find_element_by_id('ap_email').send_keys(uname)
    browser.find_element_by_id('continue').click()

    browser.find_element_by_id('ap_password').send_keys(key)
    browser.find_element_by_id('signInSubmit').click()

    try:
        browser.find_element_by_id('ap-account-fixup-phone-skip-link').click()
    except:
        pass
    finally:

        try:
            price = float((browser.find_element_by_id(
                'price_inside_buybox').text)[1:])
        except:
            try:
                price = float(
                    (browser.find_element_by_id('newBuyBoxPrice').text)[1:])
            except:
                print('*No price found*')
                browser.close()
                return (False, '0')
        finally:

            if price <= trigger_price:
                print(price)
                browser.find_element_by_id('add-to-cart-button').click()
                try:
                    browser.find_element_by_id('attachSiNoCoverage').click()
                except:
                    pass
                finally:
                    try:
                        browser.get(
                            'https://www.amazon.com/gp/buy/spc/handlers/display.html?hasWorkingJavascript=1')
                    except:
                        print('ERROR***No "Proceed to Checkout" button was found***')
                        browser.close()
                        return (False, '-1')
                    finally:
                        browser.find_element_by_xpath(
                            '//*[@id="submitOrderButtonId"]/span/input').click()
                        browser.close()
                        return (True, '0')
            else:
                print('*Price too high*')
                browser.close()
                return (False, '0')
