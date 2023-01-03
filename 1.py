# from lib2to3.pgen2 import driver
# from typing_extensions import Self
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from pyautogui import click
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
# 신규 추가건
from pywinauto.application import Application
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from appium import webdriver
# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
# 신규 추가건
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.actions.action_builder import KeyInput
from selenium.webdriver.common.actions.action_builder import PointerActions
from selenium.webdriver.common.actions.action_builder import PointerInput
# Screenshot
# from Screenshot import Screenshot_Clipping
from selenium.webdriver.common.actions.mouse_button import MouseButton

import uiautomation as auto
import time
import os
import pywinauto

# options = UiAutomator2Options()
# options.deviceName = 'R5CT333M03H'
# options.platformName = 'Android'
# options.platformVersion = '12'
# options.deviceName = 'Galaxy 22'
# options.app = ('C:\python_selenium_appium\(staging)remote_mobile_2700005-release.apk')
# options.automationName = 'Appium'
# options.newCommandTimeout = 3000

# Appium1 points to http://127.0.0.1:4723/wd/hub by default
# driver = webdriver.Remote(
#     "http://127.0.0.1:4723/wd/hub", options=options)

desired_caps = UiAutomator2Options()
desired_caps = {
    "appium:deviceName": "R5CT333M03H",
    "platformName": "Android",
    "appium:platformVersion": "12",
    "appium:automationName": "Appium",
    "deviceName": "Galaxy S22",
    "appium:app": "C:\python_selenium_appium\(staging)remote_mobile_2700005-release.apk",
    "newCommandTimeout": 3000
}

driver = webdriver.Remote(
    "http://127.0.0.1:4723/wd/hub", desired_caps)

# Remote 앱 첫 화면 출력을 위한 암묵적 3초 대기
driver.implicitly_wait(time_to_wait=3)

# 이용 통계 다이얼 로그창 출력 여부 확인
if driver.find_element(By.ID, "com.virnect.remote.mobile2.staging:id/parentPanel").is_displayed():
    print("이용 통계 다이얼 로그창이 정상적으로 출력되었습니다.")
else:
    print("이용 통계 다이얼 로그창이 출력되지 않았습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 이용 통계 수집 동의 버튼 선택
usage = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((AppiumBy.ID, "android:id/button1")))
actions = ActionChains(driver)\
    .move_to_element(usage)\
    .click(usage)\
    .perform()
