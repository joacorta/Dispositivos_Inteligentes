import conexion
import datetime
import time
import serial

tiempo=datetime.datetime.now()

# Crear una instancia del conector de base de datos
conexion_bd = conexion.Connection(host="localhost", user="root", password="", database="NodoTemperatura")

# Conectar a la base de datos
conexion_bd.connect()

# leer datos que ingresan a traves del puerto serie COM5
ser = serial.Serial('COM5', 9600, timeout=1)


print("Bienvenido, las opciones son:")
print("- Leer la tabla de temperaturas, ingrese 1")
print("- para comenzar a recolectar los datos de temperatura desde el dispositivo, ingrese 2")
print("- Insertar nuevo dato de temperatura, ingrese 3")
print("- Modificar una medicion de temperatura, ingrese 4")
print("- Eliminar un registro de la tabla, ingrese 5")
print("- Para esconectarse de la BD y Salir, ingrese 0 (cero)")

opcion=input("Ingrese el numero correspondiente a la opcion deseada:")

if opcion == "1":
# Leer los temperaturas desde la tabla
    LecturasTemperatura = conexion_bd.leer_LecturasTemperatura()
    for lectura_id in LecturasTemperatura:
        print(lectura_id)
    print("Fin tabla LecturasTemperatura")




elif opcion == "2":
    while True:
        # Recolectar dato de temperatura desde el serial
        temp_str1 = ser.readline()

        try:
            temp = float(temp_str1)  # Convierte la cadena en un número decimal
            tiempo = datetime.datetime.now()
            conexion_bd.ingresar_LecturasTemperatura(0, tiempo, temp)
            print("Temperatura a registrar en °C: ")
            print(temp)
            
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número válido para la temperatura.")

        # Espera 1 segundo antes de la siguiente iteración
        time.sleep(1)


elif opcion == "3":
# Ingresa temperatura a la tabla
    
    
    temp_str = input("Ingrese la temperatura sensada: ")

    try:
        temp = float(temp_str)  # Convierte la cadena en un número decimal
        tiempo=datetime.datetime.now()
        conexion_bd.ingresar_LecturasTemperatura(0, tiempo, temp)
        print("Datos ingresados a LecturasTemperatura")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número válido para la temperatura.")

elif opcion == "4":
# Modificar temperatura de LecturasTemperatura
    temp_str = input("Ingrese la nueva temperatura sensada: ")
    IdTemp_str= input("Ingrese el ID a modificar: ")
    try:
        temp = float(temp_str)  # Convierte la cadena en un número decimal
        IdTemp= int(IdTemp_str)
    
        conexion_bd.modificar_LecturasTemperatura(IdTemp, temp)
        print("Datos modificados en posicion LecturasTemperatura")
        print(IdTemp)
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número válido para la temperatura.")

elif opcion == "5":
# Eliminar una lectura de temperatura
    IdTemp_str= input("Ingrese el ID a eliminar: ")
    try:
        IdTemp= int(IdTemp_str)
        conexion_bd.eliminar_LecturasTemperatura(IdTemp)
        print("Datos eliminado en posicion LecturasTemperatura")
        print(IdTemp)
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número válido de posicion")
    
elif opcion == "0":
# Desconectar de la base de datos
    conexion_bd.disconnect()

else:
    print("Opción no válida. Por favor, selecciona una opción válida.")
    
# Desconectar de la base de datos

conexion_bd.disconnect()