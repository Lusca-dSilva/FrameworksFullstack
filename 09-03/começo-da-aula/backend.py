from flask import Flask, request, render_template

app = Flask(__name__)

# @app.route('/home')
# def home():
#     return render_template('index.html')

@app.route('/') 
def main():
    n1 = request.args.get('nota1')
    n2 = request.args.get('nota2')
    nota1 = float(n1)
    nota2 = float(n2)
    media = (nota1 + nota2) / 2
    

    if media > 7:
        resultado = 'Aprovado'
    elif 4 < media <= 7:
        resultado = 'Recuperação'
    else:
        resultado = 'Reprovado'
    return resultado
    
    
if __name__ == '__main__':
    app.run(debug=True)