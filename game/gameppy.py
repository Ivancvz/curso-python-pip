import random
print('Bienvenido al juego, tus opciones son: ')
options = ['Piedra', 'Papel', 'Tijera']
n = 1
for option in options:
    print(str(n) + '. '+ option)
    n = n+1
print()
print('Las reglas son las siguiente:')
print('- '+options[0]+' le gana a '+options[2])
print('- '+options[1]+' le gana a '+options[0])
print('- '+options[2]+' le gana a '+options[1])
print()

point_user = 0
point_computer = 0

while abs(point_user - point_computer) < 2: 
    user_option = int(input('Elige tu opción 1, 2 o 3: '))-1
    print('Elegiste '+options[user_option])
    computer_option = random.randint(0,2)
    print('La computadora eligió '+options[computer_option])
    print()
    if user_option == computer_option:
        print('Empate')
    elif user_option - computer_option == 1:
        print('Ganaste!')
        point_user = point_user+1
    elif computer_option - user_option == 2:
        print('Ganaste !')
        point_user = point_user+1
    else:
        print('Perdiste, aún puedes')
        point_computer = point_computer+1
    print()
    print('Puntos: '+str(point_user))
    print('Puntos: '+str(point_computer))
print()

if point_user>point_computer:
    print('Ganaste el juego')
else:
    print('Ganó la computadora')