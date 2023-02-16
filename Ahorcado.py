### Proyecto Juego del Ahorcado 

### Ahorcado game es sólo un juego de adivinar palabras adivinando el carácter de la palabra. En este juego, hay una lista de palabras presentes, de las cuales nuestro intérprete elegirá 1 palabra al azar.

# El usuario primero tiene que introducir sus nombres y, a continuación, se le pedirá que adivine cualquier alfabeto. Si la palabra al azar contiene ese alfabeto, se mostrará como la salida (con la colocación correcta) de lo contrario el programa le pedirá que adivine otro alfabeto. Los usuarios dispondrán de 10 turnos (que pueden ser modificados) para adivinar la palabra completa.

### TODO
# Cambia los turnos que quieres dar al jugador
# Cambiar la lista que contiene la lista de palabras secretas
### Proyecto Juego del Ahorcado 

### Ahorcado game es sólo un juego de adivinar palabras adivinando el carácter de la palabra. En este juego, hay una lista de palabras presentes, de las cuales nuestro intérprete elegirá 1 palabra al azar.

# El usuario primero tiene que introducir sus nombres y, a continuación, se le pedirá que adivine cualquier alfabeto. Si la palabra al azar contiene ese alfabeto, se mostrará como la salida (con la colocación correcta) de lo contrario el programa le pedirá que adivine otro alfabeto. Los usuarios dispondrán de 10 turnos (que pueden ser modificados) para adivinar la palabra completa.

### TODO
# Cambia los turnos que quieres dar al jugador
# Cambiar la lista que contiene la lista de palabras secretas

from os import system
import random

def cls():
    system ('cls')

def ahorcado_game():
    cls()
    
    print("\nBienvenido")
    print("Juguemos al ahorcado\n")

    name = input("¿Cuál es tu nombre? ")
    name = name.capitalize()
    print("\nHola " + name + ", Es hora de jugar a Ahorcado")
    print("Empieza a adivinar...")
    guessed_word = []

    # Crea una variable con un valor vacío
    guesses = ""

    # Determinar el número de vueltas
    turns = 15                                 #TODO : Cambia los turnos que quieres dar al jugador

    # Aquí establecemos el Secreto
    words = [
        "Forrest Gump",
        "Atrápame si puedes",
        "Infiltrados",
        "Spiderman",
        "Superman",
        "Arrow",
        "Flash",
        "Guild Wars 2"       
    ]

    word = random.choice(words)
    word = word.upper()

    while turns > 0:
        failed = 0

        for char in word:
            if char in guesses:
                print(char, end=" ")

            elif char == " ":
                print(' / ', end=" ")
                
            else:
                print("_", end=" ")
                failed += 1

        if failed == 0:
            print("\n\n" + name + " ¡GANASTE! :)")
            break

        guess = input("\nAdivina un personaje : ")
        guess = guess.upper()

        if len(guess) > 1:
            break

        guesses += guess
        if (guess not in word) and (guess not in guessed_word):
            turns -= 1
            guessed_word.append(guess)
            print("\nAdivinanza equivocada :/")
        cls()

        print("\nTienes", + turns, "adivinanzas más")
        print("\nSe ha introducido un carácter incorrecto : ", guessed_word)

        if turns == 0:
            print("\nEl juego ha terminado, has perdido :o")

    check = input("\n¿Quieres volver a jugar S/N? ")

    if check == "S" or check == "s" :
        ahorcado_game()


ahorcado_game()