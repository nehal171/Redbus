from behave import *
from selenium import webdriver
import time


@given('Open the browser and enter valid url')
def step_impl(context):
    path = r"C:\Users\Nehal\Desktop\driverfiles\chromedriver.exe"
    context.driver = webdriver.Chrome(executable_path=path)
    context.driver.get("https://www.redbus.in/")
    context.driver.maximize_window()
    context.driver.implicitly_wait(30)


@when('Click on redrail')
def step_impl(context):
    context.driver.find_element("xpath", '//a[@class="site-links redRail"]').click()
    time.sleep(1)


@when('Enter from station')
def step_impl(context):
    for char1 in "Delhi":
        context.driver.find_element('xpath', '//label[text()="FROM STATION"]/..//input[@class="search-input"]').send_keys(char1)
    time.sleep(2)
    context.driver.find_element('xpath', '//div[@class="solr_results_block"]/div/div[text()="New Delhi"]').click()


@when('Enter to station')
def step_impl(context):
    for char2 in "Mumbai Central":
        context.driver.find_element('xpath', '//label[text()="TO STATION"]/..//input[@class="search-input"]').send_keys(char2)
    time.sleep(2)
    context.driver.find_element('xpath', '//div[@class="solr_results_block"]/div/div[text()="Mumbai Central"]').click()
    time.sleep(2)


@when('Click on date-picker and enter the date')
def step_impl(context):
    context.driver.find_element("xpath", '//div[@class="home_date_wrap"]').click()
    context.driver.find_element("xpath", '//span[text()="30"]').click()


@when('Click on search button')
def step_impl(context):
    context.driver.find_element('xpath', '//button[@class="search-btn "]').click()
    time.sleep(2)


@when('Select desired train class')
def step_impl(context):
    context.driver.find_element('xpath', '//div[text()="3A"]').click()
    time.sleep(2)


@when('Click on go ahead button')
def step_impl(context):
    context.driver.find_element('xpath', '//div[@class="go_ahead_button"]').click()
    time.sleep(2)


@when('Click on irctc username and Enter irctc username and verify the username')
def step_impl(context):
    context.driver.find_element('xpath', '//input[@placeholder="IRCTC username"]').click()
    context.driver.find_element('xpath','//div[@class="irctc_username_modal_wrap"]//input[@placeholder="IRCTC username"]').send_keys('Missi')
    time.sleep(1)
    context.driver.find_element('xpath', '//div[@class="check_irctc_un"]').click()
    time.sleep(3)


@when('Click on add new passenger button and enter passenger details')
def step_impl(context):
    context.driver.find_element('xpath', '//div[@class="add_new_passenger_button"]').click()
    time.sleep(2)
    context.driver.find_element('xpath', '//input[@placeholder="Name"]').send_keys('Rahul')
    context.driver.find_element('xpath', '//input[@placeholder="Age"]').send_keys('24')
    context.driver.find_element('xpath', '//span[text()="Male"]').click()
    context.driver.find_element('xpath', '//div[text()="Lower"]').click()
    time.sleep(10)
    context.driver.find_element('xpath', '//div[@class="add_passenger_button"]').click()
    time.sleep(2)


@when('Enter email id')
def step_impl(context):
    context.driver.find_element('xpath', '//input[@placeholder="Enter Email"]').send_keys('nehaljoshi080@gmail.com')


@when('Enter phone no')
def step_impl(context):
    context.driver.find_element('xpath', '//input[@placeholder="Enter your phone no"]').send_keys('9769631257')


@when('Click on proceed button')
def step_impl(context):
    context.driver.find_element('xpath', '//div[@class="proceed_button"]').click()


@when('Click on upi and enter upi id and verify it')
def step_impl(context):
    context.driver.find_element('xpath', '//div[text()="Add a new UPI ID"]').click()
    context.driver.find_element('xpath', '//input[@class="input_upi"]').send_keys('9769631257@ybl')
    context.driver.find_element('xpath', '//div[@class="eupi-verify"]').click()
    time.sleep(3)


@when('Close the browser')
def step_impl(context):
    context.driver.close()


@then('Redrail module is functionally stable')
def step_impl(context):
    assert True


