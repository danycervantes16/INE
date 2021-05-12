import csv
import pandas as pd
import numpy as np

import selectorFunction as joa

rechGral = open( "C:\danydev\INE\RechGral.csv")
rechGralReader = csv.reader(rechGral)
rechGralData = list(rechGralReader)
rechGralData

for i in range(1, len(rechGralData)):
    #print(rechGralData[i][3],type(rechGralData[i][3]))
    rechGralData[i][3]=float(rechGralData[i][3])
    #print(rechGralData[i][3],type(rechGralData[i][3]))

rechInd = open( "C:\danydev\INE\RechInd.csv")
rechIndReader = csv.reader(rechInd)
rechIndData = list(rechIndReader)
rechIndData
#print(len(rechIndData))

for i in range(1, len(rechIndData)):
    #print(rechIndData[i][3],type(rechIndData[i][3]))
    rechIndData[i][3]=float(rechIndData[i][3])
    #print(rechIndData[i][3],type(rechIndData[i][3]))
#print(type(rechIndData))


resultados = []
for i in range(1, len(rechGralData)):
##for i in range(2,4):
##for i in range(1,2):
    junta = rechGralData[i][0]
    nomina = rechGralData[i][1]
    banco = rechGralData[i][2]
    rechazo = rechGralData[i][3]
    arrayRechInd = []
    for j in range(1, len(rechIndData)):
        juntaInd = rechIndData[j][0]
        nominaInd = rechIndData[j][1]
        bancoInd = rechIndData[j][2]
        rechazoInd = rechIndData[j][3]
        if juntaInd == junta and nominaInd == nomina and bancoInd == banco:
            arrayRechInd.append(rechazoInd)
    ##Integrando la funcion selectorFunction
    ##print(arrayRechInd)
    arrayRejects = arrayRechInd
    backupRejects = arrayRechInd[:]
    originalLenght = len(backupRejects)
    ##result=[]
    ##positions=[]
    finalArray = joa.select(junta,nomina,banco,rechazo,arrayRejects,0,originalLenght,backupRejects,[],[])
    lenghtFinalArray = len(finalArray)
    for k in range(lenghtFinalArray):
        resultados.append([junta,nomina,banco,finalArray[k]])

##convertir a numpy array
npFinal=np.array(resultados)

# convert array into dataframe
dataFinal = pd.DataFrame(npFinal)
  
# save the dataframe as a csv file
dataFinal.to_csv("resultado.csv")




    
    

