from tkinter import *
import requests
import xmltodict



def api(station):
    """Return train information from the NS

    Return from API:

        Eindbestemming
        Vertrektijd
        Vertrekspoor
        Treinsoort
    """
    station = e.get()
    text.config(state=NORMAL)
    text.delete('1.0', 'end')
    api_login = ('rickvlot@hotmail.com', 'kDQOe1pgLOtJXaMMGoieVGrSKQcffSG1sYyrD3GSxCV0wfN_lIkTIA')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + str(station)
    response = requests.get(api_url, auth=api_login)

    vertrekXML = xmltodict.parse(response.text)

# Schrijf een try-exept om fouten te kunnen voorkomen
    try:
        for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:

            eindbestemming = vertrek['EindBestemming']

            vertrektijd = vertrek['VertrekTijd']
            vertrektijd = vertrektijd[11:16]
            vertrekspoor = str(vertrek['VertrekSpoor']['#text'])
            treintype = vertrek['TreinSoort']

            text.insert('end', 'Om '+vertrektijd+' vertrekt een '+treintype+' naar '+eindbestemming+' vanaf spoor '+vertrekspoor + '\n')
        text.config(state=DISABLED)
    except KeyError:
        text.insert('1.0', 'Dit station bestaat niet.' + '\n')
        text.insert('1.0', 'Voer a.u.b een bestaand station in.' + '\n')

# Maak met behulp van Tkinter een interface-scherm
root = Tk()
root.config(bg="#FFCC18")
root.wm_title("NS Actuele Vertrektijden")

# Maak een textbox aan waarin men een station in kan voeren
label1 = Label(text="Vul hier het station in waarvan u de reisinformatie wilt opvragen: ", bg="#FFCC18")
label1.pack(side=TOP)

e = Entry(root, font="Arial", width=37)
e.bind("<Return>", api)
e.pack()

# Voeg een plaatje van het NS-logo toe
photo = PhotoImage(file="nspoep.png")
label = Label(image=photo)
label.pack(side=BOTTOM)

# Codeer hoe de tekst eruit moet zien die verschijnt op het beeldscherm
text = Text(root, width=70, height=25, bg="#FFCC18")
text.config(state=DISABLED)
text.config(font=("Arial", 12,))
text.pack()

root.mainloop()
