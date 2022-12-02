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
        
#Supprimer les lignes avec des cellules vides pour se faire on va faire
#une première boucle pour lire tout la tableau puis une seconde pour faire
#cellule par cellule, si il trouve une case vide on supprimera la ligne
#On va également supprimer la ligne ID logement avec le writerow
                
        for l in obj:
            vide = False
            for i in range(len(l)):

                if l[i] == None or l[i] == '':
                    vide = True
                    break
            if not vide:
                writer.writerow([l[0], l[2], l[3], l[4]])


#Reouvre le fichier après modificiation
f= open (r"output.csv")
myReader = csv.reader(f,delimiter=';')

#Lecture du CSV dans un tableau
for row in myReader:
    table.append(row)
    
#On sélectionner les colonnes désirés pour l'addition
col_2 = [i[2] for i in table]
col_1 = [i[1] for i in table]

