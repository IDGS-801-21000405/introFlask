from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    titulo = 'IDGS801'
    lista = ['Carlos', 'Christian', 'Briones', 'Milton']
    return render_template('index.html', titulo=titulo, lista=lista)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route('/hola')
def hola():
    return "<h1>Hola, Mundo!</h1>"

@app.route('/user/<string:user>')
def user(user):
    return f'<h1>Hola, {user}!</h1>'

@app.route('/numero/<int:n>')
def numero(n):
    return f'<h1>El número es: {n}</h1>'

@app.route('/user/<int:id>/<string:username>')
def user2(id, username):
    return f'<h1>El usuario es: {username} con id: {id}</h1>'

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
    return f'<h1>La suma es: {n1 + n2}</h1>'

@app.route('/default/')
@app.route('/default/<string:param>')
def func(param='juan'):
    return f'''
        <form action="/default/" method="get">
            <label for="param">Ingresa el parámetro:</label>
            <input type="text" id="param" name="param" value="{param}">
            <button type="submit">Enviar</button>
        </form>
        <h1>El parámetro es: {param}</h1>
    '''

@app.route("/operaciones")
def operaciones():
    return render_template("OperacionesBasicas.html")

@app.route("/cinepolis", methods=["GET","POST"])
def cinepolis():
    nombre = request.form.get("nombre")  
    if nombre: 
        return render_template("cinepolis.html", nombre=nombre)
    
    return render_template("cinepolis.html")

@app.route("/resultado-cinepolis", methods=["POST"])
def resultadoCinepolis():
    nombre = request.form.get("nombre")
    asistentes = int(request.form.get("asistentes"))
    boletos = int(request.form.get("boletos")) 
    metodo = int(request.form.get("metodo"))
    ventaTotal = 0
    venta = 0
    descuento = 0

    boletosPermitidos =  7 * asistentes
    if boletos <= boletosPermitidos:
        total = boletos * 12
        descuento = 0
        if boletos > 5:
            descuento = 15
        elif 2 < boletos <= 5:
            descuento = 10
        if metodo == 2:
            descuento += 10
        totalVenta = total - (total * descuento / 100)
    else:
        resultado = f'Solamente puede comprar: {boletosPermitidos} boletos'
        return render_template("cinepolis-resultado.html", resultado=resultado)

    if metodo == 1:
        metodo = 'Efectivo'
    elif metodo == 2:
        metodo = 'Tarjeta Cinepolis'

    return render_template("cinepolis-resultado.html", nombre=nombre, asistentes=asistentes, boletos=boletos, metodo=metodo, totalVenta=totalVenta)

@app.route("/resultado", methods=["POST"])
def resultado():

    numero1 = request.form.get("numero1")
    numero2 = request.form.get("numero2")
    tipoOperacion = int(request.form.get("operacion")) 

    resultado = ""

    if (tipoOperacion == 1):
        resultado = "La suma de {} + {} es = {}".format(numero1, numero2, str(int(numero1)+int(numero2)))
    elif (tipoOperacion == 2):
        resultado =  "La resta de {} - {} es = {}".format(numero1, numero2, str(int(numero1)-int(numero2)))
    elif (tipoOperacion == 3):
        resultado =  "La multiplicacion de {} * {} es = {}".format(numero1, numero2, str(int(numero1)*int(numero2)))
    elif (tipoOperacion == 4):
        resultado =  "La division de {} / {} es = {}".format(numero1, numero2, str(int(numero1)/int(numero2)))

    return resultado

if __name__ == "__main__":
    app.run(debug=True, port=3000)