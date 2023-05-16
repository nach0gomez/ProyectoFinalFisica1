import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = tk.Tk()
root.geometry("800x600")

# Crear figura y eje
fig = Figure(figsize=(6, 5), dpi=100)
ax = fig.add_subplot(111)

# Datos de la gráfica
x = range(20, 151)
y = ['Estado sólido', 'Estado líquido', 'Estado gaseoso']

# Dibujar la gráfica
ax.plot(x, [1]*len(x), 'r', label='Estado sólido')
ax.plot(x, [2]*len(x), 'b', label='Estado líquido')
ax.plot(x, [3]*len(x), 'g', label='Estado gaseoso')
ax.set_xlabel('Temperatura (°C)')
ax.set_ylabel('Estado de la materia')
ax.legend()

# Crear lienzo de la figura en tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.mainloop()
