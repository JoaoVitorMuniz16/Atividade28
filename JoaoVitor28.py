from datetime import date
atual = date.today().year
counter_young = 0
counter_adult = 0
for i in range(7):
    num = int(input("Digite anos de nascimento: \n"))
    if atual - num >= 21:
        counter_adult += 1
    elif atual - num < 21:
        counter_young += 1
print("Ao todo tivemos {} maiores e {} menores de idade.".format(
    counter_adult, counter_young))