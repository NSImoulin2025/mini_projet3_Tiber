from flask import Flask, request, jsonify, render_template
from calculatrice import Calculatrice

app = Flask(__name__)
calculatrice = Calculatrice()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcul', methods=['POST'])
def calculer():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    operation = data.get('operation')

    try:
        if operation == 'addition':
            resultat = calculatrice.addition(a, b)
        elif operation == 'soustraction':
            resultat = calculatrice.soustraction(a, b)
        elif operation == 'multiplication':
            resultat = calculatrice.multiplication(a, b)
        elif operation == 'division':
            resultat = calculatrice.division(a, b)
        elif operation == 'puissance':
            resultat = calculatrice.puissance(a, b)
        elif operation == 'racine':
            resultat = calculatrice.racine_carree(a)
        else:
            return jsonify({'error': 'Opération non reconnue'}), 400

        return jsonify({'resultat': resultat})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
