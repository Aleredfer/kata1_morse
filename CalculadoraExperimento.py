from tkinter import *
from tkinter import ttk

class Calculadora(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height=kwargs["height"], width=kwargs["width"])

        #Entrada:
        self.caracter = IntVar()
        self.entrada_entry = ttk.Entry(self, width=15, textvariable=self.caracter)
        self.entrada_entry.place(x=90, y=10)
        
        #Salida:

        
        self.salida_text = Text(self, width=10, height=1)
        self.salida_text.place(x=0, y=10)
        

        

        #Números:
        uno_lbl = ttk.Label(self, text="1", width=3, anchor=CENTER)
        uno_lbl.place(x=10, y=85)

        dos_lbl = ttk.Label(self, text="2", width=3, anchor=CENTER)
        dos_lbl.place(x=50, y=85)

        tres_lbl = ttk.Label(self, text="3", width=3, anchor=CENTER)
        tres_lbl.place(x=90, y=85)
        
        cuatro_lbl = ttk.Label(self, text="4", width=3, anchor=CENTER)
        cuatro_lbl.place(x=10, y=125)

        cinco_lbl = ttk.Label(self, text="5", width=3, anchor=CENTER)
        cinco_lbl.place(x=50, y=125)

        seis_lbl = ttk.Label(self, text="6", width=3, anchor=CENTER)
        seis_lbl.place(x=90, y=125)
        
        siete_lbl = ttk.Label(self, text="7", width=3, anchor=CENTER)
        siete_lbl.place(x=10, y=165)

        ocho_lbl = ttk.Label(self, text="8", width=3, anchor=CENTER)
        ocho_lbl.place(x=50, y=165)

        nueve_lbl = ttk.Label(self, text="9", width=3, anchor=CENTER)
        nueve_lbl.place(x=90, y=165)

        #btn_send = ttk.Button(self, command=self.send_telegram, text="Send")
        #Símbolos:
        pinta_lbl = ttk.Button(self, command=self.pintar, text="pinta")
        pinta_lbl.place(x=25, y=180)
        
        div_lbl = ttk.Label(self, text="/", width=3, anchor=CENTER)
        div_lbl.place(x=130, y=45)

        mult_lbl = ttk.Label(self, text="*", width=3, anchor=CENTER)
        mult_lbl.place(x=130, y=85)
        
        sum_lbl = ttk.Label(self, text="+", width=3, anchor=CENTER)
        sum_lbl.place(x=130, y=125)
        
        rest_lbl = ttk.Label(self, text="-", width=3, anchor=CENTER)
        rest_lbl.place(x=130, y=165)

        borrar_lbl = ttk.Button(self, text="Delete", command=self.borrado)
        borrar_lbl.place(x=10, y=45)

        igual_lbl = ttk.Label(self, text="=", width=3, anchor=CENTER)
        igual_lbl.place(x=90, y=45)

    def pintar(self):
        self.traduccion = self.caracter.get()
        self.salida_text.insert(INSERT, self.traduccion)
        self.entrada_entry.delete("1.0", END)

    #def sumar(self):
        #Numeros = self.caracter.get()
        
    def borrado(self):
        self.salida_text.delete("1.0", END)
        

        





class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calculadora")
        self.geometry("180x300")

        self.calculadora = Calculadora(self, height=300, width=180)

    def start(self):
        self.mainloop()

if __name__ == "__main__":
    miCalculadora = MainApp()
    miCalculadora.calculadora.place(x=10, y=10)
    miCalculadora.start()