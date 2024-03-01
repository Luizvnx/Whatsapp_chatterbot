
class BotService:
    def __init__(self):
        self.opcoes_servico = {
            '1': 'Consulta de Saldo',
            '2': 'Transferência de Fundos',
            '3': 'Recarga de Celular',
            '4': 'Sair'
        }

    def exibir_menu(self):
        print("Selecione um serviço:")
        for chave, valor in self.opcoes_servico.items():
            print(f"{chave}. {valor}")

    def iniciar_dialogo(self):
        print("Bem-vindo ao ServiçoBot!")
        while True:
            self.exibir_menu()
            escolha = input("Digite o número correspondente ao serviço desejado: ")
            
            if escolha in self.opcoes_servico:
                if escolha == '4':
                    print("Obrigado por usar o ServiçoBot. Até logo!")
                    break
                else:
                    self.processar_escolha(escolha)
            else:
                print("Escolha inválida. Por favor, selecione uma opção válida.")

    def processar_escolha(self, escolha):
        print(f"Você selecionou: {self.opcoes_servico[escolha]}")
        # Lógica para processar a escolha do cliente

# Exemplo de uso
#if __name__ == "__main__":
#    bot = BotService()
#    bot.iniciar_dialogo()
