from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('File Counter')
root.geometry('500x500')
color = 'gray'
root.configure(bg=color)

count_result = dict()

def count_text(file):
    file_open = open(str(file),'r')
    full_text = file_open.readlines()
    file_open.close()

    for word in word_list.get().split(', '): # A quantidade de laços será a mesma quantidade de palavras que eu colocar para o programa pesquisar.
        for text in full_text: # Para cada palavra que ele encontrar no texto
            if word in count_result: # Se eu digitei a palavra no software, mostre ela e quantas vezes ela apareceu.
                count_result[word] = count_result[word] + text.count(word)
            else:
                count_result[word] = text.count(word)
    #print(count_result)
    answer.delete('1.0',END)  #Impede que as palavras que são mostradas no Text apareçam mais de uma vez toda vida que apertar o botão Count Words. É colocado aqui em cima porque ele zera o answer para o novo loop.
    #Mostrando quantidade de palavras no Text
    for k, v in count_result.items():
        answer.insert('1.0','{0} {1} \n'.format(k,v))
    count_result.clear()

def open_file():
    root.filename = filedialog.askopenfilename()

def clear_text():
    word_list.delete(0, END)
    answer.delete('1.0',END)

word_list = Entry(root, width=63)
word_list.place(x=0,y=0)

#highlightbackground
file = Button(root, text='Select file',width=60, highlightbackground=color,
              command= lambda : open_file())
file.place(x=0,y=30)

count = Button(root, text='Count Words',width=60, highlightbackground=color,
               command = lambda : count_text(root.filename))
count.place(x=0,y=60)

clear = Button(root, text='Clear Text',width=60, highlightbackground=color,
               command=lambda : clear_text())
clear.place(x=0,y=90)

answer = Text(root, height=300,width=500,bg=color)
answer.place(x=0,y=120)


root.mainloop()