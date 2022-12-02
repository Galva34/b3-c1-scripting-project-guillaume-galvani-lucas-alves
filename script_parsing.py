#début script
import csv
table=[]
col_addition = 0
col_addition_2 = 0


#lire le fichier csv source
with open('conso-annuelles.csv', 'r') as f:
    obj = csv.reader(f,delimiter=';')

#extraire données vers fichier csv
    with open('conso-clan.csv', 'w',newline='') as resultat:
        writer = csv.writer(resultat,delimiter=';')

