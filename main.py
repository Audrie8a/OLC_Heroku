from Analyzer.Panther import parser
from Environment.Listas import Listas
from Reportes.Reportes import Reportes


f = open("./entrada.txt", "r")
input = f.read()
parser.parse(input)

print("\n---------------------------Lista Errores -----------------------------------")
Listas.printErrores()
print("\n-----------------------Salida-----------------------")
Listas.printSaida()
#Reportes.Tabla_Errores()