print("이용 통계 및 수집 동의 버튼을 선택했습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 접근 권한 허용 다이얼 로그창 출력 여부 확인
if driver.find_element(AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/mobile_permission_fragment").is_displayed():
    print("접근 권한 다이얼 로그창이 정상적으로 출력되었습니다.")
else:
    print("접근 권한 다이얼 로그창이 출력되지 않았습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 접근 권한 허용 확인 버튼 선택
access = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/permission_btn_confirm")))
actions = ActionChains(driver)\
    .move_to_element(access)\
    .click(access)\
    .perform()
print("접근 권한 허용 확인 버튼을 선택했습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 동영상 녹화 허용 다이얼 로그창 출력 여부 확인
if driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/grant_dialog").is_displayed():
    print("동영상 녹화 다이얼 로그창이 정상적으로 출력되었습니다.")
else:
    print("동영상 녹화 다이얼 로그창이 출력되지 않았습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 동영상 녹화 허용 여부 선택
# 앱 사용 중에만 허용으로 선택
videobtn = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")))
actions = ActionChains(driver)\
    .move_to_element(videobtn)\
    .click(videobtn)\
    .perform()
print("동영상 녹화 허용으로 선택했습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 오디오 녹음 혀용 다이얼 로그창 출력 여부 확인
if driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/grant_dialog").is_displayed():
    print("오디오 녹음 허용 다이얼 로그창이 정상적으로 출력되었습니다.")
else:
    print("오디오 녹음 다이얼 로그창이 출력되지 않았습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 오디오 녹음 허용 여부 선택
# 앱 사용 중에만 허용으로 선택
audiobtn = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")))
actions = ActionChains(driver)\
    .move_to_element(audiobtn)\
    .click(audiobtn)\
    .perform()
print("오디오 녹음 허용으로 선택했습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# STG VIRNECT Remote에서 근처 기기를 찾을 수 있도록 상대적 위치 파악 허용 다이얼 로그창 출력 여부 확인
if driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/grant_dialog").is_displayed():
    print("STG VIRNECT Remote에서 상대적 위치 파악 허용 다이얼 로그창이 정상적으로 출력되었습니다.")
else:
    print("STG VIRNECT Remote에서 상대적 위치 파악 허용 다이얼 로그창이 출력되지 않았습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# STG VIRNECT Remote에서 근처 기기를 찾을 수 있도록 상대적 위치 파악 허용
# 허용 버튼 선택
permitbtn1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")))
actions = ActionChains(driver)\
    .move_to_element(permitbtn1)\
    .click(permitbtn1)\
    .perform()
print("STG VIRNECT Remote에서 기기를 찾을 수 있게 허용으로 선택했습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# STG VIRNECT Remote에서 기기의 사진 및 미디어 액세스 허용 다이얼 로그창 출력 여부 확인
if driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/grant_dialog").is_displayed():
    print("STG VIRNECT Remote에서 기기의 사진 및 미디어 액세스 허용 다이얼 로그창이 정상적으로 출력되었습니다.")
else:
    print("기기의 사진 및 미디어 액세스 허용 다이얼 로그창이 출력되지 않았습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# STG VIRNECT Remote에서 기기의 사진 및 미디어 액세스 허용
# 허용 버튼 선택
permitbtn2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")))
actions = ActionChains(driver)\
    .move_to_element(permitbtn2)\
    .click(permitbtn2)\
    .perform()
print("STG VIRNECT Remote에서 기기의 사진 및 미디어 액세스를 허용으로 선택했습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 서버 설정 뷰 출력 여부 확인
if driver.find_element(AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/recycler_view").is_displayed():
    print("서버 설정 뷰가 정상적으로 출력되었습니다.")
else:
    print("서버 설정 뷰가 출력되지 않았습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 서버 설정 알림창에서 서버 선택
# 한국(remote.virnect.com) 선택
viewgroupkor = driver.find_element(
    AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/rc_item_tv_title")
actions = ActionChains(driver)\
    .move_to_element(viewgroupkor)\
    .click(viewgroupkor)\
    .perform()
print("서버 설정 알림창에서 한국 서버를 선택했습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# email account 입력
email_input = driver.find_element(
    AppiumBy.CLASS_NAME, "android.widget.AutoCompleteTextView")
email_input.send_keys('stgim875@gmail.com')
print("이메일 계정이 입력되었습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# password account 입력
password_input = driver.find_element(
    AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/login_input_et_pwd")
password_input.send_keys('@rokmc875th')
print("비밀번호가 입력되었습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# show password 입력 계정 보기 버튼 선택
show_passwordbtn = driver.find_element(
    AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Show password"]')
actions = ActionChains(driver)\
    .move_to_element(show_passwordbtn)\
    .click(show_passwordbtn)\
    .perform()
print("show password 메뉴를 선택했습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 로그인 버튼 선택
loginbtn = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/login_btn_login")))
actions = ActionChains(driver)\
    .move_to_element(loginbtn)\
    .click(loginbtn)\
    .perform()
print("로그인 버튼을 선택했습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 워크스테이션 선택 뷰 알림창 여부 확인
if driver.find_element(AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/recycler_view").is_displayed():
    print("워크스페이스 선택 뷰 알림창이 정상적으로 출력되었습니다.")
else:
    print("워크스페이스 선택 뷰 알림창이 출력되지 않았습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 워크스페이션 선택
# 김성태 선택
workspace_title = driver.find_element(
    AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/rc_item_tv_title")
actions = ActionChains(driver)\
    .move_to_element(workspace_title)\
    .click(workspace_title)\
    .perform()
print("워크스페이스를 선택했습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 원격 협업 리스트에서 새로고침 동작(pull 동작)
# user_actions = TouchAction(driver)
# user_actions.press(x=536, y=801)
# user_actions.move_to(x=526, y=1492)
# user_actions.release()
# user_actions.perform()

# 원격 협업 리스트에서 새로고침 동작(pull 동작)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(
    driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(506, 838)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(506, 1245)
actions.w3c_actions.pointer_action.release()
actions.perform()

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 진행중인 인수 테스트 원격 협업 출력 여부 확인
if driver.find_element(
    AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup"
).is_displayed():
    print("진행중인 인수 테스트 원격 협업 리스트가 출력되었습니다.")
else:
    print("진행중인 인수 테스트 원격 협업 리스트가 출력되지 않았습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 진행중인 인수 테스트 원격 협업 선택
Imageview = driver.find_element(
    AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/rc_item_iv_room_profile")
actions = ActionChains(driver)\
    .move_to_element(Imageview)\
    .click(Imageview)\
    .perform()
print("진행중인 원격협업을 선택했습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 인수 테스트 원격 협업 참가 모달창 출력 여부 확인
if driver.find_element(
    AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup"
).is_displayed():
    print("인수 테스트 원격 협업 참가 모달창이 출력되었습니다.")
else:
    print("인수 테스트 원격 협업 참가 모달창이 출력되지 않았습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 인수 테스트 원격 협업 선택
Participate = driver.find_element(
    AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/cl_detail_wrapper")
actions = ActionChains(driver)\
    .move_to_element(Participate)\
    .click(Participate)\
    .perform()
print("인수 테스트 원격 협업을 선택했습니다.")

# 웹에서 포인팅 동작을 확인하기 때문에 실시간 화면에서 60초 대기
# 모든 컬러 포인팅이 웹에서 구현된 것이 아니기 때문에 타임 변경 될 수 있음
# 90초 타임 슬립
time.sleep(90)

# 협업 보드 탭 선택
collaboration = driver.find_element(
    AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/tv_collaboration_board")
actions = ActionChains(driver)\
    .move_to_element(collaboration)\
    .click(collaboration)\
    .perform()
print("협업 보드탭을 선택하였습니다.")

# 협업 보드 > 캔버스에 이미지 업로드 > 이미지 공유 > 그리기 모드로 점찍기 동작 > 캔버스에 텍스트 입력하기 텍스트 모드 입력까지 135초 대기
# 협업 보드에 있는 모든 메뉴에 대한 동작이 구현된 것이 아니기 때문에 타임 변경 될 수 있음
# 130초 타임 슬립
time.sleep(135)

# web에서 AR 기능 탭 선택하면 Remote 녹화 or 전송 여부 모달창 출력 여부 확인하기
if driver.find_element(AppiumBy.ID, "android:id/parentPanel").is_displayed():
    print("STG VIRNECT Remote으로 녹화 또는 전송 시작 모달창이 출력되었습니다.")
else:
    print("STG VIRNECT Remote으로 녹화 또는 전송 시작 모달창이 출력되지 않았습니다.")

# web에서 AR 기능 탭 선택하면 Remote 녹화 or 전송 여부 모달창에서 [시작하기] 선택
remote_recording = driver.find_element(AppiumBy.ID, "android:id/button1")
actions = ActionChains(driver)\
    .move_to_element(remote_recording)\
    .click(remote_recording)\
    .perform()
print("시작하기 버튼을 선택하였습니다.")

# 160초 타입 슬립
time.sleep(160)

# 웹에 공유된 3D콘텐츠 터치하여 이동하기
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(
    driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(514, 1543)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(374, 1389)
actions.w3c_actions.pointer_action.release()
actions.perform()

# 다시 원위치로 3D콘텐츠 이동하기
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(
    driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(350, 1231)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(449, 1365)
actions.w3c_actions.pointer_action.release()
actions.perform()

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 콘텐츠 제어 권한 요청 팝업 수락하기

# 웹에서 콘텐츠 제어권 요청 후, 제어하는 동작하는 동안 대기
# 300초 타임 슬립
time.sleep(300)
