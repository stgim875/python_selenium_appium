from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

from pywinauto.application import Application
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from appium import webdriver

from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.actions.action_builder import KeyInput
from selenium.webdriver.common.actions.action_builder import PointerActions
from selenium.webdriver.common.actions.action_builder import PointerInput


import uiautomation as auto
import time
