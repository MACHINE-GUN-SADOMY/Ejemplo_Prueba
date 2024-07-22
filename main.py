import funciones

def opccion_input():
    try:
        opt=int(input(">> "))
    except (ValueError) as nombre_error:
        if isinstance (nombre_error, ValueError):
            print("Valor incorrecto, vuelve a intentarlo.")
    else:
        match opt:
            case 1:
                funciones.main_1()
            
            case 2:
                funciones.main_2()

            case 3:
                funciones.main_3()

            case 4:
                funciones.main_4()
            case _:
                print("Opcion incorrecta, vuelva a intentarlo.")

while True:
    print("""
    ========= MENU =======
    == 1.- Aleatorios ====
    == 2.- Mostrar Json ==
    == 3.- Convertir CSV =
    == 4.-  Salir       ==
    """)
    opccion_input()


#funciones.main_menu()