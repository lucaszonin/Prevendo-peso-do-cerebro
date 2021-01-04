import pandas as pd

class linear_regression:
    '''
      Prevendo o peso do cérebro considerando o tamanho da cabeça de seres humanos utilizando Regressão Linear Simples.
    '''
    dados = pd.read_csv('pesos2.csv')
    
    #Separando os dados
    X = dados['Head Size'].values
    Y = dados['Brain Weight'].values

    numerador = 0
    denominador = 0

    def __init__(self, X = X, Y = Y):
    
        self.X = X
        self.Y = Y
        self.n = len(X)
        self.X_mean = sum(self.X) / len(self.X)
        self.Y_mean = sum(self.Y) / len(self.Y)
        self.head_size = input('Digite o tamanho em cm³ da cabeça: ')
    
        for i in range(self.n):

            self.numerador += (X[i] - self.X_mean) * (Y[i] - self.Y_mean)
            self.denominador += (X[i] - self.X_mean) ** 2
                
        self.b = self.numerador / self.denominador
        self.a = self.Y_mean - (self.b * self.X_mean)

        return self.prever_peso(self.a, self.b, self.head_size)


    def prever_peso(self, a, b, head_size):

        # y = a + bx
    
        y = a + (b * int(head_size))
 
        return print("O peso do cérebro em gramas é: {}".format(y))


if __name__ == "__main__":
    
    modelo  = linear_regression()
