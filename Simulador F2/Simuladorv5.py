import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Parámetros iniciales de la onda
amplitud_E = 1
frecuencia_E = 1
amplitud_B = 1
frecuencia_B = 1

# Crear la figura y los ejes 3D
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

# Eliminar la cuadrícula y las etiquetas de los ejes
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
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

# Añadir nomenclatura a los ejes
ax.text(4 * np.pi, 0, 0, 'X', color='black', fontsize=12, ha='right')
ax.text(0, 2, 0, 'Y', color='black', fontsize=12, va='bottom')
ax.text(0, 0, 2, 'Z', color='black', fontsize=12, ha='left')

# Añadir vectores sobre las ondas y etiquetas B y E 
# Vector sobre la onda roja (Campo Magnético B) 
ax.quiver(2 * np.pi, 0, amplitud_B, 1, 0, 0, color='red', pivot='tail', length=1, normalize=True) 
ax.text(2 * np.pi, 0, amplitud_B, 'B', color='red', fontsize=12, ha='left') 

# Vector sobre la onda azul (Campo Eléctrico E) 
ax.quiver(2 * np.pi, amplitud_E, -1.5, 1, 0, 0, color='blue', pivot='tail', length=1, normalize=True) 
ax.text(2 * np.pi, amplitud_E, -1.5, 'E', color='blue', fontsize=12, ha='left')

# Añadir un vector que indique la dirección de propagación  (inicio_x, inicio_y, inicio_z, dir_x, dir_y, dir_z)
ax.quiver(4 * np.pi, 0.5, 2 , 1, 0, 0, color='green', pivot='tail', length=1, normalize=True)
ax.text(4 * np.pi + 1, 0, 2, 'V', color='green', fontsize=12, ha='right')

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



# faltan:
# botones interactivos: modificar frecuencia, amplitud y calcular longitud de onda.
