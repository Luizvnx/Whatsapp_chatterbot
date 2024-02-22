from usecase.obter_mensagens import get_mensagem
import session


def bot():
    while True:
        get_mensagem.buscar()

if __name__ == "__main__":
    session.iniciar_sessao(bot)
    