import csv
exampleFile = open( "import.csv")
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
exampleData[0][0]

