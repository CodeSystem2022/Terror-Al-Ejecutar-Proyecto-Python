def listarFacturas(facturas):
    print("\nFacturas: \n")
    contador = 1
    for fact in facturas:
        datos="{0}. idFacturacion: {1} | Subtotal: {2}  | Impuestos {3} | Total: {4}"
        print(datos.format(contador, fact[0], fact[1], fact[2], fact[3]))
        contador +=1
    print(" ")
    
    
def pedirDatosRegistro(subtotal, impuestos, total):
    factura =(subtotal, impuestos, total)
    return factura