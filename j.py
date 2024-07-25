import tkinter
import base64
import tkinter as tk
from tkinter import messagebox

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def save():
    text=inputSecret.get("1.0",tk.END)
    tit=inputTitle.get()
    ke=inputKey.get()

    if len(text)==0 or len(tit)==0 or len(ke)==0:
        messagebox.showinfo(title="HATA",message="LÜTFEN BİLGİLERİNİZİ TAM GİRİNİZ")
    
    else:
        message_descrypt=encode(ke,text)

        try:
            with open ("mySecr.txt","a") as data_file:
                data_file.write(f'\n{tit}\n{message_descrypt}')

        except FileNotFoundError:
            with open ("mySecr.txt","w") as data_file:
                data_file.write(f'\n{tit}\n{message_descrypt}')
        
        finally:
            inputKey.delete(0,tk.END)
            inputSecret.delete("1.0",tk.END)
            inputTitle.delete(0,tk.END)

def descrypt():
    mesa=inputSecret.get("1.0",tk.END)
    ke=inputKey.get()

    if len(mesa)==0 or len(ke)==0:
        messagebox.showerror(title="HATA",message="LÜTFEN BİLGİLERİNİZİ TAM GİRİNİZ")
    
    else:
        try:    
                descry=decode(ke,mesa)
                inputSecret.delete("1.0",tk.END)
                inputSecret.insert("1.0",descry)

        except:
                messagebox.showinfo(title="HATA",message="LÜTFEN BİLGİLERİNİZİ TAM GİRİNİZ")

window=tkinter.Tk()

canva=tkinter.Canvas()
logo=tkinter.PhotoImage(file="RandomPhoto.png")
canva.create_image(200,200,image=logo)
canva.pack()

title=tkinter.Label(text="enter your title")
title.pack()

inputTitle=tkinter.Entry(width=30)
inputTitle.pack()

secret=tkinter.Label(text="enter your message")
secret.pack()

inputSecret=tkinter.Text(width=30,height=10)
inputSecret.pack()

key=tkinter.Label(text="enter your master key")
key.pack()

inputKey=tkinter.Entry(width=30)
inputKey.pack()

saveButton=tkinter.Button(text="SAVE",command=save)
# command
saveButton.pack()

descryp=tkinter.Button(text="DESCRYPT",command=descrypt)
# command
descryp.pack()


window.mainloop()