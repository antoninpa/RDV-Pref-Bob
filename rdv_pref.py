#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import smtplib
from bs4 import BeautifulSoup
import requests

user = input('Adresse mail ?')
password = input('Mot de passe pour l\'application ?')

def gmail_sender():
    email_text = """From: %s \nTo: %s  \nSubject: RDV disponible - Pref. Bobigny\n\n RDV Disponile. Suivre : http://www.seine-saint-denis.gouv.fr/booking/create/9829/0""" % (user, user)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, user, email_text)
    except smtplib.SMTPAuthenticationError:
        print("Oups, problem !")

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
parameters = {
    'condition': 'on',
    'nextButton': 'Effectuer+une+demande+de+rendez-vous'
}

while True:
    r = requests.post(
        'http://www.seine-saint-denis.gouv.fr/booking/create/9829/0',
        headers=headers,
        data=parameters
    )
    soup = BeautifulSoup(r.text, 'html.parser')
    form = soup.find(id="FormBookingCreate")
    if form:
        print('Formulaire de RDV indisponible...')
    else:
        gmail_sender()
        print('*'*65+'\n** Formulaire de RDV disponible !! Un mail vous a été envoyé ! **\n'+'*'*65)
        time.sleep(3600.0)
    time.sleep(60.0)
    
