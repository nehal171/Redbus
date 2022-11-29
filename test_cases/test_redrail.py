import datetime
import time
from library_.config import Config
from data.reading_objects import ReadExcel
from POM.redraill import Railway
import pytest

class TestRailwayPage:
    read_xl = ReadExcel()
    details = read_xl.read_test_data(Config.TRAIN_DATA_SHEET)
    @pytest.mark.parametrize('from_stn,to_stn,irctc_usr,name,age,email,phone_no,upi',details)
    def test_Railway(self,from_stn,to_stn,irctc_usr,name,age,email,phone_no,upi,_driver):
        _driver.implicitly_wait(50)
        try:
            rp1 = Railway(_driver)
            rp1.click_redrail()
            rp1.from_station(from_stn)
            rp1.f_stn()
            rp1.to_station(to_stn)
            rp1.t_stn()
            rp1.date_1()
            rp1.day_1()
            rp1.src_btn()
            rp1.trn_cls()
            rp1.click_go_btn()
            rp1.click_irctc_usr()
            rp1.enter_irctc_usr(irctc_usr)
            rp1.click_check_btn()
            rp1.click_add_psgr()
            rp1.enter_name(name)
            rp1.enter_age(age)
            rp1.click_gender()
            rp1.click_pref()
            rp1.click_meal_pref()
            rp1.click_add_passenger()
            rp1.enter_email(email)
            rp1.enter_ph_no(phone_no)
            rp1.click_prcd()
            rp1.click_upi()
            rp1.enter_upi(upi)
            rp1.click_verify()
        except BaseException as error_msg:
            td=datetime.datetime.now()
            name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
            _driver.save_screenshot(Config.SCREENSHOTS_PATH+name)
            raise error_msg

