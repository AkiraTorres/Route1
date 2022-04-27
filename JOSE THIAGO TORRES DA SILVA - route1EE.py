from os import system
from random import randint, choice

mapa = [
    ["A", "A", "A", "A", "A", "", "", "A", "A", "A", "A", "A"],
    ["A", "", "", "", "", "", "", "", "", "", "", "A"],
    ["A", "", "", "", "A", "", "", "", "", "", "", "A"],
    ["A", "E", "E", "E", "A", "E", "E", "E", "G", "G", "G", "A"],
    ["A", "", "", "", "A", "G", "G", "G", "G", "G", "G", "A"],
    ["A", "E", "E", "E", "A", "G", "G", "G", "G", "G", "G", "A"],
    ["A", "", "", "", "", "", "", "", "", "", "", "A"],
    ["A", "", "", "", "", "", "", "", "G", "G", "G", "A"],
    ["A", "A", "E", "E", "E", "A", "A", "A", "G", "G", "G", "A"],
    ["A", "", "", "", "", "", "", "", "", "", "", "A"],
    ["A", "E", "", "E", "E", "", "E", "E", "E", "E", "E", "A"],
    ["A", "", "", "", "", "", "", "", "", "", "", "A"],
    ["A", "", "", "", "", "", "", "", "", "", "", "A"],
    ["A", "A", "A", "A", "A", "A", "G", "G", "G", "E", "E", "A"],
    ["A", "", "", "", "", "", "G", "G", "G", "", "", "A"],
    ["A", "", "", "", "", "", "", "", "", "", "", "A"],
    ["A", "E", "E", "", "", "E", "E", "E", "E", "E", "E", "A"],
    ["A", "", "G", "G", "G", "G", "", "", "G", "G", "G", "A"],
    ["A", "G", "G", "G", "", "", "", "G", "G", "", "", "A"],
    ["A", "A", "A", "A", "A", "A", "G", "A", "A", "A", "A", "A"],
]


# pokemons possíveis de serem encontrados na grama
possiblePokes = [
    "Ratata",
    "Pidgey",
    "Weedle",
    "Caterpie",
    "Paras",
    "Charmander",
    "Bulbasaur",
    "Squirtle",
    "Pikachu",
    "Eevee",
]


pokedex = {}


# variável contendo a posição inicial do jogador
playerPosition = [19, 6]


# retorna um valor aleatório de 0 até o valor passado como parâmetro
def aleatorio(valor):
    return randint(0, valor)


# imprime o menu detalhando as opções disponíveis do menu principal
def printMenu():
    print(
        "9 - Para abrir esse menu\n8 - Subir\n2 - Descer\n4 - Ir para esquerda\n6 - Ir para direita\n5 - Abrir Pokedex"
    )
    print("0 - Sair do Jogo")


# função para realizar o encontro com um pokemon selvagem e registrá-lo na pokedex se assim desejado
def pokemonEncounter():
    print("Um pokemon selvagem apareceu!")
    n = input("Capturar ou correr?[1-Capturar ou 2-Correr: ")
    while n != "1" and n != "2":
        n = input("Digite uma opção válida: ")
    if n == "1":
        pokemon = choice(possiblePokes)
        if pokemon in pokedex:
            print("Esse Pokemon já está salvo na pokedex.")
        else:
            pokeStatus = {
                "HP": aleatorio(100),
                "Atk": aleatorio(100),
                "Def": aleatorio(100),
                "Sp. Atk": aleatorio(100),
                "Sp. Def": aleatorio(100),
                "Speed": aleatorio(100),
            }
            pokedex[pokemon] = pokeStatus
    elif n == "2":
        print("Fujão")

    if len(pokedex) == 10:
        system("clear")
        print("Parabéns! Você completou a pokedex.")
        exit()


# função para verificar se o espaço ao qual o jogador deseja se mover está válido ou não
def validateMapSpace(command):
    row, column = playerPosition[0], playerPosition[1]
    position = [0, 0]

    try:
        if command == "8":
            mapSpace = mapa[row - 1][column]
            position[0] = -1
        elif command == "2":
            mapSpace = mapa[row + 1][column]
            position[0] = 1
        elif command == "4":
            mapSpace = mapa[row][column - 1]
            position[1] = -1
        elif command == "6":
            mapSpace = mapa[row][column + 1]
            position[1] = 1

        return [position, mapSpace]
    except Exception:
        print("Game over")
        exit()


# função para mover o jogador e - caso ele pise na grama - possibilita o encontro com um pokemon selvagem
def movePlayer(command):
    position, mapSpace = validateMapSpace(command)

    if mapSpace == "":
        playerPosition[0] += position[0]
        playerPosition[1] += position[1]
    elif mapSpace == "A" or (mapSpace == "E" and command != "2"):
        print("Bump!")
    elif mapSpace == "E" and command == "2":
        playerPosition[0] += position[0]
        playerPosition[1] += position[1]
    elif mapSpace == "G":
        playerPosition[0] += position[0]
        playerPosition[1] += position[1]

        if aleatorio(100) >= 50:
            pokemonEncounter()


# função para validar as entradas dos menus
def validateMenuInput(command, pokedex=False):

    if pokedex == True:
        command = input("Escolha uma ação: ")
        while command != "1" and command != "2" and command != "0":
            command = input("Escolha uma ação: ")
    else:
        command = input("Insira um comando: ")
        while (
            command != "9"
            and command != "0"
            and command != "5"
            and command != "2"
            and command != "4"
            and command != "6"
            and command != "8"
        ):
            command = input("Insira um comando: ")
    return command


# função para gerenciar as operações com a pokedex
def openDex():
    command = ""
    savedPokes = list(pokedex.keys())
    for pokemon in savedPokes:
        print(f"{pokemon} ", end="")
    print("\nDigite")
    print(
        "1 para Listar Detalhes\n2 para Apagar Registro\n0 para voltar ao menu principal"
    )

    while command != "0":
        command = validateMenuInput(command, True)

        if command == "1":
            pokemon = input("Digite o nome do pokemon para ver os detalhes: ")

            if pokemon in pokedex:
                stats = pokedex[pokemon]
                print(f"\nHP: {stats['HP']}")
                print(f"Atk: {stats['Atk']}")
                print(f"Def: {stats['Def']}")
                print(f"Sp. Atk: {stats['Sp. Atk']}")
                print(f"Sp. Def: {stats['Sp. Def']}")
                print(f"Speed: {stats['Speed']}\n")
            else:
                print("Pokemon não registrado.\n")

        elif command == "2":
            pokemon = input(
                "Digite o nome do pokemon para deletar o seu registro da pokedex: "
            )

            if pokemon in pokedex:
                pokedex.pop(pokemon)
                print("Pokemon deletado da pokedex.")
            else:
                print("Pokemon não registrado.\n")


# menu inicial
def menu():
    system("clear")
    print("Bem-vindo!\nA qualquer momento você pode escolher uma das opções:")
    printMenu()
    print("Entrando na Rota 1")
    command = ""
    while command != "0":
        print(f"\nSua posição atual: {playerPosition}")
        command = validateMenuInput(command)
        if command == "9":
            printMenu()
        elif command == "8" or command == "2" or command == "4" or command == "6":
            movePlayer(command)
        elif command == "5":
            system("clear")
            openDex()
            system("clear")
        elif command == "0":
            system("clear")
            print("Fim de Jogo.")
        else:
            print("Comando inválido.")


if __name__ == "__main__":
    menu()
