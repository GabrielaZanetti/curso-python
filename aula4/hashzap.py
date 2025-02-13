## Passo a Passo
# Titulo: HashZap
# Botão: iniciar o chat(abre um popUp)
# PopUp: Titulo, input para o nome, botão para acessar o chat
# Tela do chat: Nova tela com "%nome% entrou no chat", input para nova mensagem e botão de enviar

# Flet → apps/site/programas de computador
# `pip install flet`

import flet as ft

class Message():
    def __init__(self, user: str, name: str, text: str):
        self.user = user
        self.name = name
        self.text = text

def main(pagina: ft.Page):  # função principal
    titulo = ft.Text("HashZap")
    nome_usuario = None  # variável global para armazenar o nome do usuário
    def get_initials(user_name: str):
        return user_name[:1].capitalize()

    def get_avatar_color(user_name: str):
        colors_lookup = [
            ft.colors.AMBER,
            ft.colors.BLUE,
            ft.colors.BROWN,
            ft.colors.CYAN,
            ft.colors.GREEN,
            ft.colors.INDIGO,
            ft.colors.LIME,
            ft.colors.ORANGE,
            ft.colors.PINK,
            ft.colors.PURPLE,
            ft.colors.RED,
            ft.colors.TEAL,
            ft.colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]
    
    def enviar_mensagem_tunel(mensagem: Message):
        # Alinha à direita ou à esquerda com base no remetente
        alinhamento = ft.MainAxisAlignment.END if mensagem.user == pagina.session_id else ft.MainAxisAlignment.START
        fundo_cor = ft.colors.BLUE_GREY_900 if mensagem.user == pagina.session_id else ft.colors.BLUE_GREY_700

        # Cria a linha da mensagem com o alinhamento e a cor de fundo apropriada
        mensagem_eu = ft.Container(
            content=ft.Text(f"{mensagem.text}"),
            bgcolor=fundo_cor,
            margin=ft.margin.only(right=15),
            padding=10,
            border_radius=5
        )

        mensagem_env = None
        if mensagem.user == pagina.session_id:
            mensagem_env = mensagem_eu  # Mensagem do próprio usuário
        else:
            mensagem_env = ft.Row([
                ft.CircleAvatar(
                    content=ft.Text(get_initials(user_name=mensagem.name)),
                    color=ft.colors.WHITE,
                    bgcolor=get_avatar_color(user_name=mensagem.name),
                ), 
                ft.Column(
                    [
                        ft.Text(mensagem.name, weight="bold"),
                        ft.Text(mensagem.text, selectable=True),
                    ],
                    tight=True,
                    spacing=5,
                )
            ])  # Mensagem de outro usuário


        linha_mensagem = ft.Row(
            controls=[mensagem_env],
            alignment=alinhamento
        )
        
        chat.controls.append(linha_mensagem)
        pagina.update()  # atualiza a view da tela
        chat.scroll_to(offset=-1, duration=100)

    pagina.pubsub.subscribe(enviar_mensagem_tunel)  # cria o túnel de comunicação

    titulo_janela = ft.Text("Bem-vindo ao HashZap")

    def enviar_mensagem(event):
        if not mensagem_texto.value:
            mensagem_texto.focus()
        else:
            pagina.pubsub.send_all(Message(user=pagina.session_id, name=nome_usuario, text=mensagem_texto.value)) # envia a mensagem no túnel
            mensagem_texto.value = ""
            mensagem_texto.focus()

    mensagem_texto = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem, expand=True)
    btn_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    chat = ft.Column(expand=True, scroll=ft.ScrollMode.AUTO)
    linha_mensagem = ft.Row([mensagem_texto, btn_enviar])

    def entrar_chat(event):
        if not campo_nome_usuario.value:
            campo_nome_usuario.error_text = "Informe um usuário"
            campo_nome_usuario.update()
        else:
            nonlocal nome_usuario
            nome_usuario = campo_nome_usuario.value
            
            # Remover o título, remover o botão iniciar, fechar janela, criar/campo texto/botão enviar do chat
            pagina.controls.clear()
            pagina.update()
            janela.open = False

            pagina.add(chat, linha_mensagem)
            pagina.pubsub.send_all(Message(user=pagina.session_id, name=nome_usuario, text="entrou no chat"))
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
