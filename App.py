#Librerias utilizadas
import re
import random
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from tkinter import Toplevel
from tkinter import scrolledtext 
import random
from Proyecto_compiladores import obtenerOperaciones
from Proyecto_compiladores import tabla_lexica
from Proyecto_compiladores import resultados_conversion,resultado_arreglo_operaciones,num_count, roman_count, oct_count, hex_count, bin_count, maya_count, domino_count
from Proyecto_compiladores import convertir



current_file = None
tabla = [
    ["Tipo de Token", "Valor", "Número de línea"],
    ["ROMANO", "Romano", 2],
    ["BINARIO", "Binario", 3]
]
#Convertir numero de tokens en porcentaje 

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

#Funcion para la tabla de analisis lexico

def mostrar_lexico(data):
    ventana_lexico = Toplevel(root)
    ventana_lexico.title("Tabla de Análisis Léxico")

    frame = tk.Frame(ventana_lexico)
    frame.pack(fill="both", expand=True)

    style = ttk.Style()
    style.configure("Treeview", font=("Arial", 15))
    
    tabla = ttk.Treeview(frame, show="headings", height=20, style="Treeview")
    tabla['columns'] = data[0]
    for col in data[0]:
        tabla.heading(col, text=col)
        tabla.column(col, anchor='center', width=200)

    # Insertar filas
    for row in data[1:]:
        tabla.insert('', 'end', values=row)

    tabla.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame, command=tabla.yview)
    scrollbar.pack(side="right", fill="y")
    tabla.config(yscrollcommand=scrollbar.set)

    ventana_lexico.geometry("900x500")  # Ajustar el tamaño de la ventana
    ventana_lexico.resizable(False, False)

#Desarrolladores

def mostrar_about():
    limpiar_canvas()
    
    parrafo = """
        Integrantes Grupo #1 IS-913:
        
        - Gelen Fabiola Amador Pavón 
        - Gleny Gissela Nihimaya Torres
        - Jennebier Esther Alvarado López
        - Lleymi Nohemi Cruz Montoya
        - Michael David Chang Oseguera
        - Nicolás Antonio Lovo Montenegro
    """
    canvas.create_text(10, 10, text=parrafo, anchor="nw",fill="black", font=("Arial", 15))

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
        
    

    
 #funcion para edicion de archivo   

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

                # Actualizar resultados después de guardar
                global resultado_arreglo_operaciones, resultados_conversion
                resultado_arreglo_operaciones = obtenerOperaciones(nuevo_contenido)
                resultados_conversion = realizarConversiones(resultado_arreglo_operaciones)
                
                limpiar_canvas()
                canvas.delete("all")
                canvas.create_text(10, 10, text=nuevo_contenido, anchor="nw", fill="black", font=("Arial", 14))


            boton_guardar = tk.Button(ventana_editor, text="Guardar", command=guardar)
            boton_guardar.pack(pady=10)
            
            ventana_editor.resizable(False,False)
            ventana_editor.geometry("600x500") 

def limpiar_canvas():
    canvas.delete("all")
    current_file = None
    
    
#funcion para desplegar el modal de informacion secundaria

