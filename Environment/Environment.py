from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Environment.Listas import Listas

class Environment:
    
    def __init__(self, father):
        #Usamos un diccionario para nuestra tabla de simbolos, guardara el id como clave y como cuerpo un simbolo
        self.variable = {}
        self.function={}
        self.Global={}
        self.Parameter={}
        
        #Father es el entorno exterior al cual podemos acceder
        self.father = father

    def getGlobal(self):
        tempEnv: Environment = self;
        while(tempEnv.father != None):
            tempEnv = tempEnv.father
        return tempEnv

    def saveVariable(self, id: str, value, type: typeExpression, isArray: bool, linea, columna):
        try:
            if self.Parameter.get(id)==None:
                if (self.variable.get(id) != None): #Encontro una local la edita
                    self.alterVariable(id,Symbol(id,value,type,self.variable.get(id).getExtens(),self.variable.get(id).getLine(),self.variable.get(id).getColumn()),linea,columna)
                else: #Busca una Global
                    tempEnvGlobal = self
                    tempEnv = self
                    condicion=False
                    while(tempEnvGlobal != None):
                        if(tempEnvGlobal.Global.get(id) != None):
                            condicion=True
                            break
                        tempEnvGlobal = tempEnvGlobal.father

                    if condicion:
                        self.alterVariableGlobal(id,Symbol(id,value,type,tempEnvGlobal.Global.get(id).getExtens(),tempEnvGlobal.Global.get(id).getLine(),tempEnvGlobal.Global.get(id).getColumn()),linea,columna)
                    else:
                        while(tempEnv != None):
                            if(tempEnv.variable.get(id) != None):                        
                                break
                            tempEnv = tempEnv.father
                        if tempEnv!= None:
                            if tempEnv.variable.get(id)!=None:
                                if tempEnv.variable.get(id).getExtens()=='none':
                                    self.alterVariable(id,Symbol(id,value,type,tempEnv.variable.get(id).getExtens(),tempEnv.variable.get(id).getLine(),tempEnv.variable.get(id).getColumn()),linea,columna)
                                else:
                            
                                    tempVar = Symbol(id,value,type,"none",linea,columna)
                                    tempVar.array = isArray
                                    self.variable[id] = tempVar
                            else:
                        
                                tempVar = Symbol(id,value,type,"none",linea,columna)
                                tempVar.array = isArray
                                self.variable[id] = tempVar
                        else:
                            tempVar = Symbol(id,value,type,"none",linea,columna)
                            tempVar.array = isArray
                            self.variable[id] = tempVar 
            else:
                self.alterVariable(id,Symbol(id,value,type,self.Parameter.get(id).getExtens(),self.Parameter.get(id).getLine(),self.Parameter.get(id).getColumn()),linea,columna)
        except:
            print("Error al manejar Variable " + id ,linea,columna)
            Listas.saveError("Error al manejar Variable " + id,linea,columna)
            return None

    def saveParameter(self, id: str, value, type: typeExpression, isArray: bool, linea, columna):
        
        try:
            if (self.Parameter.get(id) != None):
                print("Parametro " + id + " Está repetido!")
                Listas.saveError("Parametro " + id + " Está repetido!",linea,columna)
                return
            tempVar = Symbol(id,value,type,"Parameter",linea,columna)
            tempVar.array = isArray
            self.Parameter[id] = tempVar
        except:            
            print("Error al crear Variable " + id ,linea,columna)
            Listas.saveError("Error al crear Variable " + id,linea,columna)
            return None

    def saveVariableLocal(self, id: str, value, type: typeExpression, isArray: bool, linea, columna):
        try:
            if self.Parameter.get(id)==None:
                if (self.variable.get(id) != None or self.Global.get(id) != None):
                    print("La variable " + id + " ya existe")
                    return None
                tempVar = Symbol(id,value,type,"local",linea,columna)
                tempVar.array = isArray
                self.variable[id] = tempVar
            else:
                print("Error al crear Variable "+id+". Se encuentra un parámetro con este Id")               
                Listas.saveError("Error al crear Variable "+id+". Se encuentra un parámetro con este Id",linea,columna)
        except:
            print("Error al crear Variable " + id ,linea,columna)
            Listas.saveError("Error al crear Variable " + id,linea,columna)
            return None

    def saveVariableGlobal(self, id: str, value, type: typeExpression, isArray: bool, linea, columna):
        try:
            if self.Parameter.get(id)==None:
                if (self.Global.get(id) != None):
                    print("La variable " + id + " ya existe")
                    return None
                tempVar = Symbol(id,value,type,"global",linea, columna)
                tempVar.array = isArray
                self.Global[id] = tempVar
            else:
                print("Error al crear Variable "+id+". Se encuentra un parámetro con este Id")
                Listas.saveError("Error al crear Variable "+id+". Se encuentra un parámetro con este Id",linea,columna)
        except:
            print("Error al crear Variable " + id ,linea,columna)
            Listas.saveError("Error al crear Variable " + id,linea,columna)
            return None

    def getVariable(self, id: str,linea,columna) -> Symbol:
        try:
            if self.Parameter.get(id)==None:
                condicion=0
                tempEnv = self
                tempEnvGlobal = self
                
                while(tempEnv != None):
                    if(tempEnv.variable.get(id) != None):
                        if(tempEnv.variable.get(id).getExtens()=='local' and condicion!=0):
                            print("Error: la variable " + id + " no existe")                      
                            Listas.saveError("Error: la variable" + id + " no existe" + id,linea,columna)
                            return None
                        else:
                            return tempEnv.variable.get(id).getValue()
                            
                    tempEnv = tempEnv.father
                    condicion=condicion+1

                

                while(tempEnvGlobal != None):
                    if(tempEnvGlobal.Global.get(id) != None):
                        return tempEnvGlobal.Global.get(id).getValue()
                    tempEnvGlobal = tempEnvGlobal.father
                print("Error: la variable " + id + " no existe")                      
                Listas.saveError("Error: la variable " + id + " no existe" + id,linea,columna)
                
                return None
            else:
            
                tempEnv = self
                
                while(tempEnv != None):
                    if(tempEnv.Parameter.get(id) != None):
                        return tempEnv.Parameter.get(id).getValue()                        
                    else:
                        print("Error: el parámetro " + id + " no existe")                      
                        Listas.saveError("Error: el parámetro " + id + " no existe" + id,linea,columna)
                        return None                        
                    tempEnv = tempEnv.father
        except:
            print("Error al obtener Variable " + id ,linea,columna)
            Listas.saveError("Error al obtener Variable " + id,linea,columna)
            return None

    def alterParametro(self, id: str, value: Symbol,linea,columna):
        try:
            tempEnv = self
            if(tempEnv.Parameter.get(id) != None):
                tempVar: Symbol = tempEnv.Parameter.get(id)
                tempVar.value = value.getValue()
                self.Parameter[id] = tempVar
                return
            print("Error: el Parametro " + id + " no existe",linea,columna)            
            Listas.saveError("Error: el Parametro " + id + " no existe",linea,columna)
            return None
        except:            
            print("Error al eidtar Parametro " + id ,linea,columna)
            Listas.saveError("Error al eidtar Parametro " + id,linea,columna)
            return None

    def alterVariable(self, id: str, value: Symbol,linea,columna):
        try:
            tempEnv = self
            while(tempEnv != None):
                if(tempEnv.variable.get(id) != None):
                    tempVar: Symbol = tempEnv.variable.get(id)
                    tempVar.value = value.getValue()
                    self.variable[id] = tempVar
                    return
                tempEnv = tempEnv.father
            print("Error: la variable " + id + " no existe",linea,columna)
            Listas.saveError("Error: la variable " + id + " no existe" + id,linea,columna)
            return None
        except:
            print("Error al asignar valor variable " + id ,linea,columna)
            Listas.saveError("Error al asignar valor variable " + id,linea,columna)
            return None

    def alterVariableGlobal(self, id: str, value: Symbol,linea,columna):
        try:
            tempEnv = self
            while(tempEnv != None):
                if(tempEnv.Global.get(id) != None):
                    tempVar: Symbol = tempEnv.Global.get(id)
                    tempVar.value = value.getValue()
                    self.Global[id] = tempVar
                    return
                tempEnv = tempEnv.father
            print("Error: la variable " + id + " no existe",linea,columna)
            Listas.saveError("Error: la variable " + id + " no existe" + id,linea,columna)
            return None
        except:
            print("Error al asignar valor variable " + id ,linea,columna)
            Listas.saveError("Error al asignar valor variable " + id,linea,columna)
            return None

    def saveFunction(self, id: str, function,linea,columna):
        try:
            if (self.function.get(id) != None):
                print("La función " + id + " ya existe",linea,columna)
                Listas.saveError("La función " + id + " ya existe",linea,columna)
                return
            self.function[id] = function
        except:
            print("Error al salvar la función " + id ,linea,columna)
            Listas.saveError("Error al salvar la función " + id,linea,columna)
           
    
    def getFunction(self, id: str,linea,columna):
        try:
            tempEnv = self
            while(tempEnv != None):
                if(tempEnv.function.get(id) != None):
                    return tempEnv.function.get(id)
                tempEnv = tempEnv.father
            print("Error: la función " + id + " no existe",linea,columna)
            Listas.saveError("Error: la función " + id + " no existe" + id,linea,columna)
            return None
        except:
            print("Error al buscar la función " + id ,linea,columna)
            Listas.saveError("Error al buscar la función " + id,linea,columna)
            return None