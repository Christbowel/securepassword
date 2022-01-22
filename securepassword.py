import random
import datetime

 
size =int(input("entrer le nombre de caractere du mot de passe dont vous souhaitez obtenir :  "))
char = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ@#€&$_"
   
for i in range(1, size):
   password = random.choice(char)
   print (password)



print ("lire le mot de passe verticalement!!!")


print (datetime.datetime.now())

print ("MERCI D'AVOIR UTILISE CET OUTIL...")


input("apuyer sur entrer pour quitter...")
print ("sortie encours..............")
exit()
