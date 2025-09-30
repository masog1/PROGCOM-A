import tkinter as tk
import random

# Opciones del juego
opciones = ["piedra", "papel", "tijera", "pistola", "fuego", "agua", "aire", "esponja", "humano"]

# Reglas
reglas = {
    "piedra": ["tijera", "esponja"],
    "papel": ["piedra", "pistola"],
    "tijera": ["papel", "esponja"],
    "pistola": ["tijera", "humano"],
    "fuego": ["papel", "esponja"],
    "agua": ["fuego", "pistola"],
    "aire": ["agua", "fuego"],
    "esponja": ["agua", "papel"],
    "humano": ["piedra", "fuego"]
}

# Función principal
def jugar(eleccion_jugador):
    eleccion_pc = random.choice(opciones)
    if eleccion_jugador == eleccion_pc:
        resultado = f"Empate: ambos eligieron {eleccion_jugador.capitalize()}"
    elif eleccion_pc in reglas[eleccion_jugador]:
        resultado = f"Ganaste : {eleccion_jugador.capitalize()} vence a {eleccion_pc.capitalize()}"
    else:
        resultado = f"Perdiste : {eleccion_pc.capitalize()} vence a {eleccion_jugador.capitalize()}"
    etiqueta_resultado.config(text=resultado)

# Ventana
ventana = tk.Tk()
ventana.title("Juego Extendido")
ventana.geometry("600x400")

# Texto arriba
etiqueta = tk.Label(ventana, text="Elige tu opción:", font=("Arial", 16))
etiqueta.grid(row=0, column=0, columnspan=3, pady=10)

# Botones en rejilla 3x3
for i, opcion in enumerate(opciones):
    boton = tk.Button(
        ventana, text=opcion.capitalize(), font=("Arial", 12),
        width=12, height=2, command=lambda o=opcion: jugar(o)
    )
    boton.grid(row=(i // 3) + 1, column=i % 3, padx=10, pady=10)

# Resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 14), fg="blue", wraplength=500)
etiqueta_resultado.grid(row=5, column=0, columnspan=3, pady=20)

ventana.mainloop()
