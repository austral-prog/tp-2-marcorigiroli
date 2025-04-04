def change():
    gasto = float(input("Ingresar gasto:\n"))
    dinero_recibido = float(input("Dinero recibido\n"))

    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)
    centavos = ((vuelto - pesos) * 100)

    print("\nVuelto\n")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
change()

