## Analisis:

-El programa inicia y se leen las variables de entrada:

    altitud_inici: Altitud inicial del satélite.
    co_arras: Coeficiente de arrastre inicial.
    altud_min: Altitud mínima de seguridad.


Se define la variable orbita como 0, la cual servirá para contar el número de órbitas.


-Bucle mientras:

    El bucle se ejecuta mientras (altitud_ini) sea mayor que (altitud_min), es decir, mientras el satélite no haya alcanzado la altitud mínima de seguridad.

-Cálculo de la altitud descendida (altitud_proce):

    En cada iteración del bucle, se calcula cuánto desciende el satélite en esa órbita: altitud_proce = altitud_ini * co_arras.

-Cálculo de la nueva altitud (alt_lorbit):

    Se calcula la altitud después de completar la órbita: alt_lorbit = altitud_ini - altitud_proce.

-Incremento del coeficiente de arrastre (co_arras):

    El coeficiente de arrastre se incrementa ligeramente en cada órbita: co_arras = co_arras + 1e-5.

-Incremento del contador de órbitas (orbita):

    Se incrementa el contador de órbitas en cada iteración del bucle: orbita = orbita + 1.

-Impresión de los resultados para la órbita actual:

    Se imprime un mensaje que incluye:
        Número de órbita actual.
        Altitud descendida en esa órbita.
        Altitud final después de la órbita.
        Nuevo valor del coeficiente de arrastre.
        Condicional para finalizar el bucle:
-Si alt_lorbit es menor o igual a altitud_min, el bucle se detiene con la instrucción romper, indicando que el satélite ha traspasado el límite de seguridad.

Al finalizar el bucle, se imprime un mensaje indicando que la simulación ha finalizado.

### Variables:
    altitud_ini: Altitud inicial del satélite, definida como una variable entera.

    co_arras: Coeficiente de arrastre, definida como una variable de punto flotante.

    altitud_min: Altitud mínima de seguridad, definida como una variable de punto flotante.

    orbita: Contador de órbitas, inicializado a 0.

    altitud_proce: Altitud procedida  en una órbita, calculada como alt_inici * coef_ar.
    
    alt_lorbit: Altitud después de completar una órbita, calculada como alt_inici - alt_des.
    
    co_arras: Se incrementa en cada iteración del bucle por 1e-5 para simular el aumento de la resistencia atmosférica.
    
    orbita: Contador que se incrementa con cada órbita completada.



### Datos de Entrada
    -altitud_ini (Altitud inicial del satélite)
    -co_arras (Coeficiente de arrastre)
    -altitud_min (Altitud mínima de seguridad)


### Datos de Salida
    -Mensajes de simulación:
        Para cada órbita: Se imprime la altitud procedida, la altitud final tras la órbita, y el nuevo coeficiente de arrastre.

        Mensaje final: Indica la finalización de la simulación.
