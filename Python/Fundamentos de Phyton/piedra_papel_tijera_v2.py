print('BIENVENIDO AL JUEGO DE PIEDRA, PAPEL O TIJERA\n')

player_one_name = input('Jugador 1, Ingresa tu nombre: ')
player_two_name = input('Jugador 2, Ingresa tu nombre: ')
rounds = 0
player_one_win = 0
player_two_win = 0

while rounds < 5:
    player_one_option = input(f"{player_one_name} Ingresa la opción: Piedra, Papel o Tijera: ").lower()
    player_two_option = input(f"{player_two_name} Ingresa la opción: Piedra, Papel o Tijera: ").lower()

    if player_one_option == player_two_option:
        print('EMPATE!!!!')
    elif player_one_option == 'piedra' and player_two_option == 'tijera':
        print(f'el jugador {player_one_name} gana')
        player_one_win += 1

    elif player_one_option == 'piedra' and player_two_option == 'papel':
        print(f'el jugador {player_two_name} gana')
        player_two_win += 1

    elif player_one_option == 'tijera' and player_two_option == 'piedra':
        print(f'el jugador {player_two_name} gana')
        player_two_win += 1

    elif player_one_option == 'tijera' and player_two_option == 'papel':
        print(f'el jugador {player_one_name} gana')
        player_one_win += 1

    elif player_one_option == 'papel' and player_two_option == 'tijera':
        print(f'el jugador {player_two_name} gana')
        player_two_win += 1

    elif player_one_option == 'papel' and player_two_option == 'piedra':
        print(f'el jugador {player_one_name} gana')
        player_one_win += 1

    else:
        print('opción invalida')

    rounds += 1

if player_two_win > player_one_win:
    print(f"{player_two_name} GANÓ!!!")
elif player_two_win < player_one_win:
    print(f"{player_one_name} GANÓ!!!")
else:
    print("Nadie ganó, EMPATE!!")


