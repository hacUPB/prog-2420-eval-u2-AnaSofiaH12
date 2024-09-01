```
Inicio 
    Leer T 
    Leer nombre 
    Leer Apellido 


 //Bienvenida al usuario
    
    Imprimir “T. Nombre, Apellido ¡Bienvenido a FastFast Airlines!" 

    Definir ciudades= [Medellín, Cartagena, Bogotá]
    Definir dias_1 = [lunes, martes, miércoles, jueves]
    Definir dias_2 = [viernes, sábado, domingo]

    Leer cuidad_ origen 
    Leer cuidad_destino 
    Leer dia_semana 
    Leer dia_mes 


 //se le indica la distancia al usuario

    Si cuidad_origen = Medellin y cuidad_destino = Bogota 
	    Distancia = 240 
    Fin si

    Si cuidad_origen = Bogota y cuidad_destino = Medellin 
        Distancia = 240 
    Fin si

    Si cuidad_origen = Medellin y cuidad_destino = Cartagena 
	    Distancia = 461
    Fin si 

    Si cuidad_origen = Cartagena y cuidad_destino = Medellin  
	    Distancia = 461
    Fin si 

    Si cuidad_origen = Bogota y cuidad_destino = Cartagena 
	    Distancia = 657
    Fin si 

    Si cuidad_origen = Cartagena y cuidad_destino = Bogota 
	    Distancia = 657
    Fin si 


 // se le indica al usuario el precio de su boleto 

    Si dia = (dias_1) 
	    Si distancia < 400
		    Entonces precio =79.900
	    Sino 
		    Entonces precio = 156.900
	    Fin si
    Fin si 

    Si dia = (dias_2)
	    Si distancia < 400
		    Entonces precio = 119.900
	    Sino 
		    Entonces precio = 213.000
	    Fin si 
    Fin si 
    
    Imprimir = “Diga que asiento prefiere (A, B, C), tenga en cuenta pasillo es C, ventana es A o sin preferencia es B” 

    Leer asiento 
    Leer preferencia 
    Asiento = random.randint(1, 30)
    Imprimir “asiento + preferencia”
    
    Imprimir “nombre, apellido, ciudad de salida(ciudad_origen), ciudad de llegada(ciudad_destino), su fecha del viaje es(dia_mes)(dia_semana), precio del boleto(precio), y tu asiento es(asiento)”
Fin

