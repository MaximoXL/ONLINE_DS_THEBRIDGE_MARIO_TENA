import numpy as np
import random

# Definir constantes
celda_vacia = "-"
celda_barco = "O"
celda_disparo = "X"
celda_agua = "~"
list_orientacion = ["N", "S", "E", "O"]


class Tablero:
    def __init__(self, id_jugador):
        """Constructor de la clase Tablero."""
        self.id_jugador = id_jugador  # ID del jugador (0 para jugador humano, 1 para la máquina)
        # Inicializa un tablero de 10x10
        self.tablero = np.full((10, 10), celda_vacia)
        self.coordenadas_barcos = []  # Lista para almacenar las coordenadas de los barcos
        # Lista para almacenar las coordenadas de los disparos
        self.coordenadas_disparos = []

    def coloca_barco_plus(self, barco):
        """
        Coloca un barco en el tablero si cabe.
        Retorna True si el barco se coloca correctamente, False si no cabe.
        """
        for fila, columna in barco:
            if fila < 0 or fila >= self.tablero.shape[0] or columna < 0 or columna >= self.tablero.shape[1]:
                return False  # Si el barco se sale del tablero
            if self.tablero[fila, columna] != celda_vacia:
                return False  # Si la celda ya está ocupada
        # Colocar el barco
        for fila, columna in barco:
            self.tablero[fila, columna] = celda_barco
        # Almacena las coordenadas del barco
        self.coordenadas_barcos.extend(barco)
        return True

    def crea_barco_aleatorio(self, eslora=4, num_intentos=100):
        """
        Crea un barco aleatorio en el tablero.
        Si no puede colocarse después de 'num_intentos', retorna False.
        """
        num_max_filas = self.tablero.shape[0]
        num_max_columnas = self.tablero.shape[1]

        for intento in range(num_intentos):
            barco = []
            pieza_original = (random.randint(0, num_max_filas - 1),
                              random.randint(0, num_max_columnas - 1))
            orientacion = random.choice(list_orientacion)

            fila, columna = pieza_original
            barco.append(pieza_original)

            # Generamos las celdas del barco según la orientación
            for i in range(eslora - 1):
                if orientacion == "N":
                    fila -= 1
                elif orientacion == "S":
                    fila += 1
                elif orientacion == "E":
                    columna += 1
                else:  # orientacion == "O"
                    columna -= 1
                pieza = (fila, columna)
                barco.append(pieza)

            # Verificar si el barco cabe en el tablero
            if self.coloca_barco_plus(barco):
                print(f"Barco colocado: {barco}")
                return True

        # Si no se pudo colocar después de 'num_intentos', retornar False
        print("No se pudo colocar el barco después de los intentos.")
        return False

    def __str__(self):
        """
        Representación visual del tablero.
        Para el tablero enemigo, no se deben mostrar los barcos.
        """
        tablero_str = ""
        for fila in self.tablero:
            for celda in fila:
                if celda == celda_barco:
                    # No mostrar barcos, solo agua.
                    tablero_str += " " + celda_agua + " "
                else:
                    tablero_str += " " + celda + " "
            tablero_str += "\n"
        return tablero_str


# Crear un tablero para el jugador
jugador_tablero = Tablero(id_jugador=0)

# Intentar colocar un barco aleatorio
jugador_tablero.crea_barco_aleatorio(eslora=4, num_intentos=100)

# Mostrar el tablero del jugador
print("Tablero del Jugador:")
print(jugador_tablero)
