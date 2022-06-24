import tkinter

def CelsiusToFahrenheit(Celsius, entry):
    Fahrenheit = 9.0/5.0 * float (Celsius) + 32
    entry.delete(0, 'end')
    entry.insert (0, str(Fahrenheit))
    
def FahrenheitToCelsius(Fahrenheit, entry):
    Celsius = (float (Fahrenheit)- 32) * 5.0/9.0
    entry.delete(0, 'end')
    entry.insert(0, str(Celsius))

def main():
    window = tkinter.Tk()
    window.geometry("250x200")
    
    window.title('Grid')
    lb  = tkinter.Label(window, text= 'Fahrenheit')
    lb.grid(row=0, column=0)
    
    lb1= tkinter.Label (window, text = 'Celsius')
    lb1.grid(row=0, column=1)
    
    en = tkinter.Entry(window, justify='right')
    en.grid(row=1, column=0)
    en.insert(0,'32.0')
    
    en1 = tkinter.Entry(window, justify= 'right')
    en1.grid(row=1, column=1)
    en1.insert(0, 0.0)
    
    btnFtoC = tkinter.Button(window, text='>>>>', command=lambda: FahrenheitToCelsius(en.get(), en1))
    btnFtoC.grid(row=2, column=0)
    btnCtoF = tkinter.Button(window, text='<<<<', command=lambda: CelsiusToFahrenheit(en1.get(), en))
    btnCtoF.grid(row=2, column=1)
    
    
    
    window.mainloop()

run = main()

if __name__ == '__main__':
    run