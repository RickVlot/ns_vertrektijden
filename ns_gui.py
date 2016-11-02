from tkinter import *
import requests
import xmltodict
import tkinter.messagebox
import tkinter.font

root = Tk()
root.config(bg="yellow")

def api(station): # Gemaakt door Rick Vlot, modified by Gijs Willemse 2-11-2016
    station = e.get()
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

        text.insert('end', 'Om '+vertrektijd+' vertrekt een trein naar '+eindbestemming + '\n')
    return


e = Entry(root, font="Arial")
e.bind("<Return>", api)
e.pack()

text = Text(root, width=60, height=30, bg="yellow", font="Arial" )
text.pack()

root.mainloop()
