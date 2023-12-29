from usecase.responder_clientes import response
from usecase.obter_mensagens import get_mensagem

def iniciar_sessao():
    try:
        exec(open('session.py').read())
        pass
    except FileNotFoundError:
        print("O arquivo 'session' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao executar 'session.py': {e}")


def bot():
    while True:
        get_mensagem.buscar()
        #if msg is not None:
            #response.response_client(msg)
        #else:
            #print('AGUARDANDO NOVAS MENSAGENS')

if __name__ == "__main__":
    iniciar_sessao()
    bot()