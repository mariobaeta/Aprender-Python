'''

print('-----')
print('SITES')
print('-----')

print()
print()




print('Duolingo Brasileiro')
print('Duolingo Inglês')
print('Duolingo Alemão')

escolha_site = str(input('Escolha qual versão do site do duolingo deseja acessar: '))


if escolha_site == 'Duolingo Brasileiro':
    print('https://pt.duolingo.com/')

elif escolha_site == 'Duolingo Inglês':
    print('https://en.duolingo.com/')
 
elif escolha_site == 'Duolingo Alemão':
    print('https://de.duolingo.com/')

   
'''
'''
import webbrowser

webbrowser.open('https://pt.duolingo.com/')
'''

from tkinter import *

import webbrowser

app = Tk()

frame = Frame(app)
frame.pack()

url = "https://pt.duolingo.com/"

def OpenUrl():
ph    webbrowser.open_new(url)

button = Button(frame, text="Duolingo PT", command=lambda aurl=url:OpenUrl(url))
button.pack(side = "left", padx = 20, pady = 20)

app.mainloop()

