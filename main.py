import pygame
import sys
import random

# Inicializa pygame
pygame.init()

# Configura la ventana
screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption("Juego de Ahorcado")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

imagen_ahorcado = [
    pygame.transform.scale(pygame.image.load("imagenes/estructura.jpg"), (200, 300)),
    pygame.transform.scale(pygame.image.load("imagenes/cabeza.jpg"), (200, 300)),
    pygame.transform.scale(pygame.image.load("imagenes/torso.jpg"), (200, 300)),
    pygame.transform.scale(pygame.image.load("imagenes/brazoderecho.jpg"), (200, 300)),
    pygame.transform.scale(pygame.image.load("imagenes/brazoizquierdo.jpg"), (200, 300)),
    pygame.transform.scale(pygame.image.load("imagenes/piernaderecha.jpg"), (200, 300)),
    pygame.transform.scale(pygame.image.load("imagenes/piernaizquierda.jpg"), (200, 300)),
    pygame.transform.scale(pygame.image.load("imagenes/etapafinal.jpg"), (200, 300)),
]

# Lista de palabras para adivinar
palabras = [
    "algebra", "geometria", "trigonometria", "calculo", "estadistica", 
    "probabilidad", "ecuacion", "funcion", "variable", "constante", 
    "numero", "integral", "derivada", "vector", "matriz", "poligono", 
    "angulo", "circunferencia", "area", "volumen", "teoria", "teorema", 
    "recta", "pendiente", "logaritmo", "exponente", "limite", "secante", 
    "coseno", "tangente"
]

# Escoge una palabra aleatoria
palabra_secreta = random.choice(palabras)
palabra_adivinada = ['_'] * len(palabra_secreta)

# Número de intentos fallidos (cambia a 8)
intentos_fallidos = 0

# Fuente para el texto
font = pygame.font.Font(None, 36)

# Función para dibujar la palabra adivinada
def dibujar_palabra():
    texto = font.render(' '.join(palabra_adivinada), True, WHITE)
    screen.blit(texto, (300, 50))

# Función para dibujar las letras del abecedario
def dibujar_abecedario():
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, letra in enumerate(abecedario):
        x = 50 + (i % 13) * 50  # Posición en X
        y = 500 + (i // 13) * 50  # Posición en Y
        letra_texto = font.render(letra, True, WHITE)
        screen.blit(letra_texto, (x, y))

# Función para manejar los intentos fallidos
def manejar_intentos_fallidos():
    global intentos_fallidos
    if intentos_fallidos < len(imagen_ahorcado):
        screen.blit(imagen_ahorcado[intentos_fallidos], (100, 100))

# Bucle principal del juego
running = True
while running:
    # Detecta eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key >= pygame.K_a and event.key <= pygame.K_z:
                letra = chr(event.key)  # Convierte la tecla a letra (por ejemplo, pygame.K_a -> 'a')
                
                # Verifica si la letra está en la palabra secreta
                if letra in palabra_secreta:
                    for i in range(len(palabra_secreta)):
                        if palabra_secreta[i] == letra:
                            palabra_adivinada[i] = letra
                else:
                    # Si la letra no está en la palabra secreta, aumenta los intentos fallidos
                    intentos_fallidos += 1

    # Rellena la pantalla con el color de fondo
    screen.fill(BLACK)

    # Dibuja la imagen del ahorcado según los intentos fallidos
    manejar_intentos_fallidos()

    # Dibuja la palabra adivinada
    dibujar_palabra()

    # Dibuja el abecedario
    dibujar_abecedario()

    # Actualiza la pantalla
    pygame.display.flip()

    # Condición de victoria
    if '_' not in palabra_adivinada:
        print("¡Ganaste! La palabra era:", palabra_secreta)
        running = False

    # Condición de derrota
    if intentos_fallidos >= len(imagen_ahorcado):
        print("¡Perdiste! La palabra era:", palabra_secreta)
        running = False

# Cierra pygame
pygame.quit()
sys.exit()
