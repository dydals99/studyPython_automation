import pyautogui
import time

# 화면 크기 출력
print(pyautogui.size())

# 마우스 위치 출력
# time.sleep(2)
# print(pyautogui.position())

# 마우스 이동 
# pyautogui.moveTo(41, 442)
# pyautogui.moveTo(2430, 303, 2)

# 마우스 클릭 
# pyautogui.click()
# pyautogui.click(button='right')
# pyautogui.doubleClick()
# pyautogui.click(clicks=3, interval=1) # 3번 클릭할건데 1초마다 눌러라

# 마우스 드래그
# 3135,65 -> 2969,63
pyautogui.moveTo(3135, 65, 2)
pyautogui.dragTo(2969, 63, 2)