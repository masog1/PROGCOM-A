import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json


# -------------------------------
# Función para generar la señal
# -------------------------------
def generar_senal():
    try:
        dur = float(entry_duracion.get())
        freq = float(entry_frecuencia.get())
        amp = float(entry_amplitud.get())
        dec = float(entry_decay.get())

        t = np.linspace(0, dur, 500)
        presion = 80 + amp * np.sin(2 * np.pi * freq * t) * np.exp(-t/dec)

        PAS = round(np.max(presion), 1)
        PAD = round(np.min(presion), 1)
        PP = round(PAS - PAD, 1)

        label_pas.config(text=f"PAS: {PAS} mmHg")
        label_pad.config(text=f"PAD: {PAD} mmHg")
        label_pp.config(text=f"PP: {PP} mmHg")

        fig.clear()
        ax = fig.add_subplot(111)
        ax.plot(t, presion, linewidth=2)
        ax.set_title("Simulación de Presión Arterial")
        ax.set_xlabel("Tiempo (s)")
        ax.set_ylabel("Presión (mmHg)")
        ax.grid()

        canvas.draw()

    except ValueError:
        messagebox.showerror("Error", "Ingresa valores numéricos válidos.")


# -------------------------------
# Guardar configuración en JSON
# -------------------------------
def guardar_json():
    data = {
        "duracion": entry_duracion.get(),
        "frecuencia": entry_frecuencia.get(),
        "amplitud": entry_amplitud.get(),
        "decay": entry_decay.get()
    }

    file_path = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("JSON files", "*.json")]
    )

    if file_path:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        messagebox.showinfo("Guardado", "Configuración guardada correctamente.")


# -------------------------------
# Cargar configuración desde JSON
# -------------------------------
def cargar_json():
    file_path = filedialog.askopenfilename(
        filetypes=[("JSON files", "*.json")]
    )

    if file_path:
        try:
            with open(file_path, "r") as f:
                data = json.load(f)

            entry_duracion.delete(0, tk.END)
            entry_frecuencia.delete(0, tk.END)
            entry_amplitud.delete(0, tk.END)
            entry_decay.delete(0, tk.END)

            entry_duracion.insert(0, data["duracion"])
            entry_frecuencia.insert(0, data["frecuencia"])
            entry_amplitud.insert(0, data["amplitud"])
            entry_decay.insert(0, data["decay"])

        except:
            messagebox.showerror("Error", "Archivo JSON inválido.")


# -------------------------------
# Ventana principal Tkinter
# -------------------------------
root = tk.Tk()
root.title("Simulación de Presión Arterial")
root.geometry("900x600")

# Frame de controles
frame_controls = tk.Frame(root)
frame_controls.pack(side="left", padx=20, pady=20)

tk.Label(frame_controls, text="Duración (s):").pack()
entry_duracion = tk.Entry(frame_controls)
entry_duracion.pack()
entry_duracion.insert(0, "2")

tk.Label(frame_controls, text="Frecuencia (Hz):").pack()
entry_frecuencia = tk.Entry(frame_controls)
entry_frecuencia.pack()
entry_frecuencia.insert(0, "1.2")

tk.Label(frame_controls, text="Amplitud:").pack()
entry_amplitud = tk.Entry(frame_controls)
entry_amplitud.pack()
entry_amplitud.insert(0, "40")

tk.Label(frame_controls, text="Decay:").pack()
entry_decay = tk.Entry(frame_controls)
entry_decay.pack()
entry_decay.insert(0, "1.5")

btn_generar = tk.Button(frame_controls, text="Generar Señal", command=generar_senal)
btn_generar.pack(pady=10)

btn_guardar = tk.Button(frame_controls, text="Guardar JSON", command=guardar_json)
btn_guardar.pack(pady=5)

btn_cargar = tk.Button(frame_controls, text="Cargar JSON", command=cargar_json)
btn_cargar.pack(pady=5)

label_pas = tk.Label(frame_controls, text="PAS: --")
label_pas.pack()

label_pad = tk.Label(frame_controls, text="PAD: --")
label_pad.pack()

label_pp = tk.Label(frame_controls, text="PP: --")
label_pp.pack()

# Gráfica de Matplotlib
fig = plt.Figure(figsize=(6, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side="right", padx=20, pady=20)

root.mainloop()
