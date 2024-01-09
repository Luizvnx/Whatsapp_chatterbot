import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


class BotService:

    def __init__(self):
        config_file_path = os.path.join(dir_path, 'configuration.json')
        with open(config_file_path, 'r') as config_file:
            self.opcoes_servico = json.load(config_file)


    def print_json(self):
        print(self.opcoes_servico.items())