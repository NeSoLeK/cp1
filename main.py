from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
driver = webdriver.Firefox()


driver.get("https://demo.opencart.com/")
sleep(3)
try:

    product_link = driver.find_element(By.CSS_SELECTOR, ".product-thumb")
    product_link.click()

    sleep(10)

    screenshots = driver.find_elements(By.CSS_SELECTOR,".img-thumbnail")
    for screenshot in screenshots:
        screenshot.click()
        close = driver.find_element(By.CSS_SELECTOR, ".mfp-close")
        close.click()


    sleep(10)

    currency_dropdown = driver.find_element(By.CSS_SELECTOR, "#form-currency")
    currency_dropdown.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'EUR'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'USD'))).click()


    pc_category_link = driver.find_element(By.CSS_SELECTOR, "#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(6) > a")
    pc_category_link.click()


    empty_page_message = driver.find_element(By.CSS_SELECTOR, ".alert.alert-info")
    if empty_page_message.is_displayed():
        print("Страница категории 'PC' пуста.")
    else:
        print("Страница категории 'PC' не пуста.")


    registration_link = driver.find_element(By.CSS_SELECTOR, "a[href='index.php?route=account/register']")
    registration_link.click()


    firstname_input = driver.find_element(By.ID, "input-firstname")
    firstname_input.send_keys("Ilya")

    lastname_input = driver.find_element(By.ID, "input-lastname")
    lastname_input.send_keys("Elistratov")

    email_input = driver.find_element(By.ID, "input-email")
    email_input.send_keys("elistratov.ilya@gmail.com")

    telephone_input = driver.find_element(By.ID, "input-telephone")
    telephone_input.send_keys("1234567890")

    address_input = driver.find_element(By.ID, "input-address-1")
    address_input.send_keys("123 Strit")

    city_input = driver.find_element(By.ID, "input-city")
    city_input.send_keys("Moscow")

    postcode_input = driver.find_element(By.ID, "input-postcode")
    postcode_input.send_keys("123007")

    country_input = driver.find_element(By.ID, "input-country")
    country_input.send_keys("Russia")

    region_input = driver.find_element(By.ID, "input-zone")
    region_input.send_keys("Moscow")


    register_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Continue']")
    register_button.click()

except Exception as e:
    print("Произошла ошибка:", e)

finally:

    driver.quit()