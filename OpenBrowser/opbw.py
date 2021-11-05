import webbrowser  #Fornece uma interface de alto nível para permitir a exibição de documentos web aos usuaŕios
#fornece interface padrão do Python para o Kit ferramentas gráficas Tk
from tkinter import *

root = Tk()

root.title('Abrir Browser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20)

#chamada do programa
root.mainloop()
