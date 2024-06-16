from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_imc():
    if request.method == 'POST':
        peso = float(request.form['peso'].replace(',', '.'))
        altura = float(request.form['altura'].replace(',', '.'))
        imc = peso / (altura ** 2)
        imc = round(imc, 2)
        return render_template('resultado.html', imc=imc)
    return render_template('calcular.html')

if __name__ == '__main__':
    app.run(debug=True)

