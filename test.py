##r=[]
##p=[]
##def test(a,b):
##    if a == 1:
##        return r,p
##    else:
##        r.append(a)
##        p.append(b)
##        return test(a-1,b-1)
##
##x= test(5,4)
##print(x)

##r=[]
##p=[]
##def select(a,b,acum):
##    if acum + b[0] == a:
##        r.append(b[0])
##        p.append(0)
##        return r,p
##    elif acum + b[0] < a:
##        acum += b[0]
##        r.append(b[0])
##        p.append(0)
##        b.pop(0)
##        return select(a,b,acum)
##    elif acum + b[0] > a:
##        b.pop(0)
##        return select(a,b,acum)
##        
##x= test(5,[1,2,5,2],0)
##print(x)
## [1,4,3,3,4]

generalReject=7
particularRejects=[1,7,7,4,3,3,4]
##generalReject=5
##particularRejects=[1,2,5,4,1,1]
originalLenght = len(particularRejects)
print("El monto es ", generalReject)
print("La lista es ", particularRejects)
print("El Resultado de montos y posiciones es: ")
##print(originalLenght)

result=[]
positions=[]
def select(reject,rejectsList,accum):
    if len(rejectsList)>0 and accum + rejectsList[0] == reject:
        lenght = len(rejectsList)
        result.append(rejectsList[0])
        positions.append(originalLenght-lenght)
        ##print(originalLenght)
        return result,positions
    elif len(rejectsList)>0 and accum + rejectsList[0] < reject:
        lenght = len(rejectsList)
        accum += rejectsList[0]
        result.append(rejectsList[0])
        positions.append(originalLenght-lenght)
        print(result,positions)
        rejectsList.pop(0)
        return select(reject,rejectsList,accum)
    elif len(rejectsList)>0 and accum + rejectsList[0] > reject:
        rejectsList.pop(0)
        print(result,positions)
        return select(reject,rejectsList,accum)
    elif len(rejectsList) == 0:
        print("Ya valio madres")
      
x = select(generalReject,particularRejects,0)
print(x)



