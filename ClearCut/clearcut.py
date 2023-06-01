import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
from rembg import remove
from PIL import Image

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png")])
    if file_path:
        input_path_entry.delete(0, tk.END)
        input_path_entry.insert(tk.END, file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Image files", "*.png")])
    if file_path:
        output_path_entry.delete(0, tk.END)
        output_path_entry.insert(tk.END, file_path)

def remove_background():
    input_path = input_path_entry.get()
    output_path = output_path_entry.get()

    if not input_path or not output_path:
        status_label.config(text="Please select input and output paths.", fg="red")
        return

    try:
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)
        status_label.config(text="Background removed successfully.", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")

# Crear la ventana de la aplicación
window = tk.Tk()
window.title("Clear Cut")
window.geometry('400x250')

# Etiqueta y campo de entrada para el archivo de entrada
input_path_label = tk.Label(window, text="Input Path:")
input_path_label.pack(pady=(5,0))
input_path_entry = tk.Entry(window)
input_path_entry.pack()
input_path_button = tk.Button(window, text="Select File", command=select_input_file)
input_path_button.pack(pady=5)

# Etiqueta y campo de entrada para el archivo de salida
output_path_label = tk.Label(window, text="Output Path:")
output_path_label.pack(pady=(10,0))
output_path_entry = tk.Entry(window)
output_path_entry.pack()
output_path_button = tk.Button(window, text="Select File", command=select_output_file)
output_path_button.pack(pady=5)

# Etiqueta de estado
status_label = tk.Label(window, text="")
status_label.pack()

# Botón para remover el fondo
remove_button = tk.Button(window, text="Remove Background", command=remove_background)
remove_button.pack(pady=6)

# Iniciar el bucle de eventos de la aplicación
window.mainloop()