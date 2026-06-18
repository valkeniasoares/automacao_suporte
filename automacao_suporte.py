import pyautogui
import time

print("Bora faturar caralho")
time.sleep(10)

while True:
    #clicar na nota
    pyautogui.click (650,321)
    time.sleep(4)
    pyautogui.click (375,207)
    time.sleep(4)

    #clilcar para abrir a fila 
    pyautogui.click(1509,186)
    time.sleep(4)

    #Realizar o reenvio 
    pyautogui.click (1029,363)
    time.sleep(4)

    #fechar a página da fila 
    pyautogui.click (1338,171)
    time.sleep(4)
    pyautogui.click (1637,185)
    time.sleep(4)
    

    #atualizar a página 
    pyautogui.click (928,250)
    time.sleep(4)