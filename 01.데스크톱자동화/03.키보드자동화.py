import pyautogui
import pyperclip

# 키보드 입력 (문자)
# pyautogui.write('studyCoding', interval=0.25)

# 키보드 입력 (키)
# pyautogui.press('enter')
# pyautogui.press('up')

# 키보드 입력 (여러개 동시에)
# 한글입력 잘되나?pyautogui.hotkey('ctrl', 'c')

# 한글 입력 방법 
pyperclip.copy('한글입력 잘되나?')
pyautogui.hotkey('ctrl', 'v')