def mostrar_informacion_secundaria():
    info_window = Toplevel(root)
    info_window.title("INFORMACION SECUNDARIA")

    info_frame = ttk.Frame(info_window)
    info_frame.pack(fill="both", expand=True)

    info_text = scrolledtext.ScrolledText(info_frame, wrap=tk.WORD, font=("Arial", 14))
    info_text.pack(fill=tk.BOTH, expand=True)

    info_text.tag_configure("center", justify="center")
    info_text.insert(tk.END, f"El token NUMERO aparece {num_count} veces en el archivo de entrada\n", "center")
    info_text.insert(tk.END, f"El token ROMANO aparece {roman_count} veces en el archivo de entrada\n", "center")
    info_text.insert(tk.END, f"El token OCTAL aparece {oct_count} veces en el archivo de entrada\n", "center")
    info_text.insert(tk.END, f"El token HEXADECIMAL aparece {hex_count} veces en el archivo de entrada\n", "center")
    info_text.insert(tk.END, f"El token BINARIO aparece {bin_count} veces en el archivo de entrada\n", "center")
    info_text.insert(tk.END, f"El token MAYA aparece {maya_count} veces en el archivo de entrada\n", "center")
    info_text.insert(tk.END, f"El token DOMINO aparece {domino_count} veces en el archivo de entrada\n", "center")

    info_text.insert(tk.END, "\nDistribución de porcentajes:\n", "center")
    for token_type, porcentaje in porcentaje_distribucion.items():
        info_text.insert(tk.END, f"Porcentaje de {token_type}: {porcentaje:.2f}%\n", "center")

    info_text.config(state=tk.DISABLED)  

    cerrar_button = tk.Button(info_frame, text="Cerrar", command=info_window.destroy)
    cerrar_button.pack(pady=10)

    info_window.geometry("600x400") 
    info_window.resizable(False, False)


def realizarConversiones(arreglo):
    resultados=[]
    for elemento in arreglo:
        match = re.match(r'(\d+)(\w+)', elemento)
        if match:
            numero = match.group(1)
            conversion = match.group(2)
            if conversion == "Aleatorio":
                resultado = convertir_aleatoriamente(numero)
            else:
                resultado = convertir(numero, conversion)
        else:
            resultado="Operación desconocida"
        resultados.append(resultado)
    return resultados

def convertir_aleatoriamente(numero):
    sistemas_conversion = ["Romano", "Binario", "Octal", "Hexadecimal", "Maya", "Domino"]
    sistema_aleatorio = random.choice(sistemas_conversion)
    resultado = convertir(numero, sistema_aleatorio)
    return resultado

    

def mostrar_resultados_modal():
    resultados_window = Toplevel(root)


    resultados_frame = ttk.Frame(resultados_window)
    resultados_frame.pack(fill="both", expand=True)

    resultados_label = tk.Label(resultados_frame, text="RESULTADOS DE CONVERSION", font=("Arial", 20, "bold"))
    resultados_label.pack()

    resultados_text = scrolledtext.ScrolledText(resultados_frame, wrap=tk.WORD, font=("Arial", 30))
    resultados_text.pack(fill=tk.BOTH, expand=True)

    resultados_text.tag_configure("center", justify="center")
    
    # Actualizar resultados antes de mostrarlos
    resultados_conversion = realizarConversiones(resultado_arreglo_operaciones)

    for conversion, resultado in zip(resultado_arreglo_operaciones, resultados_conversion):
        resultados_text.insert(tk.END, f"{conversion}------>{resultado} \n", "center")

    resultados_text.config(state=tk.DISABLED) 

    resultados_window.geometry("700x500")  
    resultados_window.resizable(False, False)
    
# Crear la ventana principal

root = tk.Tk()
root.title("Convertidor de números")


icon_path = "ico/icon.png"
icon = tk.PhotoImage(file=icon_path)
icon_resized = icon.subsample(20)  # Adjust the subsample factor for desired size

# Colocar icono
root.iconphoto(True, icon_resized)

# Crear botones

button_frame = ttk.Frame(root)
button_frame.pack(side="top", fill="x")

lexico_button = tk.Button(button_frame, text="Léxico", command=lambda: mostrar_lexico(tabla_lexica))
sintactico_button = tk.Button(button_frame, text="Desarrolladores", command=mostrar_about)
boton_informacion = tk.Button(button_frame, text="Información Secundaria", command=mostrar_informacion_secundaria)
boton_editar = tk.Button(button_frame, text="Archivo", command=editar_archivo)
boton_mostrar_resultados = tk.Button(button_frame, text="Mostrar Resultados", command=mostrar_resultados_modal)

#Posiciones matriciales de los botones en la ventana principal

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


root.geometry("+400+150") 
root.resizable(False, False)


root.mainloop()