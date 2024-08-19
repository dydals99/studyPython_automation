from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 기존에는 webdriver.Chrome("chromedriver.exe 경로") 입력이 필요했지만
# 최근에는 필요없어졌다. 아래의 Options 같은 경우는 웹 브라우저가 
# 실행되자마자 꺼지는 현상을 방지하고자 작성한 코드이다. 
# pip install webdriver_manager 설치하고 아래의 코드를 작성하면 된다 . 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://www.naver.com")