import numpy as np
import matplotlib.pyplot as plt # type: ignore
from matplotlib.animation import FuncAnimation # type: ignore
from mpl_toolkits.mplot3d import Axes3D # type: ignore
from matplotlib.widgets import Slider, Button # type: ignore

# Parámetros iniciales de la onda
amplitud_E = 1
frecuencia_E = 1
amplitud_B = 1
frecuencia_B = 1

# Crear la figura y los ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Crear los datos iniciales de la onda
x = np.linspace(0, 4 * np.pi, 1000)
y_E = amplitud_E * np.sin(frecuencia_E * x)
z_B = amplitud_B * np.sin(frecuencia_B * x)

# Crear las líneas de las ondas E y B
line_E, = ax.plot(x, y_E, np.zeros_like(x), label='Campo Eléctrico (E)')
line_B, = ax.plot(x, np.zeros_like(x), z_B, label='Campo Magnético (B)')

# Configurar los límites de los ejes
ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)

# Añadir leyenda
ax.legend()

# Crear los deslizadores para cambiar los parámetros de las ondas
axcolor = 'lightgoldenrodyellow'
ax_amplitud_E = plt.axes([0.15, 0.01, 0.65, 0.03], facecolor=axcolor)
ax_frecuencia_E = plt.axes([0.15, 0.05, 0.65, 0.03], facecolor=axcolor)
ax_amplitud_B = plt.axes([0.15, 0.09, 0.65, 0.03], facecolor=axcolor)
ax_frecuencia_B = plt.axes([0.15, 0.13, 0.65, 0.03], facecolor=axcolor)

slider_amplitud_E = Slider(ax_amplitud_E, 'Amplitud E', 0.1, 2.0, valinit=amplitud_E)
slider_frecuencia_E = Slider(ax_frecuencia_E, 'Frecuencia E', 0.1, 2.0, valinit=frecuencia_E)
slider_amplitud_B = Slider(ax_amplitud_B, 'Amplitud B', 0.1, 2.0, valinit=amplitud_B)
slider_frecuencia_B = Slider(ax_frecuencia_B, 'Frecuencia B', 0.1, 2.0, valinit=frecuencia_B)

# Función para actualizar los datos de la onda
def update(val):
    global amplitud_E, frecuencia_E, amplitud_B, frecuencia_B
    amplitud_E = slider_amplitud_E.val
    frecuencia_E = slider_frecuencia_E.val
    amplitud_B = slider_amplitud_B.val
    frecuencia_B = slider_frecuencia_B.val

    y_E = amplitud_E * np.sin(frecuencia_E * x)
    z_B = amplitud_B * np.sin(frecuencia_B * x)

    line_E.set_ydata(y_E)
    line_B.set_zdata(z_B)

    fig.canvas.draw_idle()

# Conectar los deslizadores a la función de actualización
slider_amplitud_E.on_changed(update)
slider_frecuencia_E.on_changed(update)
slider_amplitud_B.on_changed(update)
slider_frecuencia_B.on_changed(update)

# Función para animar la onda
def animate(i):
    y_E = amplitud_E * np.sin(frecuencia_E * x + i / 10.0)
    z_B = amplitud_B * np.sin(frecuencia_B * x + i / 10.0)

    line_E.set_ydata(y_E)
    line_B.set_zdata(z_B)

    return line_E, line_B

# Botón de 'play' para comenzar la animación
ax_play = plt.axes([0.8, 0.01, 0.1, 0.04])
button_play = Button(ax_play, 'Play', color=axcolor, hovercolor='0.975')

anim_running = False

def play(event):
    global anim_running
    if anim_running:
        anim.event_source.stop()
        button_play.label.set_text('Play')
    else:
        anim.event_source.start()
        button_play.label.set_text('Pause')
    anim_running = not anim_running

button_play.on_clicked(play)

# Botón para mostrar/ocultar los planos de oscilación de los campos E y B
show_planes = True

def toggle_planes(event):
    global show_planes
    show_planes = not show_planes
    if show_planes:
        ax.plot(x, y_E, np.zeros_like(x), label='Campo Eléctrico (E)')
        ax.plot(x, np.zeros_like(x), z_B, label='Campo Magnético (B)')
    else:
        ax.lines.pop()
        ax.lines.pop()
    fig.canvas.draw_idle()

ax_toggle_planes = plt.axes([0.8, 0.07, 0.1, 0.04])
button_toggle_planes = Button(ax_toggle_planes, 'Toggle Planes', color=axcolor, hovercolor='0.975')
button_toggle_planes.on_clicked(toggle_planes)

# Crear la animación
anim = FuncAnimation(fig, animate, frames=200, interval=20)

plt.show()
