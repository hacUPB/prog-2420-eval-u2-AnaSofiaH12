```
inicio
    leer altitud_ini  
    leer co_arras    
    altitud_min         
    definir cont orbita=0

    mientras altitud_ini > altitud_min       
        calcular altitud_proce= altitud_ini * co_arras
        calcular alt_lorbit=altitud_ini - altitud_proce
        co_arras=co_arras+1e-5
        orbitas = orbitas + 1

        imprimir "para la orbita {orbita} se descendieron {altitud_proce}km, su altitud final es {alt_lorbit} y su nuevo coeficiente de arraste es{co_arras}" 

        si altitud_min >= alt_lorbit:    
            romper  
    imprimir "fin simulacion "

fin
