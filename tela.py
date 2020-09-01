import PySimpleGUI as sg
from reportlab.pdfgen import canvas

#Entrar com os dados do usuário e exportar em formato PDF
#(1,841.89)        (595.27,841.89)
#
#
#
#(1,1)              (595.27,1)
class TelaPython:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Nome'), sg.Input()],
            [sg.Text('Idade'), sg.Input()],
            [sg.Text('Nascimento'), sg.Input()],
            [sg.Text('Profissão'), sg.Input()],
            [sg.Text('Se defina em uma frase'), sg.Input()],
            [sg.Button('Enviad Dados')],
            [sg.Button('Gerar PDF')]
        ]

        #janela
        janela = sg.Window("Dados do Usuário").layout(layout)

        #extrair dados de tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        return(self.values)

class GerarPDF:
    def __init__(self, nome, idade, nascimento, profissao, definicao):
        self.nome = nome
        self.idade = idade
        self.nascimento = nascimento
        self.profissao = profissao
        self.definicao = definicao

    def imprimir(self):
        titulo = "Curriculo Vitae " + self.nome
        print(titulo)
        pdf = canvas.Canvas('{}.pdf'.format(titulo))
        pdf.setTitle("Curriculo Vitae ")
        pdf.setFont("Helvetica-Oblique", 14)

        pdf.drawString(30,800,"Nome: ")
        pdf.drawString(70,800, self.nome)
        pdf.drawString(245,800,"Idade")
        pdf.drawString(245,850, self.idade)
        pdf.drawString(245,900,"Data de Nascimento")
        pdf.drawString(245,950, self.nascimento)
        pdf.drawString(245,1000,"Profissão")
        pdf.drawString(245,1050, self.profissao)
        pdf.drawString(245,1100,"Minha definição pessoal")
        pdf.drawString(245,1150, self.definicao)
        
        pdf.save()

tela = TelaPython()
dados = tela.Iniciar()

pdf_final = GerarPDF(dados[0],dados[1],dados[2],dados[3],dados[4])
pdf_final.imprimir()