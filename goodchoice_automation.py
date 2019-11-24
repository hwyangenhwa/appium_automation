#-*- coding:utf-8 -*-

import unittest
import os
from appium import webdriver
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Init_APP(unittest.TestCase):

    def setUp(self):
        # setup file path
        app = os.path.join(os.path.dirname(__file__), 'C:\\apk\\goodchoice.apk')
        app = os.path.abspath(app)

        # Set up appium
        self.driver         = webdriver.Remote(
            command_executor='http://127.0.0.1:4001/wd/hub',
            desired_capabilities={
                'platformName': 'Android',
                'platformVersion': '9.0',
                'deviceName': 'Nexus_6',
                'automationName': 'Appium',
                'appPackage': 'kr.goodchoice.abouthere',
                'appActivity': 'kr.goodchoice.abouthere.activity.SplashActivity'
            })

    def tearDown(self):
        self.driver.quit()

    def test_install(self):
        driver              = self.driver
        wait                = WebDriverWait(driver, 20)

        # Allow telBtn // Allow locBtn // moveBtn
        tel_AllowBtn        = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "com.android.packageinstaller:id/permission_allow_button")))
        tel_AllowBtn.click()

        loc_AllowBtn        = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "com.android.packageinstaller:id/permission_allow_button")))
        loc_AllowBtn.click()

        sleep(3)

        move_Img = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "kr.goodchoice.abouthere:id/container_")))
        move_Img.click()

        later_Btn           = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "kr.goodchoice.abouthere:id/later_")))
        later_Btn.click()

    def test_motel(self):
        self.test_install()

        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Select motel Btn
        motel_Btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "kr.goodchoice.abouthere:id/relat_item3")))
        motel_Btn.click()

    def test_motel_scroll(self):
        self.test_motel()

        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # area scrolling up & down
        for i in range(0, 2):
            sleep(3)
            action = TouchAction(self.driver)

            header_view = driver.find_element_by_id("kr.goodchoice.abouthere:id/recycler_view_group_")
            start_btn = header_view.find_element_by_xpath("//android.widget.FrameLayout[@index='0']")
            end_btn = header_view.find_element_by_xpath("//android.widget.FrameLayout[@index='8']")

        if (i == 0):
            self.driver.scroll(end_btn, start_btn)
        else:
            self.driver.scroll(start_btn, end_btn)

        # area_detail scrolling up & down
        for i in range(0, 2):
            sleep(3)
            action = TouchAction(self.driver)
            header_view = driver.find_element_by_id("kr.goodchoice.abouthere:id/recycler_view_child_")
            start_btn = header_view.find_element_by_xpath("//android.widget.FrameLayout[@index='0']")
            end_btn = header_view.find_element_by_xpath("//android.widget.FrameLayout[@index='8']")

            if (i == 0):
                self.driver.scroll(end_btn, start_btn)
            else:
                self.driver.scroll(start_btn, end_btn)

    def test_mt_detail(self):
        self.test_motel()

        driver              = self.driver
        wait                = WebDriverWait(driver, 20)

        # 지역
        header_area         = driver.find_element_by_id("kr.goodchoice.abouthere:id/recycler_view_group_")
        area                = header_area.find_element_by_xpath("//android.widget.FrameLayout[@index='1']").click()

        # 세부지역
        header_detail       = driver.find_element_by_id("kr.goodchoice.abouthere:id/recycler_view_child_")
        area_detail         = header_detail.find_element_by_xpath("//android.widget.FrameLayout[@index='1']").click()

    def test_mt_detailscroll(self):

    def test_mt_detailfilter(self):
        self.test_detail()

        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # discount filtering on
        discount_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='할인숙소']")))
        discount_btn.click()

        sleep(3)
        # discount filtering off
        discount_btn.click()

        # payback filtering on
        payback_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,"//android.widget.TextView[@text='페이백']")))
        payback_btn.click()

        sleep(3)
        # payback filtering off
        payback_btn.click()

        # rent filtering on
        rent_btn =  WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,"//android.widget.TextView[@text='대실예약']")))
        rent_btn.click()

        sleep(3)
        # rent filtering off
        rent_btn.click()

        # lodgment filtering on
        lodgment_btn =  WebDriverWait(driver, 5).until(
             EC.element_to_be_clickable((By.XPATH,"//android.widget.TextView[@text='숙박예약']")))

        sleep(3)
        # lodgment filtering off
        lodgment_btn.click()

if __name__ == '__main__':
    suite_1 = unittest.TestLoader().loadTestsFromTestCase(Init_APP)
    unittest.TextTestRunner(verbosity=2).run(suite_1)
