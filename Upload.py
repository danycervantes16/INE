#responsabilidades subir 2 vectores (montos grandes, montos pequenos)
#definir el ciclo
#definir la excepcion del ciclo (Suma montos chiquitos === monto grande)
#funcion de cambio
#imprimir resultado
#desacomodar datos y volver a correr


import pandas as pd
montoscsv = pd.read_csv('C:\danydev\INE\MONTOS.csv')
#rechazos = pd.read_csv('C:\danydev\INE\RECHAZOS.csv')
tablaMontos=pd.DataFrame(montoscsv)
#tablaRechazos=pd.DataFrame(rechazoscsv)

print(tablaMontos.shape)

rechazo=1524200.30
rechazosInd=[350000.24,1300000.00,300000.00,350000.70,300000.00,350000.00,300000.00,350000.00,300000.00,224200.30]

#1) correr la lista e ir validando la acumulacion
#       Si acum+[i]<=rechazo => agregalo a resultados y posiciones, update accum
#       En otro caso saltar y pasa al siguiente dato, incrementar ++

#2) Si despues de reccorrer toda la lista, acum+[i]>rechazo
#       Eliminar el ultimo dato de resultados y la posicion
#       Buscar nuevo dato para el que estaba en ultimo
#Si despues de reccorrer toda la lista, acum+[i]>rechazo
#       Eliminar el penultimo dato de resultados y la posicion
#       Buscar nuevo dato para el que estaba en penultimo
#Si despues de reccorrer toda la lista, acum+[i]>rechazo
#       Eliminar el antepenultimo dato de resultados y la posicion
#       Buscar nuevo dato para el que estaba en antepenultimo

5
[6,1,1,7,2,3,1]

RG=5
[6,1,1,7,2,3,1]
[1,1,7,2,3,1]
Rind=1
Pos=1


RG=4
[1,7,2,3,1]
Rind=1
Pos=2

RG=3
[7,2,3,1]
[2,3,1]
Rind=2
Pos=4

RG=1
[3,1]
[1]
Rind=1
Pos=6

resulGral=[]
posGral =[]


def seleccion(reject,littleRejects):
    result = 0
    position = 0
    accumulation = 0
    i=0
    lenght=len(littleRejects)
    
    if accumulation + littleRejects[i] <= reject
        result=littleRejects[i]
        position = i
        return resulGral.append(seleccion(reject-result,littleRejects[i+1:lenght])),
                posGral.append()
    else:
        result = seleccion(reject,littleRejects)

    
    lenght = len(littleRejects)
    if accumulation + littleRejects[i] <= reject:
        accumulation = accumulation + littleRejects[i]
        result[j]=littleRejects[i]
        positions[j]=i
        j++
        i++
    else:
        i++

    else:
        j--
        i=position[j]+1
        del result[j]
        del position[j]
        seleccion(reject,littleRejects):
        
        
        
        
