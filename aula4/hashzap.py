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

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update() # atualiza a view da tela

    pagina.pubsub.subscribe(enviar_mensagem_tunel) # cria o tunel de comunicacao

    titulo_janela = ft.Text("Bem vindo ao HashZap")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")

    mensagem_texto = ft.TextField(label="Digite sua mensagem")

    def enviar_mensagem(event):
        mensagem_user = f"{campo_nome_usuario.value}: {mensagem_texto.value}"
        mensagem_texto.value = ""
        pagina.pubsub.send_all(mensagem_user) # envia a mensagem no tunel

    btn_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    chat = ft.Column()
    linha_mensagem = ft.Row([ mensagem_texto, btn_enviar ])

    def entrar_chat(event):
        # remover o titulo, remover o btn entrar, fechar janela, criar/campo texto/botão enviar do chat
        pagina.remove(titulo, botao_iniciar)
        janela.open = False

        pagina.add(chat, linha_mensagem)
        
        text_entrou_chat = f"{campo_nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(text_entrou_chat) # envia a mensagem no tunel

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

ft.app(main, view=ft.WEB_BROWSER) # execução do sistema (  // view= visualização do sistema)
