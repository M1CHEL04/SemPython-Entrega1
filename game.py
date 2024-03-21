import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de fallos permitidos
max_failures = 10
#Cantidad de fallos actuales
current_failures=0
# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

#seleccion de la dificultad
difficulty=input("Ingrese la dificultad: \nFacil. \nMedia. \nDificil. \n").lower()

if difficulty == 'facil':
    #se muestran todas las vocales
    cad= []
    for aux in secret_word:
        if(aux== "a")or(aux=="e")or(aux=="i")or(aux=="o")or(aux=="u")or(aux=="ó"):
            guessed_letters.append(aux)
            cad.append(aux)
        else:
            cad.append("_")
    word_displayed="".join(cad)
elif difficulty == 'media':
    #se muestran solo la primera y la ultima letra
    word_displayed= (secret_word[0]+(len(secret_word)-2)*"_"+secret_word[len(secret_word)-1])
    guessed_letters.append(secret_word[0])
    guessed_letters.append(secret_word[len(secret_word)-1])
else:
    #no se muestra nada
    word_displayed= "_" * len(secret_word)

# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

while (current_failures != max_failures):
     # Pedir al jugador que ingrese una letra
     letter = input("Ingresa una letra: ").lower()
     # Verificar si la letra ya ha sido adivinada
     if letter in guessed_letters:
         print("Ya has intentado con esa letra. Intenta con otra.")
         current_failures+= 1
         continue
     # Agregar la letra a la lista de letras adivinadas
     if letter == "":
         print("Error detectado: caracter no valido")
         current_failures+=1
         continue
     guessed_letters.append(letter)
     # Verificar si la letra está en la palabra secreta
     if letter in secret_word:
         print("¡Bien hecho! La letra está en la palabra.")
     else:
         print("Lo siento, la letra no está en la palabra.")
         current_failures+=1
     # Mostrar la palabra parcialmente adivinada
     letters=[]
     for letter in secret_word:
         if letter in guessed_letters:
             letters.append(letter)
         else:
             letters.append("_")
     word_displayed = "".join(letters)
     print(f"Palabra: {word_displayed}")
     # Verificar si se ha adivinado la palabra completa
     if word_displayed == secret_word:
         print(f"¡Felicidades! Has adivinado la palabra secreta:  {secret_word}")
         break
else:
    print(f"¡Oh no! Has alcanzado los {max_failures} fallos.")
    print(f"La palabra secreta era: {secret_word}")

#Condiciones:
    #El programa distingue letras con o sin acento, por lo tanto si la letra va con acento y lo pones sin, contara como error.
    #En la modalidad "media" si se llega a dar el caso de que se repetie la primera o la ultima letra a lo largo de la palabra, se tomaran como letras adivinadas y las imprimira en el siguiente intento.