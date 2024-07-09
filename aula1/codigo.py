# Passo 1: Acessar o site da empresa
#    Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer Login
# Passo 3: Pegar/importar a base de dados
# Passo 4: Cadastrar o primeiro produto
# Passo 5: Repetir o passo 4 até cadastrar todos os produtos

import pyautogui # automatiza mouse/teclado/tela
import time

pyautogui.PAUSE = 0.5 # a cada comando do pyautogui faz uma pausa de meio segundo

pyautogui.press("win")
pyautogui.write("Crome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(1.5)

pyautogui.click(x=-720, y=369) # Click no input do email (deve ser alterado a posicao conforme a tela)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("pythonimpressionador@gmail.com")

pyautogui.hotkey("tab")
pyautogui.write("minha senha")

pyautogui.click(x=-698, y=536) # click no botao de login
