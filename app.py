import pandas as pd

class linear_regression:
    
    '''
      Prevendo o peso do cérebro considerando o tamanho da cabeça de seres humanos utilizando Regressão Linear Simples.
    '''

    #Carregar os dados
    dados = pd.read_csv('dados/pesos2.csv')
    
    #Preparando as informações iniciais
    def __init__(self):
    
        self.numerador = 0
        self.denominador = 0
        self.X = self.dados['Head Size'].values
        self.Y = self.dados['Brain Weight'].values
        self.n = len(self.X)
        self.X_mean = sum(self.X) / len(self.X)
        self.Y_mean = sum(self.Y) / len(self.Y)
        self.head_size = input('Digite o tamanho em cm³ da cabeça: ')
        self.calculos_ab()

    #Fórmula regressão linear simples para calcular a e b 
    def calculos_ab(self):

        for i in range(self.n):

            self.numerador += (self.X[i] - self.X_mean) * (self.Y[i] - self.Y_mean)
            self.denominador += (self.X[i] - self.X_mean) ** 2
                
        b = self.numerador / self.denominador
        a = self.Y_mean - (b * self.X_mean)

        self.prever_peso(a, b)


    def prever_peso(self, a, b):

        # y = a + bx
    
        y = a + (b * int(self.head_size))
 
        return print("O peso do cérebro em gramas é: {}".format(y))


if __name__ == "__main__":
    
    modelo  = linear_regression()
