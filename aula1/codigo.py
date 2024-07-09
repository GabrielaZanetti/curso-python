# Passo 1: Acessar o site da empresa
#    Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer Login
# Passo 3: Pegar/importar a base de dados
# Passo 4: Cadastrar o primeiro produto
# Passo 5: Repetir o passo 4 até cadastrar todos os produtos

import pyautogui # automatiza mouse/teclado/tela

pyautogui.PAUSE = 0.5 # a cada comando do pyautogui faz uma pausa de meio segundo

pyautogui.press("win")
pyautogui.write("Crome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
