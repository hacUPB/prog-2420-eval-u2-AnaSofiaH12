
def main():
    altitud_ini=float(input("Ingrese la altitud inicial: "))
    co_arras=float(input("Ingrese el coeficiente de arrastre: "))
    altitud_min=float(input("Ingrese la altitud minima segura: "))
    a=altitud_ini
    c=co_arras
    m=altitud_min
    orbita=0
    
    while a>m:
        b=co_arras*a
        a=a-b
        c+=1e-5
        orbita+=1
        
        print(f"En la orbita {orbita} su altura fue de {a} y su coeficiente de arrastre fue de {c}")
        if m>=a:
            break
    print("simulacion terminada")
if __name__ == "__main__":
    main()
    