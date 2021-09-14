from datetime import datetime

class Listas:
    lstError=[]
    lstSalida=[]

    @staticmethod
    def saveError(Descripcion, fila, columna):
        now = datetime.now()
        Fecha = now.strftime("%d/%m/%Y %H:%M:%S")
        Listas.lstError.append([len(Listas.lstError)+1,Descripcion,fila,columna,Fecha])

    @staticmethod
    def saveSalida(Entrada, tipoSalida):
        Listas.lstSalida.append([Entrada,tipoSalida])

    def printErrores():
        for var in Listas.lstError:
            print(var[0],var[1],var[2],var[3],var[4])
    
    def printSaida():
        for var in Listas.lstSalida:
            if (var[1]=='print'):
                print(var[0], end=" ")
            else:
                print(var[0])
    def getListSaida():
        return Listas.lstSalida
    
    def getListError():
        return Listas.lstError
    
    def LimpiarLsts():
        Listas.lstSalida.clear()
        Listas.lstError.clear()