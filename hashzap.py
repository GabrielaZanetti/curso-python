## Passo a Passo
# Titulo: HashZap
# Botão: iniciar o chat(abre um popUp)
# PopUp: Titulo, input para o nome, botão para acessar o chat
# Tela do chat: Nova tela com "%nome% entrou no chat", input para nova mensagem e botão de enviar

# Flet → apps/site/programas de computador
# `pip install flet`

import flet as ft

def main(pagina): # função principal
    titulo = ft.Text("HashZap")

    def abrir_popup(event):
        print('Click')

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(titulo)
    pagina.add(botao_iniciar)

ft.app(main) # execução do sistema ( view=ft.WEB_BROWSER // view= visualização do sistema)
