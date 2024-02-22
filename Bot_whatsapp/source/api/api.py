from flask import Flask, request, jsonify
from Bot_whatsapp.source.dao.dao import Dao

app = Flask(__name__)
_dao = Dao(base_url="http://localhost/BOT_WHATSAPP/index.php?", headers={"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'})



@app.route('/verificar_contato/<contato>')
def search_user(contato):
    response = _dao.verificar_contato(contato)
    return jsonify(response)

#FINALIZAR ESSE AQ
@app.route('/perguntas')
def get_perguntas():
    response = _dao.enviar_perguntas()
    return jsonify(response)


@app.route('/')
def index():
    return 'Index Page'

if __name__ == '__main__':
    app.run(debug=True)
