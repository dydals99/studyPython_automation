from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pyautogui
import pyperclip

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
driver.maximize_window() # 전체화면 

# 아이디 입력 
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
pyperclip.copy("whdydals0802")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# 비밀번호 입력
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
pyperclip.copy("!Wh124578")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# 로그인 버튼 클릭 
driver.find_element(By.CSS_SELECTOR, "#log\.login").click()

