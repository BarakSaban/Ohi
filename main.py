import pyautogui

Question = input("What's your question?")
pyautogui.click(1334, 1054)
pyautogui.click(1725, 60)
pyautogui.typewrite(Question)
pyautogui.press("enter")
