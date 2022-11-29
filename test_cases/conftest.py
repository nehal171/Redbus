from selenium import webdriver
import time
import pytest
from library_.config import Config

@pytest.fixture(params=["Chrome","Edge"])
def _driver(request):  #when we want to run this on different platforms then only request parameter should be used
    if request.param == "Chrome":
        driver_1 = webdriver.Chrome(executable_path=Config.Chrome_Driver_Path)
        time.sleep(1)

    elif request.param == "Edge":
        driver_1 = webdriver.Edge(executable_path=Config.EdgePath_Driver_Path)
        time.sleep(1)

    # elif request.param == "Firefox":
    #     driver_1 = webdriver.Firefox(executable_path=Config.FireFox_Driver_Path)
    #     time.sleep(1)
    #     driver = webdriver.Firefox(GeckoDriverManager().install())
    #     options = Options()
    #     options.binary_location=r""
    #     driver = webdriver.Firefox(executable_path=Config.FireFox_Driver_Path,options=options)
    #     driver = webdriver.Firefox(GeckoDriverManager().install())


    driver_1.get(Config.URL)
    time.sleep(2)
    driver_1.maximize_window()
    yield driver_1
    print(driver_1.title)
    # time.sleep(2)
    # driver.save_screenshot("test_loginpage.png")
    driver_1.close()