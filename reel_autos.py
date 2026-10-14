print("🎬 ORGANIZADOR DE REELS - TUKI AI")

duracion = int(input("¿Cuántos segundos dura el Reel? "))
escenas = int(input("¿Cuántas escenas querés? "))

if escenas > 0:
    resultado = duracion / escenas
    print("Cada escena debe durar", resultado, "segundos")
else:
    print("Error: la cantidad de escenas debe ser mayor que cero.")
