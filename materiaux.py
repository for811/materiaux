__author__ = 'Charli Fortier'
#!/usr/bin/env python

import sys
import os
import time
import pprint

os.system('cls')
print "Programme d'aide au cours de materiaux."
print "Ecole National D'aerotechnique."
print "Polytechnique Montreal."
print ""
time.sleep(1)

##Charli
tc = ["1- Designation des metaux" ,
      "2- Courbe de traction" ,
      "3- Proprietes des materiaux"
      ]
##Marianne
tm = ["1- ..........",
      "2- ..........",
      "3- .........."
      ]

loop = "Y"
name = raw_input("Entrez votre nom: ")
name = name.lower()
if name == "charli" or name == "c":
    os.system('cls')
    print "Bonjour Charli!"
elif name == "marianne" or name == "m":
    os.system('cls')
    print "Bonjour Marianne!"
time.sleep(2)
os.system('cls')

def choose():
    choose = ""
    if name == "charli" or name == "c":
        pprint.pprint(tc)
        choose = tc[(int(raw_input("Selectionner le numero correspondant: "))) - 1]
        os.system('cls')
        return call_theorie(choose)

    elif name == "marianne" or name == "m":
        pprint.pprint(tm)
        choose = tm[(int(raw_input("Selectionner le numero correspondant: "))) - 1]
        os.system('cls')
        return call_theorie(choose)

def call_theorie(choose):
    if name == "charli" or name == "c":
        if choose == tc[0]:
            designation_des_metaux()
            return designation_des_metaux()
        elif choose == tc[1]:
            courbe_de_traction()
            return
        elif choose == tc[2]:
            proprietes_des_metaux()
            return
    elif name == "marianne" or name == "m":
        print "Aucune matiere pour le moment"
        return

def designation_des_metaux():
    choose = ""
    designationmetaux = ["1- Acier au carbone",
                         "2- Acier allie",
                         "3- Acier inox",
                         "4- Alluminum",
                         "5- Alluminum / Traitement thermique"]
    pprint.pprint(designationmetaux)
    choose = designationmetaux[(int(raw_input("Selectionner le numero correspondant: "))) - 1]
    os.system('cls')
    if choose == designationmetaux[0]:
        f = open('commun/designation/acier_carbone.txt')
        file_contents = f.read()
        print (file_contents)
        raw_input("Appuyez sur entrer pour continuer...")
        f.close()
        os.system('cls')
        return
    elif choose == designationmetaux[1]:
        f = open('commun/designation/acier_allier.txt')
        file_contents = f.read()
        print (file_contents)
        raw_input("Appuyez sur entrer pour continuer...")
        f.close()
        os.system('cls')
        return
    elif choose == designationmetaux[2]:
        f = open('commun/designation/acier_inox.txt')
        file_contents = f.read()
        print (file_contents)
        raw_input("Appuyez sur entrer pour continuer...")
        f.close()
        os.system('cls')
        return
    elif choose == designationmetaux[3]:
        f = open('commun/designation/aluminium.txt')
        file_contents = f.read()
        print (file_contents)
        raw_input("Appuyez sur entrer pour continuer...")
        f.close()
        os.system('cls')
        return
    elif choose == designationmetaux[4]:
        f = open('commun/designation/aluminium_ttd.txt')
        file_contents = f.read()
        print (file_contents)
        raw_input("Appuyez sur entrer pour continuer...")
        f.close()
        os.system('cls')
        return
    else:
        print "Oupss.... Ces n/'etait pas un choix..."
        time.sleep(2)
        os.system('cls')
        return designation_des_metaux()


while True: ##Boucle qui repete la sequence
    loop == "Y"
    choose()
    loop = raw_input("Voulez-vous continuer? (Y/N)")
    loop = loop.upper()
    os.system('cls')
    if loop == "Y":
         os.system('cls')
    else:
        exit()
