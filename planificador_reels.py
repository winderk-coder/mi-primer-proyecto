print("🎬 PLANIFICADOR DE REELS - TUKI AI")

duracion = int(input("¿Cuántos segundos dura el Reel? "))
escenas = int(input("¿Cuántas escenas querés? "))

if duracion > 0 and escenas > 0:
    tiempo = duracion / escenas

    for numero in range(1, escenas + 1):
        inicio = (numero - 1) * tiempo
        fin = numero * tiempo
        print("Escena", numero, ":", inicio, "a", fin, "segundos")
else:
    print("Error: ingresá valores mayores que cero.")
