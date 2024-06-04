def crear_hotel(niveles, habitaciones_por_nivel):
    hotel = [[' ' for _ in range(habitaciones_por_nivel)] for _ in range(niveles)]

    for nivel in range(niveles):
        for habitacion in range(habitaciones_por_nivel):
            hotel[nivel][habitacion] = f"{nivel + 1:0>1}{habitacion + 1:0>2}"

    return hotel

def mostrar_hotel(hotel):
    for nivel in hotel:
        print(' | '.join(nivel))

def ocupar_habitacion(hotel, habitacion):
    nivel, numero = int(habitacion[0]) - 1, int(habitacion[1:])
    if 1 <= nivel < len(hotel) and 1 <= numero <= len(hotel[0]):
        if hotel[nivel][numero - 1] == 'X':
            print(f"La habitación {habitacion} ya está ocupada.")
        else:
            hotel[nivel][numero - 1] = 'X'
            print(f"La habitación {habitacion} ha sido ocupada.")
            return True
    else:
        print(f"habitación no valida: {habitacion}. Inténtalo de nuevo.")
    return False

def main():
    niveles = 5
    habitaciones_por_nivel = 12
    hotel = crear_hotel(niveles, habitaciones_por_nivel)

    while True:
        mostrar_hotel(hotel)
        habitacion = input("Ingresa el número de habitación para ocupar (0 para salir): ")
        if habitacion == '0':
            break
        ocupar_habitacion(hotel, habitacion)

    habitaciones_ocupadas = sum(row.count('X') for row in hotel)
    print(f"Se ocuparon {habitaciones_ocupadas} habitaciones en total.")


main()
