import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import Toplevel
from tkinter import messagebox
from tkinter import scrolledtext
from Proyecto_compiladores import tabla_lexica
from Proyecto_compiladores import num_count, roman_count, oct_count, hex_count, bin_count, maya_count, domino_count



current_file = None
tabla = [
    ["Tipo de Token", "Valor", "Número de línea"],
    ["ROMANO", "Romano", 2],
    ["BINARIO", "Binario", 3]
]


def mostrar_lexico(data):
    ventana_lexico = Toplevel(root)
    ventana_lexico.title("Tabla de Análisis Léxico")

    frame = tk.Frame(ventana_lexico)
    frame.pack(fill="both", expand=True)

    tabla = ttk.Treeview(frame, show="headings")
    tabla['columns'] = data[0]
    for col in data[0]:
        tabla.heading(col, text=col)
        tabla.column(col, anchor='center', width=300)

    # Insertar filas
    for row in data[1:]:
        tabla.insert('', 'end', values=row)


    tabla.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame, command=tabla.yview)
    scrollbar.pack(side="right", fill="y")
    tabla.config(yscrollcommand=scrollbar.set)

def mostrar_about():
    limpiar_canvas()
    
    parrafo = """
        Integrantes:
        - Gelen Fabiola Amador Pavón 
        - Gleny Gissela Nihimaya Torres
        - Jennebier Esther Alvarado López
        - Lleymi Nohemi Cruz Montoya
        - Michael David Chang Oseguera
        - Nicolás Antonio Lovo Montenegro
        
    """
    canvas.create_text(10, 10, text=parrafo, anchor="nw", fill="black", font=("Arial", 12))

def mostrar_archivo():
    global current_file
    limpiar_canvas()
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        current_file = archivo
        with open(archivo, "r") as f:
            contenido = f.read()
            canvas.delete("all")
            canvas.create_text(10, 10, text=contenido, anchor="nw", fill="black", font=("Arial", 12))
        

def editar_archivo():
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos de Texto", "*.txt")])
    if ruta_archivo:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            ventana_editor = tk.Toplevel(root)
            ventana_editor.title("Editor de Archivo")
            editor = scrolledtext.ScrolledText(ventana_editor, wrap=tk.WORD)
            editor.insert('1.0', contenido)
            editor.pack(fill=tk.BOTH, expand=True)

            def guardar():
                nuevo_contenido = editor.get('1.0', tk.END)
                with open(ruta_archivo, 'w') as archivo:
                    archivo.write(nuevo_contenido)
                ventana_editor.destroy()

            boton_guardar = tk.Button(ventana_editor, text="Guardar", command=guardar)
            boton_guardar.pack(pady=10)

def limpiar_canvas():
    canvas.delete("all")
    current_file = None

# Crear la ventana principal
root = tk.Tk()
root.title("Convertidor de números")

# Crear botones
#lexico_button = ttk.Button(root, text="Léxico", command=mostrar_lexico(tabla))
lexico_button = ttk.Button(root, text="Léxico", command=lambda: mostrar_lexico(tabla_lexica))
sintactico_button = ttk.Button(root, text="Desarrolladores", command=mostrar_about)
archivo_button = ttk.Button(root, text="Archivo", command=mostrar_archivo)

boton_editar = tk.Button(root, text="Editar Archivo", command=editar_archivo)


# Colocar botones en la ventana
lexico_button.pack(side="right")
sintactico_button.pack(side="right")
archivo_button.pack(side="right")
boton_editar.pack(side="right")


# Crear canvas con scrollbar
canvas_frame = tk.Frame(root)
canvas_frame.pack(side="left", fill="both", expand=True)

canvas_scrollbar = tk.Scrollbar(canvas_frame)
canvas_scrollbar.pack(side="right", fill="y")

canvas = tk.Canvas(canvas_frame, yscrollcommand=canvas_scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
canvas_scrollbar.config(command=canvas.yview)

root.mainloop()
