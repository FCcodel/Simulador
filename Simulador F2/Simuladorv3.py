import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros iniciales de la onda
amplitud_E = 1
frecuencia_E = 1
amplitud_B = 1
frecuencia_B = 1

# Crear la figura y los ejes
fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111, projection='3d', facecolor='white')

# Crear los datos iniciales de la onda
x = np.linspace(0, 4 * np.pi, 1000)
z = np.linspace(0, 10, 1000)
X, Z = np.meshgrid(x, z)
Y_E = amplitud_E * np.sin(frecuencia_E * X)
Y_B = amplitud_B * np.sin(frecuencia_B * X)

# Crear las líneas de las ondas E y B
line_E, = ax.plot(x, Y_E[0, :], zs=0, zdir='z', label='Campo Eléctrico (E)', color='b')
line_B, = ax.plot(x, Y_B[0, :], zs=0, zdir='y', label='Campo Magnético (B)', color='r')

# Configurar los límites de los ejes y la orientación
ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)
ax.set_xlabel('X (Propagación)', color='black')
ax.set_ylabel('Y (Campo Magnético)', color='black')
ax.set_zlabel('Z (Campo Eléctrico)', color='black')
ax.view_init(elev=30, azim=-60)  # Ajustar la vista para que los ejes se orienten correctamente

# Eliminar la cuadrícula y los ejes adicionales
ax.grid(False)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis.line.set_color('black')
ax.yaxis.line.set_color('black')
ax.zaxis.line.set_color('black')

# Añadir las líneas de los ejes manualmente para asegurar visibilidad
ax.plot([0, 4 * np.pi], [0, 0], [0, 0], color='black')  # Eje X
ax.plot([0, 0], [-2, 2], [0, 0], color='black')  # Eje Y
ax.plot([0, 0], [0, 0], [-2, 2], color='black')  # Eje Z

# Añadir leyenda
ax.legend()

# Función para actualizar los datos de la onda
def update(val):
    global amplitud_E, frecuencia_E, amplitud_B, frecuencia_B
    Y_E = amplitud_E * np.sin(frecuencia_E * X + val / 10.0)
    Y_B = amplitud_B * np.sin(frecuencia_B * X + val / 10.0)

    line_E.set_data(x, Y_E[0, :])
    line_B.set_data(x, Y_B[0, :])
    line_E.set_3d_properties(np.zeros_like(x), 'z')
    line_B.set_3d_properties(np.zeros_like(x), 'y')

    fig.canvas.draw_idle()

# Función para animar la onda
def animate(i):
    update(i)
    return line_E, line_B

# Crear la animación
anim = FuncAnimation(fig, animate, frames=200, interval=20)

plt.show()
