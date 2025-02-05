from flask import Flask, request, jsonify
from sympy import symbols, Function, Eq, laplace_transform, cos, sin
from sympy.abc import s, t

app = Flask(__name__)

@app.route('/calculate')
def calculate():
    equation = request.args.get('equation')
    y = Function('y')
    y1 = Function('y1')
    y2 = Function('y2')

    if equation == 'eq1':
        eq = Eq(y(t).diff(t, 2) + y(t), cos(t))
    elif equation == 'eq2':
        eq = Eq(y1(t).diff(t, 2) + y1(t), sin(t))
    elif equation == 'eq3':
        eq = Eq(y2(t).diff(t, 2) + y2(t), cos(t) + sin(t))
    else:
        return jsonify(result="Ecuación no válida")

    L_eq_lhs = laplace_transform(eq.lhs, t, s)[0]
    L_eq_rhs = laplace_transform(eq.rhs, t, s)[0]
    L_eq = L_eq_lhs - L_eq_rhs
    result = L_eq.simplify()

    return jsonify(result=str(result))

if __name__ == '__main__':
    app.run(debug=True)
""" 
#* Paso a Paso del Programa:
3. **Definición de las Ecuaciones Diferenciales**:
   - Se crean tres ecuaciones diferenciales de segundo orden con términos de seno y coseno.

4. **Transformada de Laplace de las Ecuaciones**:
   - Se aplica la transformada de Laplace a ambas partes de cada ecuación diferencial.

5. **Solución de las Ecuaciones en el Dominio de Laplace**:
   - Se resuelven las ecuaciones transformadas en el dominio de Laplace para encontrar la función de Laplace de las soluciones.

6. **Transformada Inversa de Laplace**:
   - Se aplica la transformada inversa de Laplace para convertir las soluciones del dominio de Laplace de vuelta al dominio del tiempo.

### Descripción de los Métodos:

- **`laplace_transform(f, t, s)`**:
  - Este método aplica la transformada de Laplace a una función `f` con respecto a la variable `t`, y devuelve la función transformada en el dominio de Laplace con la variable `s`.

- **`inverse_laplace_transform(F, s, t)`**:
  - Este método aplica la transformada inversa de Laplace a una función `F` en el dominio de Laplace con la variable `s`, y devuelve la función transformada en el dominio del tiempo con la variable `t`.

- **`subs(old, new)`**:
  - Este método sustituye una expresión `old` por una nueva `new` dentro de una ecuación. Por ejemplo, `L_eq1.subs(laplace_transform(y(t), t, s), Y1)` reemplaza la transformada de Laplace de `y(t)` con `Y1` en la ecuación `L_eq1`.

 """