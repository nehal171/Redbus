from data.reading_objects import ReadExcel
from selenium import webdriver
from library_.config import Config
import time

read_xl = ReadExcel()
railway_obj = read_xl.read_locators(Config.TRAIN_LOCATORS_SHEET)
print(railway_obj)

class Railway:
    def __init__(self,driver_1):
        self.driver_1 = driver_1

    def click_redrail(self):
        self.driver_1.find_element(*railway_obj["red_rail"]).click()

    def from_station(self,from_stn):
        for char in from_stn:
            self.driver_1.find_element(*railway_obj["from_place"]).send_keys(char)

    def f_stn(self):
        self.driver_1.find_element(*railway_obj["f_place"]).click()

    def to_station(self,to_stn):
        for char in to_stn:
            self.driver_1.find_element(*railway_obj["to_place"]).send_keys(char)

    def t_stn(self):
        self.driver_1.find_element(*railway_obj["t_place"]).click()
        time.sleep(3)


    def date_1(self):
        self.driver_1.find_element(*railway_obj["date"]).click()

    def day_1(self):
        self.driver_1.find_element(*railway_obj["day"]).click()

    def src_btn(self):
        self.driver_1.find_element(*railway_obj["search_trains"]).click()
        time.sleep(1)

    def trn_cls(self):
        self.driver_1.find_element(*railway_obj["tran_class"]).click()

    def click_go_btn(self):
        self.driver_1.find_element(*railway_obj["go_ahead"]).click()

    def click_irctc_usr(self):
        self.driver_1.find_element(*railway_obj["irctc_username"]).click()
        time.sleep(1)

    def enter_irctc_usr(self,irctc_usr):
        self.driver_1.find_element(*railway_obj["enter_irctc_user"]).send_keys(irctc_usr)
        time.sleep(2)

    def click_check_btn(self):
        self.driver_1.find_element(*railway_obj["check_button"]).click()
        time.sleep(4)

    def click_add_psgr(self):
        self.driver_1.find_element(*railway_obj["add_passenger"]).click()

    def enter_name(self,name):
        self.driver_1.find_element(*railway_obj["name_"]).send_keys(name)
        time.sleep(1)

    def enter_age(self,age):
        self.driver_1.find_element(*railway_obj["age_"]).send_keys(age)
        time.sleep(1)

    def click_gender(self):
        self.driver_1.find_element(*railway_obj["gender_"]).click()
        time.sleep(1)

    def click_pref(self):
        self.driver_1.find_element(*railway_obj["pref_"]).click()
        time.sleep(1)

    def click_meal_pref(self):
        self.driver_1.find_element(*railway_obj["meal_pref_"]).click()
        time.sleep(1)

    def click_add_passenger(self):
        self.driver_1.find_element(*railway_obj["add_psngr_"]).click()
        time.sleep(2)

    def enter_email(self,email):
        self.driver_1.find_element(*railway_obj["email_"]).send_keys(email)
        time.sleep(1)

    def enter_ph_no(self,phone_no):
        self.driver_1.find_element(*railway_obj["phone_number_"]).send_keys(phone_no)
        time.sleep(2)

    def click_prcd(self):
        self.driver_1.find_element(*railway_obj["proceed_"]).click()

    def click_upi(self):
        self.driver_1.find_element(*railway_obj["upi_"]).click()
        time.sleep(1)

    def enter_upi(self,upi):
        self.driver_1.find_element(*railway_obj["provide_upi"]).send_keys(upi)
        time.sleep(1)

    def click_verify(self):
        self.driver_1.find_element(*railway_obj["verify_"]).click()
        time.sleep(3)

