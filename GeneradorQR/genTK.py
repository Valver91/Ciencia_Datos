import tkinter as tk
import qrcode

def generar_qr():
    enlace = enlace_entry.get()
    nombre_qr = nombre_entry.get()

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(enlace)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(f"{nombre_qr}.png")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de QR")
ventana.geometry('300x150')

# Etiqueta y campo de entrada para el enlace
enlace_label = tk.Label(ventana, text="Enlace:")
enlace_label.pack(pady=(10,0))

enlace_entry = tk.Entry(ventana)
enlace_entry.pack()

# Etiqueta y campo de entrada para el nombre del archivo QR
nombre_label = tk.Label(ventana, text="Nombre del archivo QR:")
nombre_label.pack(pady=(10,0))

nombre_entry = tk.Entry(ventana)
nombre_entry.pack()

# Botón para generar el QR
generar_button = tk.Button(ventana, text="Generar QR", command=generar_qr)
generar_button.pack(pady=(10,0))

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
