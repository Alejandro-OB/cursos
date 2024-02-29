"""Juego de piedra papel o tijera"""
import random

options = ('piedra', 'papel', 'tijera')
COMPUTER_WINS = 0
USER_WINS = 0
ROUNDS = 1

while ROUNDS < 6:
    print()
    print('*'*10)
    print(f'Round: {ROUNDS}')
    print('*'*10)

    user_option = input("piedra, papel o tijera => ").lower()

    if not user_option in options:
        print('Opcion invalida')
        continue

    COMPUTER_OPTION = random.choice(options)

    print('Opción elegida: ', user_option)
    print(f'Opción del computador: {COMPUTER_OPTION}')
    print()

    if user_option == COMPUTER_OPTION:
        print("Empate!")
    elif user_option == 'piedra':
        if COMPUTER_OPTION == 'tijera':
            print("Ganaste, tienes un punto")
            print("Piedra gana a tijera")
            USER_WINS += 1
            print()
        else:
            print("Perdiste, papel gana a piedra")
            COMPUTER_WINS += 1
            print()
    elif user_option == 'papel':
        if COMPUTER_OPTION == 'piedra':
            print("Ganaste, tienes un punto")
            print("Papel gana a piedra")
            USER_WINS += 1
            print()
        else:
            print("Perdiste, tijera gana a papel")
            COMPUTER_WINS += 1
            print()
    elif user_option == 'tijera':
        if COMPUTER_OPTION == 'papel':
            print("Ganaste, tienes un punto")
            print("Tijera gana a papel")
            USER_WINS += 1
            print()
        else:
            print("Perdiste, piedra gana a tijera")
            COMPUTER_WINS += 1
            print()
    ROUNDS +=1
    print()
    print(f'Computer wins: {COMPUTER_WINS}')
    print(f'User wins: {USER_WINS}')

    if  COMPUTER_WINS == 3 :
        print('Computer is the Winer!!!')
        break
    if USER_WINS == 3:
        print('User is the winner')
        break

    if ROUNDS > 5:
        print("Game over!!")
        if  COMPUTER_WINS > USER_WINS:
            print('Computer is the Winer!!!')
        elif COMPUTER_WINS < USER_WINS:
            print('User is the Winer!!!')
        else:
            print('JUEGO EMPATADO')
