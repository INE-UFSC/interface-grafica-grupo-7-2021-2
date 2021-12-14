import PySimpleGUI as sg 

# View do padrão MVC
class ClienteView():
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window("Consulta de clientes", self.__container ,font=("Helvetica", 14))

    def tela_consulta(self):
        #FIX ME - implementar a GUI e colocar em self.__container
        
        self.__container = [
            [sg.Text('Digite o código ou o nome do cliente e clique na ação desejada:')],
            [sg.Text('Nome:   '), sg.InputText(key='nome', size=(45, 1))],
            [sg.Text('Código: '), sg.InputText(key='codigo', size=(45, 1))],
            [sg.Button('Cadastrar'), sg.Button('Consultar')],
            [sg.Text('', key='feedback')]
        ]
        self.__window = sg.Window("Consulta de clientes", self.__container ,font=("Helvetica", 14))

    def mostra_resultado(self, resultado): 
        self.__window.Element('resultado').Update(resultado)

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
