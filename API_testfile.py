import requests
import xmltodict

station = input("Van welk station wil je de vertrektijden laten zien? ")

api_login = ('rickvlot@hotmail.com', 'kDQOe1pgLOtJXaMMGoieVGrSKQcffSG1sYyrD3GSxCV0wfN_lIkTIA')
api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + station
response = requests.get(api_url, auth=api_login)

vertrekXML = xmltodict.parse(response.text)

print('Dit zijn de vertrekkende treinen:')
for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
    eindbestemming = vertrek['EindBestemming']

    vertrektijd = vertrek['VertrekTijd']    # 2016-09-27T18:36:00+0200
    vertrektijd = vertrektijd[11:16]        # 18:36
    vertrekspoor = str(vertrek['VertrekSpoor']['#text'])
    vervoerder = vertrek['Vervoerder']
    treintype = vertrek['TreinSoort']
    print('Om '+vertrektijd+' vertrekt een '+treintype+' van '+vervoerder+' naar '+eindbestemming+' vanaf spoor '+vertrekspoor)
