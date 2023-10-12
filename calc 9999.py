from tkinter import *

ventana =Tk()
ventana.title("calculadora")
ventana.configure(bg="white")


#entrada
e_texto = Entry(ventana, font = ("Calibri 20"))
e_texto.configure(bg="pink")
e_texto.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady=5)

i = 0
def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrar():
    e_texto.delete(0,END)
    i = 0
    
def opercacion():
    ecuacion = e_texto.get()
    resulado = eval(ecuacion)
    e_texto.delete(0,END)
    e_texto.insert(0,resulado)

def borrar2 ():
    global i
    i = i-1
    e_texto.delete(i,END)
    
def convertir_hexadecimal():
    try:
        ecuacion = e_texto.get()
        resultado_decimal = eval(ecuacion)
        resultado_hexadecimal = hex(int(resultado_decimal))
        e_texto.delete(0, END)
        e_texto.insert(0, resultado_hexadecimal.upper())
        global i
        i = 0
    except Exception as e:
        messagebox.showerror("Error", "NOPE")
        
def Desactivar_hex_button():
    estado_actual = boton_convertir_hexadecimal.cget('state')
    nuevo_estado = 'normal' if estado_actual == 'disabled' else 'disabled'
    boton_convertir_hexadecimal.configure(state=nuevo_estado)
        


boton1 = Button(ventana, text="1", width=5, height=2, command=lambda:click_boton(1), bg="blue")
boton2 = Button(ventana, text="2", width=5, height=2, command=lambda:click_boton(2))
boton3 = Button(ventana, text="3", width=5, height=2, command=lambda:click_boton(3))
boton4 = Button(ventana, text="4", width=5, height=2, command=lambda:click_boton(4),bg="royal blue")
boton5 = Button(ventana, text="5", width=5, height=2, command=lambda:click_boton(5),bg="blue")
boton6 = Button(ventana, text="6", width=5, height=2, command=lambda:click_boton(6),bg="royal blue")
boton7 = Button(ventana, text="7", width=5, height=2, command=lambda:click_boton(7))
boton8 = Button(ventana, text="8", width=5, height=2, command=lambda:click_boton(8),bg="royal blue")
boton9 = Button(ventana, text="9", width=5, height=2, command=lambda:click_boton(9),bg="blue")
boton0 = Button(ventana, text="0", width=13, height=2, command=lambda:click_boton(0))

boton_borrar = Button(ventana, text="AC", width=5, height=2, command=lambda:borrar(),bg="purple")
boton_Parentesis1 = Button(ventana, text="(", width=5, height=2, command=lambda:click_boton("("))
boton_Parentesis2 = Button(ventana, text=")", width=5, height=2, command=lambda:click_boton(")"),bg="royal blue")
boton_Punto = Button(ventana, text=".", width=5, height=2, command=lambda:click_boton("."))


boton_div = Button(ventana, text="/", width=5, height=2, command=lambda:click_boton("/"),bg="blue" )
boton_mult = Button(ventana, text="x", width=5, height=2, command=lambda:click_boton("*"))
boton_suma = Button(ventana, text="+", width=5, height=2, command=lambda:click_boton("+"))
boton_resta = Button(ventana, text="-", width=5, height=2, command=lambda:click_boton("-"),bg="purple")
boton_igual = Button(ventana, text="=", width=5, height=2, command=lambda:opercacion())
boton_borrar2 = Button(ventana, text= "delete", width=5, height=2, command=lambda:borrar2())
boton_hex= Button(ventana, text=("hx"), width=5, height=2, command=lambda: convertir_hexadecimal())
boton_Desactivar_hex_button = Button(ventana, text= "dis hx", width=5, height=2, command=lambda:Desactivar_hex_button())


boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_Parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_Parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_div.grid(row=1, column=3, padx=5, pady=5)



boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_mult.grid(row=2, column=3, padx=5, pady=5)
boton_hex.grid(row=2, column=4, padx=5, pady=5 )

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_suma.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_resta.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
boton_Punto.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)

boton_hex.grid(row=4, column=5, padx=5, pady=5 )
boton_borrar2.grid(row=3, column=5, padx=5, pady=5)
boton_Desactivar_hex_button.grid(row=2, column=5, padx=5, pady=5)

ventana.mainloop()