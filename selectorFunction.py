#En caso de dudas hay print en test.py
##generalReject=7
##particularRejects = [1,4,3,3,4]
##originalLenght = len(particularRejects)
##particularRejects2 = [1,4,3,3,4] 
##
##IMPORTANTE: Fue necesario crear un respaldo de la lista de vectores 
##  porque el tamano cambia conforme la recursividad (aun no entiendo porque si se hizo una reasignacion de variables)

##result=[]
##positions=[]

def select(jle, typeNomina, bank, reject,rejectsList,accum,originalLenght, backupRejectsList,result,positions):
    ##print("El monto es ", reject)
    ##print("El acumulado es ",accum)
    ##print("Porque pitos no es la suma ", round((accum + rejectsList[0]),2))
    
    if len(rejectsList)>0 and round((accum + rejectsList[0]),2) == round(reject,2):
        lenght = len(rejectsList)
        result.append(rejectsList[0])
        positions.append(originalLenght-lenght)
        ##print("Sume Final ", rejectsList[0])
        ##print(originalLenght)
        ##return result,positions
        print("La junta es", jle)
        print("La Nomina es ",typeNomina)
        print("El Banco es ", bank)
        print("El monto es ", reject)
        print("El Resultado de montos es: ")
        print(result)
        print(" ")
        ##print("La lista es ", particularRejects)
        ##print("El Resultado de montos y posiciones es: ")
        return result
        
    elif len(rejectsList)>0 and accum + rejectsList[0] < reject:
        lenght = len(rejectsList)
        accum += rejectsList[0]
        accum = round(accum,2)
        result.append(rejectsList[0])
        positions.append(originalLenght-lenght)
        ##print(result,positions)
        ##print("Sume ", rejectsList[0])
        ##print("backup funcion", backupRejectsList)
        rejectsList.pop(0)
        return select(jle, typeNomina, bank,reject,rejectsList,accum,originalLenght, backupRejectsList,result,positions)

    elif len(rejectsList)>0 and accum + rejectsList[0] > reject:
        ##print("Quite del rejectsList ",rejectsList, rejectsList[0] )
        rejectsList.pop(0)
        #print(result,positions)
        return select(jle, typeNomina, bank,reject,rejectsList,accum,originalLenght, backupRejectsList,result,positions)

    #Esta seccion realiza retroceso del vector cuando no cumple con el monto general
    elif len(rejectsList) == 0:
        ##print("ATENCION",len(result))
        lastamount = result[-1]
        lastposition = positions[-1]
        #print(result)
        #print(type(lastposition),lastposition)
        
        #print("acum viejo   ", accum)
        accum -= lastamount
        accum = round(accum,2)
        #print("acum nuevo   ", accum)

        ##print("Reste de Resul ", result[-1])
        result.pop()
        positions.pop()
        #print(result, positions)

        #print(particularRejects2)
        #print(originalLenght)
        
        rejectsList = backupRejectsList[lastposition+1:originalLenght]
        ##print("cuando quite ",rejectsList)
        return select(jle, typeNomina, bank, reject, rejectsList, accum, originalLenght, backupRejectsList,result,positions)

##x = select(generalReject,particularRejects,0)
##print(x)

