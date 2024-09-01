## Analisis problema 1 "Sistema de reservas de aerolineas"

### Analisis:
-Leer T, nombre, apellido:

    Se lee el género (T), nombre y apellido del usuario.

    Imprimir mensaje de bienvenida:
    Se imprime un mensaje de bienvenida personalizado con el género, nombre y apellido del usuario.

-Definir listas de ciudades y días:

    Se definen las listas de ciudades (ciudades), días de semana (dias_1) y días de fin de semana (días_2).

-Leer ciudad_origen, ciudad_destino, dia_semana, dia_mes:

    Se leen los datos de entrada relacionados con la ciudad de origen, destino, día de la semana y día del mes.

-Calcular la distancia entre ciudades:
```Según la combinación de ciudad_origen y ciudad_destino, se asigna un valor a la variable Distancia. Las combinaciones posibles son:
o	Medellín = Bogotá: 240 km
o	Medellín = Cartagena: 461 km
o	Bogotá = Cartagena: 657 km
```
-Calcular el precio del boleto:

    Se determina el precio del boleto basado en la distancia y el día de la semana:

        Si el día pertenece a dias_1 (lunes a jueves):
            Si la distancia es menor a 400 km: 79,900
            Si la distancia es 400 km o mayor: 156,900

        Si el día pertenece a días_2 (viernes a domingo):
            Si la distancia es menor a 400 km: 119,900
            Si la distancia es 400 km o mayor: 213,000

-Solicitar la preferencia de asiento:

    Se imprime un mensaje solicitando la preferencia de asiento del usuario (pasillo, ventana, sin preferencia).
    Se lee la preferencia del usuario.

-Asignar un número de asiento aleatorio:

    Se asigna un número de asiento aleatorio entre 1 y 30.

-Imprimir los detalles del vuelo:
Nombre y apellido del usuario.
Ciudad de origen y destino.
Fecha del viaje (día del mes y día de la semana).
Precio del boleto.
Número de asiento asignado.

Fin 


### Datos de Entrada:
	1.	Título del usuario: “Sr.” o “Sra.”
	2.	Nombre: (el nombre del usuario).
	3.	Apellido: (el apellido del usuario).
	4.	Ciudad de origen: “Medellín”, “Bogotá” o “Cartagena”.
	5.	Ciudad de destino: “Medellín”, “Bogotá” o “Cartagena”.
	6.	Día de la semana 
	7.	Día del mes: (entre 1 y 30)
	8.	Preferencia de asiento: “Pasillo”, “Ventana” o “Sin preferencia”.

### Datos de Salida:
	1.	Saludo personalizado: Un mensaje de bienvenida que incluye el nombre completo del usuario.
	2.	Nombre completo del usuario: Título, nombre y apellido.
	3.	Origen: La ciudad de origen 
	4.	Destino: La ciudad de destino 
	5.	Fecha de vuelo: El día de la semana y el día del mes.
	6.	Distancia (entre las ciudades de origen y destino) 
	7.	Precio del boleto (calculado en base a la distancia y día de la semana)
	8.	Asiento asignado: Una combinación de número de asiento y letra ( “20C”)
    9.  Ultimo mensaje: Todos los detalles del vuelo 
 


### Variables: 
```
•  T: Género del usuario (entrada)
•  nombre: Nombre del usuario (entrada)
•  apellido: Apellido del usuario (entrada)
•  ciudades: Lista de posibles ciudades (Medellín, Cartagena, Bogotá) 
•  dias_1: Lista de días de la semana (lunes, martes, miércoles, jueves) 
•  días_2: Lista de días de la semana (viernes, sábado, domingo) 
•  ciudad_origen: Ciudad de origen del vuelo (entrada)
•  ciudad_destino: Ciudad de destino del vuelo (entrada)
•  dia_semana: Día de la semana en que se realiza el viaje (entrada)
•  dia_mes: Día del mes en que se realiza el viaje (entrada)
•  Distancia: Distancia entre las ciudades de origen y destino (variable interna)
•  precio: Precio del boleto (variable interna)
•  asiento: Número de asiento asignado aleatoriamente 
•  preferencia: Preferencia de asiento del usuario (entrada)
