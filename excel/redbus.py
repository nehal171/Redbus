from selenium import webdriver
import time
path = r"C:\Users\Nehal\Desktop\driverfiles\chromedriver.exe"
driver = webdriver.Chrome(path)
#opens the redbus website
driver.get("https://www.redbus.in/")
driver.maximize_window()
driver.implicitly_wait(30)
#click on redrail icon
driver.find_element("xpath",'//a[@class="site-links redRail"]').click()

#enter from station name
for char1 in "Delhi":
    driver.find_element('xpath','//label[text()="FROM STATION"]/..//input[@class="search-input"]').send_keys(char1)
time.sleep(2)
driver.find_element('xpath','//div[@class="solr_results_block"]/div/div[text()="New Delhi"]').click()

#enter to station name
for char2 in "Mumbai Central":
    driver.find_element('xpath','//label[text()="TO STATION"]/..//input[@class="search-input"]').send_keys(char2)
time.sleep(2)
driver.find_element('xpath', '//div[@class="solr_results_block"]/div/div[text()="Mumbai Central"]').click()
# driver.find_element('xpath', '//div[text()="BDTS"]').click()
time.sleep(2)
#click on date
driver.find_element("xpath",'//div[@class="home_date_wrap"]').click()
#select date
driver.find_element("xpath",'//span[text()="30"]').click()
#click on search button
driver.find_element('xpath','//button[@class="search-btn "]').click()
time.sleep(4)
#select desired train class
driver.find_element('xpath','//div[text()="3A"]').click()
time.sleep(1)
#click on go ahead button
driver.find_element('xpath','//div[@class="go_ahead_button"]').click()
time.sleep(1)
#click irctc username
driver.find_element('xpath','//input[@placeholder="IRCTC username"]').click()
#enter irctc username
driver.find_element('xpath','//div[@class="irctc_username_modal_wrap"]//input[@placeholder="IRCTC username"]').send_keys('Missi')
time.sleep(2)
#verify irctc username
driver.find_element('xpath','//div[@class="check_irctc_un"]').click()
time.sleep(3)
#click on add new passenger button
driver.find_element('xpath','//div[@class="add_new_passenger_button"]').click()
#enter passenger name
driver.find_element('xpath','//input[@placeholder="Name"]').send_keys('Rahul')
#enter passenger age
driver.find_element('xpath','//input[@placeholder="Age"]').send_keys('24')
#select gender of passenger
driver.find_element('xpath','//span[text()="Male"]').click()
#select berth preference
driver.find_element('xpath','//div[text()="Lower"]').click()
#select meal preference
# driver.find_element('xpath','//span[text()="Non-Veg"]/..//div[@class="radio_button_inner"]').click()
#click on add passenger button
driver.find_element('xpath','//div[@class="add_passenger_button"]').click()
#enter email id
driver.find_element('xpath','//input[@placeholder="Enter Email"]').send_keys('nehaljoshi080@gmail.com')
#enter phone no
driver.find_element('xpath','//input[@placeholder="Enter your phone no"]').send_keys('9769631257')
#click on proceed button
driver.find_element('xpath','//div[@class="proceed_button"]').click()
#click on add upi id
driver.find_element('xpath','//div[text()="Add a new UPI ID"]').click()
time.sleep(2)
#enter upi id
driver.find_element('xpath','//input[@class="input_upi"]').send_keys('9769631257@ybl')
#verify upi id
driver.find_element('xpath','//div[@class="eupi-verify"]').click()
time.sleep(3)
#close the browser
driver.close()
# # driver.find_element('xpath','//div[text()="PAY NOW"]]').click()