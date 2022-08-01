
class Operações:

    #Construtor

    def __init__(self):
        pass


    #Métodos da Calculadora
    def soma(self, x, y):
        resultado = x + y
        return resultado


    def subtração(self, x, y):
        resultado = x - y
        return resultado


    def divisão(self, x, y):
        resultado = x / y
        return resultado


    def multiplicação(self, x, y):
        resultado = x * y
        return resultado


    def exponenciação(self, x, y):
        resultado = x ** y
        return resultado


    def resto_divisão(self, x, y):
        resultado = x % y
        return resultado


    def porcem(self, x, y):
        resultado = y * x / 100
        return resultado
        

class Calculadora(Operações):
    def __init__(self):
        lista = []
        self.lista = lista

    

    def Opções(self):
        print('-'*40)
        print('''Escolha a operação que deseja realizar:
        [1] Para somar
        [2] Para subtrair
        [3] Para multiplicar
        [4] Para dividir
        [5] Para elevar
        [6] Para ver o resto da divisão
        [7] Para porcentagem
        [8] Para apagar a operação anterior
        [9] Para reiniciar o programa
        [10] Para encerrar o programa''')
        print('-'*40)

    #Propriedades da calculadora
    def Adicionar_Lista(self, valor):
        self.lista.append(valor)
        print(valor)
    
    def Validar_Dados_Int(self, mensagem_principal, mensagem_erro):
         while True:
            a = input(mensagem_principal).strip()
            try:
                a = int(a)
                return a
            except ValueError:
                print(mensagem_erro)

    
    def Validar_Dados_float(self, mensagem_principal, mensagem_erro):
        while True:
            a = input(mensagem_principal).replace(',', '.').strip()            
            try:
                b = float(a)
                return b
            except ValueError:
                print(mensagem_erro)








        
        
        


        
        

