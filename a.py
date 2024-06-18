# El Servicio Nacional del Consumidor (SERNAC), está probando una forma simplificada para registrar y gestionar los
# reclamos de los consumidores. Para ello utiliza solo cuatro campos de información:
# ° RUT: Rut del reclamante, con DV.
# ° Fecha: Fecha del reclamo en formato dd-mm-yyyy HH:MM:SS
# ° Monto: Valor de la compra en miles de pesos.
# ° Reclamo: Reseña del reclamo en texto libre, de no más de veinte caracteres.
# El programa debe funcionar hasta que el usuario decida finalizar el programa.

from datetime import datetime
import csv
# Registrar Reclamo: Permite ingresar RUT, Monto y Reclamo
def registrar_reclamo():
    rut = int(input("Ingrese su rut: "))
    fecha = datetime
    monto = int(input("Ingrese monto $"))
    montooo = monto/1000
    total_monto = round(montooo)
    reclamo = input("Ingrese la razon de su reclamo: ")
    return{"rut": rut, "total_monto": total_monto, "reclamo": reclamo, "fecha": fecha}

# Listar Reclamos: Se usa para mostrar todos los reclamos ingresados, incluyendo la fecha
def listar_reclamos(cliente):
    for i in cliente:
        print(f"-"*30)
        print(f"Rut: {i['rut']}")
        print(f"Monto en miles: {i['total_monto']}")
        print(f"Reclamo: {i['reclamo']}")
        print(datetime)
        print(f"-"*30)

# Respaldar Reclamos: Genera un respaldo en archivo de todos los reclamos ingresados en formato CSV.
def respaldar_reclamos():
    with open("reclamos.csv", "w", newline = '') as file:
        writer = csv.writer(file)
        writer.writerow("rut", "fecha", "monto", "reclamos")
        writer.writerows(reclamo)

cliente = []
reclamo = []

# Y considera las siguientes funcionalidades:
# 1. Registrar Reclamo
# 2. Listar Reclamos
# 3. Respaldar Reclamos
# 4. Salir
while True: 
    resp = input("1)Registrar Reclamo\n2)Listar Reclamos\n3)Respaldar Reclamos\n4)Salir\nIngrese la opcion que desea: ")
    if resp == "1":
        cliente.append(registrar_reclamo())
    elif resp == "2":
        listar_reclamos(cliente)
    elif resp == "3":
        respaldar_reclamos()
    elif resp == "4":
        break