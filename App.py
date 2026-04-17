from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = '123456'  # pode trocar depois

SENHA = "leao123"  # 🔑 sua senha geral

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        senha = request.form.get('senha')
        if senha == SENHA:
            session['logado'] = True
            return redirect('/form')
    return render_template('login.html')

@app.route('/form')
def form():
    if not session.get('logado'):
        return redirect('/')
    return render_template('form.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    if not session.get('logado'):
        return redirect('/')
    return redirect('/sucesso')

@app.route('/sucesso')
def sucesso():
    if not session.get('logado'):
        return redirect('/')
    return render_template('sucesso.html')

if __name__ == '__main__':
    app.run(debug=True)