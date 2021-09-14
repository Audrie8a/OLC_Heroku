
from Instruction.Parameter import Parameter
from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Enum.typeExpression import typeExpression
from Environment.Listas import Listas

class Function(Instruction):
    
    def __init__(self, id: str, parameters,block,linea,columna) -> None:
        self.id = id
        self.parameters = parameters
        self.block = block
        self.linea=linea
        self.columna=columna

    def execute(self, environment: Environment):
        environment.saveFunction(self.id,self,self.linea,self.columna)

    def executeFunction(self, environment: Environment):
        try:
            newEnv = Environment(environment)
            for parameter in self.parameters:
                parameter.execute(newEnv)
            
            for ins in self.block:
                ins.execute(newEnv)
        except:
            print("\n Error al ejecutar funcion!")
            Listas.saveError("Error al ejecutar función!",self.linea,self.columna)

    def executeFunctionNone(self, environment: Environment):
        try:
            newEnv = Environment(environment)
            
            for ins in self.block:
                ins.execute(newEnv)
        except:
            print("\nError al ejecutar funcion!")
            Listas.saveError("Error al ejecutar función!",self.linea,self.columna)