from tkinter import *
import requests
import xmltodict
import tkinter.messagebox
import tkinter.font



root = Tk()
root.config(bg="#FFCC18")  # Opmaak van GUI, Gijs Willemse 3-11-2016
root.wm_title("NS Actuele Vertrektijden")
root.iconbitmap(r'C:\Users\Gebruiker\Downloads\nsiconbmp.bmp')

def api(station):  # Gemaakt door Rick Vlot, modified by Rick Vlot 3-11-2016
    station = e.get()
    text.config(state=NORMAL)
    text.delete('1.0', 'end')
    api_login = ('rickvlot@hotmail.com', 'kDQOe1pgLOtJXaMMGoieVGrSKQcffSG1sYyrD3GSxCV0wfN_lIkTIA')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + str(station)
    response = requests.get(api_url, auth=api_login)

    vertrekXML = xmltodict.parse(response.text)

    text.insert('1.0', 'Dit zijn de vertrekkende treinen:' + '\n')
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']

        vertrektijd = vertrek['VertrekTijd']    # 2016-09-27T18:36:00+0200
        vertrektijd = vertrektijd[11:16]        # 18:36
        vertrekspoor = str(vertrek['VertrekSpoor']['#text'])
        treintype = vertrek['TreinSoort']

        text.insert('end', 'Om '+vertrektijd+' vertrekt een '+treintype+' naar '+eindbestemming+' vanaf spoor '+vertrekspoor + '\n')
    text.config(state=DISABLED)



label1 = Label(text="Vul hier het station in waarvan u de reisinformatie wilt opvragen: ", bg="#FFCC18")
label1.pack(side=TOP)

e = Entry(root, font="Arial", width=37)
e.bind("<Return>", api)
e.pack()

photo = PhotoImage(file="nspoep.png")  # NS Logo toegevoegd Gijs Willemse 3-11-2016

label = Label(image=photo)  # NS Plaatje toegevoegd Doeke Roos, Gijs Willemse 3-11-2016
label.pack(side=BOTTOM)

text = Text(root, width=70, height=25, bg="#FFCC18")
text.config(state=DISABLED)
text.config(font=("Arial", 12,))
text.pack()


root.mainloop()
