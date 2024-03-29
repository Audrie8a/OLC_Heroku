from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Abstract.Expression import Expression
from Environment.Listas import Listas

class While(Instruction):

    def __init__(self, condition: Expression, block,linea,columna) -> None:
        self.condition = condition
        self.block = block
        self.linea=linea
        self.columna=columna

    def execute(self, environment: Environment):
        try:

            tempCondition: Symbol = self.condition.execute(environment)

            while(tempCondition.getValue() == True):
                newEnv = Environment(environment)

                for ins in self.block:
                    ins.execute(newEnv)

                tempCondition = self.condition.execute(environment)
        except:
            print("\nError al ejecutar el while ",self.linea,self.columna)
            Listas.saveError("Error al ejecutar el while!",self.linea,self.columna)