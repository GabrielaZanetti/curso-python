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

    titulo_janela = ft.Text("Bem vindo ao HashZap")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")

    mensagem_texto = ft.TextField(label="Digite sua mensagem")
    btn_enviar = ft.ElevatedButton("Enviar")

    def entrar_chat(event):
        # remover o titulo, remover o btn entrar, fechar janela, criar/campo texto/botão enviar do chat
        pagina.remove(titulo, botao_iniciar)
        janela.open = False

        pagina.add(mensagem_texto, btn_enviar)
        pagina.update() # atualiza a view da tela

    botao_entrar = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)
    
    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_popup(event):
        pagina.dialog = janela
        janela.open = True

        pagina.update() # atualiza a view da tela

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(titulo, botao_iniciar)

ft.app(main) # execução do sistema (, view=ft.WEB_BROWSER  // view= visualização do sistema)
