from ClienteView import ClienteView
from Cliente import Cliente
import PySimpleGUI as sg 

class ClienteController:
    def __init__(self):
        self.__telaCliente = ClienteView(self)
        self.__clientes = {} #lista de objetos Cliente

    def inicia(self):
        self.__telaCliente.tela_consulta()
        
        # Loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__telaCliente.le_eventos()

            if event == sg.WIN_CLOSED:
                rodando = False
            elif event == 'Cadastrar':
                #FIX ME - implementar lógica de cadastro

                try:
                    codigo = values['codigo']
                    nome = str(values['nome'])
                    if nome != '' and codigo.isdigit():
                        self.adiciona_cliente(int(codigo), values['nome'])
                        resultado = 'Cliente Cadastrado'
                    else:
                        resultado = 'Não foi possivel cadastrar o cliente'
                except ValueError:
                    resultado = 'Não foi possivel cadastrar o cliente'

            elif event == 'Consultar':
                #FIX ME - implementar lógica de consulta
                
                nome = values['nome']
                codigo = values['codigo']

                try:
                    if nome != '':
                        resultado = self.busca_nome(nome)
                    elif codigo != '': 
                        codigo = int(codigo)
                        resultado = str(self.busca_codigo(codigo))
                    else:
                        resultado = 'Cliente não cadastrado'

                except ValueError:
                    resultado = 'Cliente não cadastrado'
            
            if resultado != '':
                dados = str(resultado)
                self.__telaCliente.mostra_resultado(dados)

        self.__telaCliente.fim()


    def busca_codigo(self, codigo):
        try:
            return self.__clientes[codigo]
        except KeyError:
            return 'Cliente não cadastrado'

    # cria novo OBJ cliente e adiciona ao dict
    def adiciona_cliente(self, codigo, nome):
        self.__clientes[codigo] = Cliente(codigo, nome)
    
    def busca_nome(self, nome):
        for key, val in self.__clientes.items():
            if val.nome == nome:
                return 'Nome: ' + str(nome) + ', Codigo: ' + str(key) 

        return 'Cliente não cadastrado'
