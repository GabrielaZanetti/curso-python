import flet as ft

def main(pagina: ft.Page):  # função principal
    titulo = ft.Text("HashZap")
    nome_usuario = None  # variável global para armazenar o nome do usuário

    def enviar_mensagem_tunel(mensagem):
        # Divide a mensagem para verificar o remetente
        autor, texto = mensagem.split(': ', 1)
        
        # Alinha à direita ou à esquerda com base no remetente
        alinhamento = ft.MainAxisAlignment.END if autor == nome_usuario else ft.MainAxisAlignment.START
        fundo_cor = ft.colors.BLUE_GREY_900 if autor == nome_usuario else ft.colors.BLUE_GREY_700

        # Cria a linha da mensagem com o alinhamento e a cor de fundo apropriada
        mensagem_container = ft.Container(
            content=ft.Text(mensagem),
            bgcolor=fundo_cor,
            padding=10,
            border_radius=5
        )
        
        linha_mensagem = ft.Row(
            controls=[mensagem_container],
            alignment=alinhamento
        )
        
        chat.controls.append(linha_mensagem)
        pagina.update()  # atualiza a view da tela

    pagina.pubsub.subscribe(enviar_mensagem_tunel)  # cria o túnel de comunicação

    titulo_janela = ft.Text("Bem-vindo ao HashZap")

    def enviar_mensagem(event):
        mensagem_user = f"{nome_usuario}: {mensagem_texto.value}"
        mensagem_texto.value = ""
        mensagem_texto.focus()
        pagina.pubsub.send_all(mensagem_user)  # envia a mensagem no túnel

    mensagem_texto = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem, expand=True)
    btn_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    chat = ft.Column(expand=True, scroll=ft.ScrollMode.AUTO, spacing=10)
    linha_mensagem = ft.Row([mensagem_texto, btn_enviar])

    def entrar_chat(event):
        nonlocal nome_usuario
        nome_usuario = campo_nome_usuario.value
        
        # Remover o título, remover o botão iniciar, fechar janela, criar/campo texto/botão enviar do chat
        pagina.controls.clear()
        pagina.update()
        janela.open = False

        pagina.add(chat, linha_mensagem)

        text_entrou_chat = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(text_entrou_chat)  # envia a mensagem no túnel
        mensagem_texto.focus()

    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat", on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)

    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_popup(event):
        pagina.dialog = janela
        janela.open = True
        pagina.update()  # atualiza a view da tela
        campo_nome_usuario.focus()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(titulo, botao_iniciar)

ft.app(main, view=ft.WEB_BROWSER) # execução do sistema (  // view= visualização do sistema)
