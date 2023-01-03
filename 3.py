# from lib2to3.pgen2 import driver
# from typing_extensions import Self
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from pyautogui import click
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

# 모바일 앱에서 멤버 탭 선택
member_tab = driver.find_element(AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/home_iv_member")
actions = ActionChains(driver)\
    .move_to_element(member_tab)\
    .click(member_tab)\
    .perform()
print("멤버탭을 선택하였습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 원격협업 멤버를 선택
# Master maxgim875@gmail.com을 선택
member_item = driver.find_element(
    AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ImageView[1]")
actions = ActionChains(driver)\
    .move_to_element(member_item)\
    .click(member_item)\
    .perform()

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 원격협업 버튼 선택
remote_create_btn = driver.find_element(
    AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/member_iv_btn_join_room")
actions = ActionChains(driver)\
    .move_to_element(remote_create_btn)\
    .click(remote_create_btn)\
    .perform()

# 5초 슬립 타임: Remote web에서 원격협업 참여 할 때까지 잠시 대기
time.sleep(5)

# 헤더 서비스창 : +, 이미지, 플레쉬, 메뉴히든 버튼
if driver.find_element(
    AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/cl_footer_wrapper").is_displayed():
    print("footer창이 정상적으로 출력되었습니다.")
else:
    ("footer창이 출력되지 않았습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# + 버튼 선택
plusbtn = driver.find_element(
    AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/iv_more")
actions = ActionChains(driver)\
    .move_to_element(plusbtn)\
    .click(plusbtn)\
    .perform()

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# popup_wrapper창 출력 확인
if driver.find_element(
    AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/cl_default_more_popup_wrapper").is_displayed():
    print("pop_wrapper창이 정상적으로 출력되었습니다.")
else:
    print("pop_wrapper창이 출력되지 않았습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 참가자 정보 선택
Participant_info = driver.find_element(
    AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/ll_participants_info_wrapper")
actions = ActionChains(driver)\
    .move_to_element(Participant_info)\
    .click(Participant_info)\
    .perform()

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# recycler_view창 출력 여부 확인
if driver.find_element(
    AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/recycler_view").is_displayed():
    print("recycler_view창이 정상적으로 출력되었습니다.")
else:
    print("recycler_view창이 출력되지 않았습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 전체 공유할 원격협업 멤버 선택
remote_member = driver.find_element(
    AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]")
actions = ActionChains(driver)\
    .move_to_element(remote_member)\
    .click(remote_member)\
    .perform()

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# tv_name창 출력 여부 확인
if driver.find_element(
    AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/tv_name").is_displayed():
    print("tv_name창이 정상적으로 출력되었습니다.")
else:
    print("tv_name창이 출력되지 않았습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 전체 공유 버튼 클릭
video_wrapperbtn = driver.find_element(
    AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/cl_video_force_wrapper")
actions = ActionChains(driver)\
    .move_to_element(video_wrapperbtn)\
    .click(video_wrapperbtn)\
    .perform()
print("전체 공유 버튼을 선택하였습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 좌표 찾기
# frame_pointing = driver.find_element(
#     AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/frame_pointing")
# location = frame_pointing.location
# size = frame_pointing.size
# w, h = size['width'], size['height']

# print(location)
# print(size)
# print(w, h)

# time.sleep(3)

# Mobile remote 화면에 포인팅
i = 0
while i < 1:
    
    # Default 1번 컬러 포인팅
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(
        driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(317, 1025)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(314, 1035)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    
    # 3초 암묵적 대기
    driver.implicitly_wait(time_wait=3)
    
    # 삼각형 메뉴 버튼 선택 > 메뉴 열기
    menu_btn = driver.find_element(
        AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/iv_pointing")
    actions = ActionChains(driver)\
        .move_to_element(menu_btn)\
        .click(menu_btn)\
        .perform()
    
    # 3초 암묵적 대기
    driver.implicitly_wait(time_wait=3)
    
    # 포인팅 컬러 버튼 선택
    pointing_color = driver.find_element(
        AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/cl_pointing_color_wrapper")
    actions = ActionChains(driver)\
        .move_to_element(pointing_color)\
        .click(pointing_color)\
        .perform()
    
    # 3초 암묵적 대기
    driver.implicitly_wait(time_wait=3)
    
    # 컬러 2번 선택
    color_2 = driver.find_element(
        AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/iv_color_2")
    actions = ActionChains(driver)\
        .move_to_element(color_2)\
        .click(color_2)\
        .perform()
    
    # 3초 암묵적 대기
    driver.implicitly_wait(time_wait=3)
    
    # 삼각형 메뉴 버튼 선택 > 메뉴 닫기
    menu_btn = driver.find_element(
        AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/iv_pointing")
    actions = ActionChains(driver)\
        .move_to_element(menu_btn)\
        .click(menu_btn)\
        .perform()
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_wait=3)
    
    # 2번 컬러 터치 포인팅
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(
        driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(584, 1120)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(589, 1117)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    
    # 3초 암묵적 대기
    driver.implicitly_wait(time_wait=3)
    
    # 삼각형 메뉴 버튼 선택 > 메뉴 열기
    menu_btn = driver.find_element(
        AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/iv_pointing")
    actions = ActionChains(driver)\
        .move_to_element(menu_btn)\
        .click(menu_btn)\
        .perform()
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_wait=3)
    
    # 포인팅 컬러 버튼 선택
    pointing_color = driver.find_element(
        AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/cl_pointing_color_wrapper")
    actions = ActionChains(driver)\
        .move_to_element(pointing_color)\
        .click(pointing_color)\
        .perform()
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_wait=3)
    
    # 컬러 3번 선택
    color_2 = driver.find_element(
        AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/iv_color_3")
    actions = ActionChains(driver)\
        .move_to_element(color_2)\
        .click(color_2)\
        .perform()
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_wait=3)
    
    # 삼각형 메뉴 버튼 선택 > 메뉴 닫기
    menu_btn = driver.find_element(
        AppiumBy.ID, "com.virnect.remote.mobile2.staging:id/iv_pointing")
    actions = ActionChains(driver)\
        .move_to_element(menu_btn)\
        .click(menu_btn)\
        .perform()
    
    # 3초 암묵적 대기
    driver.implicitly_wait(time_wait=3)
    
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(
        driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(656, 1302)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(646, 1295)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    
    
    
    
    
    
    
    
    
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(
        driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(509, 1402)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(509, 1377)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(
        driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(132, 1317)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(140, 1329)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    
    i = i + 1
    break