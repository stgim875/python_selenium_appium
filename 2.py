# Android environment
import unittest
import os
from appium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class VirnectonpremiseTest(unittest.TestCase):
    def setUp(self):

        # Virnect 영구형 remote App 경로
        app = os.path.join(os.path.dirname(
            __file__)), 'C:\python_selenium_appium\(staging)remote_mobile_2700005-release.apk'
        app = os.path.abspath(app)

        # Set up appium
        # Appium 서버의 포트는 4723으로 지정합니다.
        # 그리고 desired_capabilities에 연결하려는 디바이스(갤럭시 S22)의 정보를 넣습니다.
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'appiumdeviceName': 'R5CT333M03H',
                'platformName': 'Android',
                'platformVersion': '12',
                'automationName': 'Appium'
            })

    def test_search_field(self):
        driver = self.driver
        # selenium의 WebDriverWait을 사용합니다. element가 나올때 까지 최고 30초까지 기다립니다.
        time.sleep(30)

        # 버넥트 이용통게 정버 수집 모달이 출력
        # 모달에서 동의 버튼을 클릭
        agree = driver.find_element(By.ID, 'android:id/button1')
        agree.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(VirnectonpremiseTest)
    unittest.TextTestRunner(verbosity=2).run(suite)