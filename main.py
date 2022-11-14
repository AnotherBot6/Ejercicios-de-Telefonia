def main():
    print('Dame el número de mensajes')
    msj=input()
    print('Dame el número de megas')
    megas=input()
    print('Dame el número de minutos')
    min=input()
    msj_int=int(msj)
    megas_flo=float(megas)
    min_int=int(min)
    
    cobro=float(0.80)
    pago=(cobro*msj_int)+(cobro*megas_flo)+(cobro*min_int)
    print('El costo mensual es: ' ,str(float(pago)))

if __name__ == '__main__':
    main()
