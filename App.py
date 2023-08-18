import tkinter as tk
import re
from tkinter import ttk
from tkinter import filedialog
from tkinter import Toplevel
from tkinter import scrolledtext 

from Proyecto_compiladores import tabla_lexica
from Proyecto_compiladores import resultado_aleatorio,resultados_conversion,resultado_arreglo_operaciones,num_count, roman_count, oct_count, hex_count, bin_count, maya_count, domino_count
from Proyecto_compiladores import convertir


current_file = None
tabla = [
    ["Tipo de Token", "Valor", "Número de línea"],
    ["ROMANO", "Romano", 2],
    ["BINARIO", "Binario", 3]
]

total_tokens = num_count + roman_count + oct_count + hex_count + bin_count + maya_count + domino_count

porcentaje_distribucion = {
    "NUMERO": (num_count / total_tokens) * 100,
    "ROMANO": (roman_count / total_tokens) * 100,
    "OCTAL": (oct_count / total_tokens) * 100,
    "HEXADECIMAL": (hex_count / total_tokens) * 100,
    "BINARIO": (bin_count / total_tokens) * 100,
    "MAYA": (maya_count / total_tokens) * 100,
    "DOMINO": (domino_count / total_tokens) * 100,
}

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

    ventana_alto = ventana_lexico.winfo_reqheight()

    posicion_y = int((ventana_lexico.winfo_screenheight() / 2) - (ventana_alto / 2))
    
    ventana_lexico.geometry(f"{posicion_y}")

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
            
            editor.focus_set()  # Desactivar el enfoque automático en el scrolledtext

            def guardar():
                nuevo_contenido = editor.get('1.0', tk.END)
                with open(ruta_archivo, 'w') as archivo:
                    archivo.write(nuevo_contenido)
                ventana_editor.destroy()

            boton_guardar = tk.Button(ventana_editor, text="Guardar", command=guardar)
            boton_guardar.pack(pady=10)
            
            ventana_alto = ventana_editor.winfo_reqheight()

            posicion_y = int((ventana_editor.winfo_screenheight() / 2) - (ventana_alto / 2))
    
            ventana_editor.geometry(f"{posicion_y}")


def limpiar_canvas():
    canvas.delete("all")
    current_file = None
    
def mostrar_informacion_secundaria():
    info_window = Toplevel(root)
    info_window.title("INFORMACION SECUNDARIA")

    info_frame = ttk.Frame(info_window)
    info_frame.pack(fill="both", expand=True)

    info_label = tk.Label(info_frame, text="INFORMACION SECUNDARIA:")
    info_label.pack()

    info_text = scrolledtext.ScrolledText(info_frame, wrap=tk.WORD)
    info_text.pack(fill=tk.BOTH, expand=True)

    info_text.insert(tk.END, f"El token NUMERO aparece {num_count} veces en el archivo de entrada\n")
    info_text.insert(tk.END, f"El token ROMANO aparece {roman_count} veces en el archivo de entrada\n")
    info_text.insert(tk.END, f"El token OCTAL aparece {oct_count} veces en el archivo de entrada\n")
    info_text.insert(tk.END, f"El token HEXADECIMAL aparece {hex_count} veces en el archivo de entrada\n")
    info_text.insert(tk.END, f"El token BINARIO aparece {bin_count} veces en el archivo de entrada\n")
    info_text.insert(tk.END, f"El token MAYA aparece {maya_count} veces en el archivo de entrada\n")
    info_text.insert(tk.END, f"El token DOMINO aparece {domino_count} veces en el archivo de entrada\n")

    info_text.insert(tk.END, "\nDistribución de porcentajes:\n")
    for token_type, porcentaje in porcentaje_distribucion.items():
        info_text.insert(tk.END, f"Porcentaje de {token_type}: {porcentaje:.2f}%\n")

    info_text.config(state=tk.DISABLED)  # Hace que el texto no sea editable

    cerrar_button = tk.Button(info_frame, text="Cerrar", command=info_window.destroy)
    cerrar_button.pack(pady=10)

    info_window.geometry("+100+100") 
    
def realizarConversiones(arreglo):
    resultados = []
    for elemento in arreglo:
        match = re.match(r'(\d+)(\w+)', elemento)
        if match:
            numero = match.group(1)
            conversion = match.group(2)
            resultado = convertir(numero, conversion)
            if resultado is not None:  # Agregar esta verificación
                resultados.append(resultado)
            else:
                resultados.append("Conversión no válida")
        else:
            resultados.append("Operación desconocida")
    return resultados
    
def mostrar_resultados_modal():
    resultados_window = Toplevel(root)
    resultados_window.title("Resultados de Conversión")

    resultados_text = scrolledtext.ScrolledText(resultados_window, wrap=tk.WORD)
    resultados_text.pack(fill=tk.BOTH, expand=True)

    for conversion, resultado in zip(resultado_arreglo_operaciones, resultados_conversion):
        resultados_text.insert(tk.END, f"{conversion}: {resultado} \n ")
    resultados_text.insert(tk.END,f"{resultado_aleatorio}")
    resultados_text.config(state=tk.DISABLED)  # Hace que el texto no sea editable

    cerrar_button = tk.Button(resultados_window, text="Cerrar", command=resultados_window.destroy)
    cerrar_button.pack(pady=10)

    resultados_window.geometry("+100+100") 
    
# Crear la ventana principal
root = tk.Tk()
root.title("Convertidor de números")

icon_path = "ico/icon.png"
icon = tk.PhotoImage(file=icon_path)
icon_resized = icon.subsample(20)  # Adjust the subsample factor for desired size

# Set the resized icon as the window's icon
root.iconphoto(True, icon_resized)

# Crear botones

button_frame = ttk.Frame(root)
button_frame.pack(side="top", fill="x")

lexico_button = tk.Button(button_frame, text="Léxico", command=lambda: mostrar_lexico(tabla_lexica))
sintactico_button = tk.Button(button_frame, text="Desarrolladores", command=mostrar_about)
archivo_button = tk.Button(button_frame, text="Archivo", command=mostrar_archivo)
boton_informacion = tk.Button(button_frame, text="Información Secundaria", command=mostrar_informacion_secundaria)
boton_editar = tk.Button(button_frame, text="Editar Archivo", command=editar_archivo)
boton_mostrar_resultados = tk.Button(button_frame, text="Mostrar Resultados", command=mostrar_resultados_modal)


archivo_button.pack(side="left", padx=5, pady=5)
boton_editar.pack(side="left", padx=5, pady=5)
lexico_button.pack(side="left", padx=5, pady=5)
boton_informacion.pack(side="left", padx=5, pady=5)
boton_mostrar_resultados.pack(side="left", padx=5, pady=5)
sintactico_button.pack(side="left", padx=5, pady=5)
# Crear canvas con scrollbar
canvas_frame = tk.Frame(root)
canvas_frame.pack(side="left", fill="both", expand=True)

canvas_scrollbar = tk.Scrollbar(canvas_frame)
canvas_scrollbar.pack(side="right", fill="y")

canvas = tk.Canvas(canvas_frame, yscrollcommand=canvas_scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
canvas_scrollbar.config(command=canvas.yview)

root.mainloop()