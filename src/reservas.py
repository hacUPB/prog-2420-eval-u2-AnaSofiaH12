from random import randint
from os import system
def main():


    Genero = str(input("¿Es usted Señor o Señora?:  "))
    nombre = str(input(("Por favor, ingrese su nombre: ")))
    apellido = str(input("Por favor, ingrese su apellido: "))


    print(f"{Genero},{nombre} {apellido},¡Bienvenid@ a AirPink Airlines!")
    print(f"{Genero},{nombre} {apellido}, Por favor en sus repuestas no utilice tildes y siempre la primera letra debera ser en mayuscula")

    ciudades = ["Medellin","Bogota","Cartagena"]
    dias_1 = ["Lunes","Martes","Miercoles","Jueves"]
    dias_2 = ["Viernes","Sabado","Domingo"]

    ciudad_origen = str(input("Por favor ingrese su ciudad de origen (Las opciones disponibles son: Medellin, Bogota , Cartagena): "))

    ciudad_destino = str(input("Por favor ingrese la ciudad de destino deseada (Las opciones disponibles son: Medellin, Bogota, Cartagena): "))

    if ciudad_origen.capitalize() in ciudades:
        if ciudad_destino.capitalize() in ciudades and ciudad_destino != ciudad_origen:
        
            dia_semana = str(input("Por favor ingrese el día que desea para su viaje (De Lunes a Domingo): "))
                
            if dia_semana.capitalize() in dias_1:
                if (ciudad_origen.capitalize() == "Bogota" and ciudad_destino.capitalize() == "Medellin") or (ciudad_origen.capitalize() == "Medellin" and ciudad_destino.capitalize() == "Bogota"):
                    distancia = 240
                    precio_1 = 79900
                            
                elif (ciudad_origen.capitalize() == "Bogota" and ciudad_destino.capitalize() == "Cartagena") or (ciudad_origen.capitalize() == "Cartagena" and ciudad_destino.capitalize() == "Bogota"):
                    precio_1 = 156900
                    distancia = 657
                            
                elif (ciudad_origen.capitalize() == "Medellin" and ciudad_destino.capitalize() == "Cartagena") or (ciudad_origen.capitalize() == "Cartagena" and ciudad_destino.capitalize() == "Medellin"):
                    precio_1 = 156900
                    distancia = 461
                            
                else:
                    print("Destino no posible")
                    


            elif dia_semana.capitalize() in dias_2:
                if (ciudad_origen.capitalize() == "Bogota" and ciudad_destino.capitalize() == "Medellin") or (ciudad_origen.capitalize() == "Medellin" and ciudad_destino.capitalize() == "Bogota"):
                    precio_1 = 119900
                    distancia = 240
                elif (ciudad_origen.capitalize() == "Bogotá" and ciudad_destino.capitalize() == "Cartagena") or (ciudad_origen.capitalize() == "Cartagena" and ciudad_destino.capitalize() == "Bogotá"):
                    precio_1 = 213000
                    distancia = 657
                            
                        
                elif (ciudad_origen.capitalize() == "Medellín" and ciudad_destino.capitalize() == "Cartagena") or (ciudad_origen.capitalize() == "Cartagena" and ciudad_destino.capitalize() == "Medellín"):
                    precio_1 = 213000
                    distancia = 461
                            
                else:
                    print("Destino no posible")
                    
            else:
                print("Día no posible")            
        else:
            print("Ciudad no posible o ciudad de origen no puede ser igual a la ciudad de destino")

    preferencia = str(input("¿Dónde le gustaria sentarse? (Pasillo, Ventana, o no tiene preferencia): "))


    def asiento(preferencia):
        if preferencia.lower() == "Pasillo":
            gusto_preferencia = "C"
        elif preferencia.lower() == "Ventana":
            gusto_preferencia = "A"
        else:
            gusto_preferencia = "B"
        
        numero = randint(1,29)
        return numero,gusto_preferencia

    dia_mes = int(input("Ingrese el día del mes que desea viajar (Entre 1 y 30): "))
    mes = str(input("¿Qué mes le gustaria viajar?: "))

    print(f"Tu vuelo de {ciudad_origen} a {ciudad_destino} el día {dia_mes} de {mes} está reservado")
    print(f"El precio de boleto es {precio_1}")
    print(f"Su asiento es {asiento(preferencia)}")

if __name__ == "__main__":
    main()
    