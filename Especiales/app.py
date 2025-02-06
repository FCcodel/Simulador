from flask import Flask, request, jsonify, render_template
from sympy import symbols, Function, Eq, laplace_transform, exp, cos, sin, Heaviside, latex
from sympy.abc import s, t
import sympy as sym
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate')
def calculate():
    equation = request.args.get('equation')
    u = Heaviside(t)
    a = symbols('a', real=True)

    if equation == 'eq1':
        ft = u - u.subs(t, t-2)
    elif equation == 'eq2':
        ft = exp(-a*t) * u
    elif equation == 'eq3':
        ft = sym.exp(-2*t)*u + sym.exp(-t)*sym.cos(3*t)*u
    else:
        return jsonify(result="Ecuación no válida")

    # Transformada de Laplace
    Fs = laplace_transform_suma(ft)

    return jsonify(result=latex(Fs))

def laplace_transform_suma(ft):
    '''Transformada de Laplace de suma de términos, separa constantes para conservar en resultado'''
    def separa_constante(termino):
        '''Separa constante antes de usar sym.laplace_transform(term_suma, t, s)'''
        constante = 1
        if termino.is_Mul:
            factor_mul = termino.args
            for factor_k in factor_mul:
                if not factor_k.has(t):
                    constante *= factor_k
            termino /= constante
        return termino, constante
    
    # Transformadas de Laplace por términos suma
    ft = ft.expand()  # Expresión de sumas
    ft = ft.powsimp() # Simplifica exponentes

    if ft.is_Add:
        term_suma = ft.args
    else:
        term_suma = [ft]
    
    Fs = 0
    for term_k in term_suma:
        term_k, constante = separa_constante(term_k)
        Fsk = laplace_transform(term_k, t, s)
        Fs += Fsk[0] * constante
    
    # Separa exponenciales constantes
    Fs = Fs.expand()
    return Fs

if __name__ == '__main__':
    app.run(debug=True)

    ##Origen https://blog.espol.edu.ec/telg1001/transformada-de-laplace-para-ft-con-sympy-python/ ##

    #ecuación 3: Referencia: Oppenheim Ejemplo 9.4 p658