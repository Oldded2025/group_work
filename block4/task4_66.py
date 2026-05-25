dlina_stola = int(input("Введите целое число dlina_stola:"))
shirina_stola = int(input("Введите целое число shirina_stola:"))
dlina_domino = int(input("Введите целое число dlina_domino:"))
shirina_domino = int(input("Введите целое число shirina_domino:"))
tolshina_domino = int(input("Введите целое число tolshina_domino:"))
# num1 = dlina_stola/shirina_domino
# num2 = shirina_stola/dlina_domino
# num3 = dlina_stola/tolshina_domino
# print(num1, num2,num3)
sluchai1 = (dlina_stola//shirina_domino) *(shirina_stola//dlina_domino)
print(sluchai1)
sluchai2 = (dlina_stola//shirina_domino) *(shirina_stola//dlina_domino)
print(sluchai2)
sluchai3 = (dlina_stola//tolshina_domino) *(shirina_stola//dlina_domino)
print(sluchai3)
sluchai4 = (dlina_stola//dlina_domino) *(shirina_stola//tolshina_domino)
print(sluchai4)