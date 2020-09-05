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
            [sg.Text('Nascionalidade'), sg.Input()],
            [sg.Text('Cidade'), sg.Input()],
            [sg.Text('Bairro'), sg.Input()],
            [sg.Text('Rua'), sg.Input()],
            [sg.Text('Número'), sg.Input()],
            [sg.Text('Complemento'), sg.Input()],
            [sg.Text('CEP'), sg.Input()],
            [sg.Text('Telefone Celular'), sg.Input()],
            [sg.Text('E-mail'), sg.Input()],
            [sg.Text('Motivações Pessoais'), sg.Input()],
            [sg.Text('Formação Academica (escolaridade)'), sg.Input()],
            [sg.Text('Empresa'), sg.Input()],
            [sg.Text('Cargo'), sg.Input()],
            [sg.Text('Inicio'), sg.Input()],
            [sg.Text('Fim'), sg.Input()],
            [sg.Text('Idiomas com nível'), sg.Input()],
            [sg.Text('Dados Extras'), sg.Input()],
            [sg.Button('Gerar Currículo')]
        ]

        #janela
        janela = sg.Window("Dados do Usuário").layout(layout)

        #extrair dados de tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        return(self.values)

class GerarPDF:
    def __init__(self, 
                nome, 
                idade, 
                nascimento, 
                profissao, 
                nascionalidade,
                cidade,
                bairro,
                rua,
                numero_casa,
                complemento,
                cep,
                telefone_celular,
                email,
                motivacao_pessoal,
                formacao,
                exp1_empresa,
                exp1_cargo,
                exp1_ini,
                exp1_fim,
                idioma,
                extras
                ):

        self.nome = nome
        self.idade = idade
        self.nascimento = nascimento
        self.profissao = profissao
        self.nascionalidade = nascionalidade
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero_casa = numero_casa
        self.complemento = complemento
        self.cep = cep
        self.telefone_celular = telefone_celular
        self.email = email
        self.motivacao_pessoal = motivacao_pessoal
        self.formacao = formacao
        self.exp1_empresa = exp1_empresa
        self.exp1_cargo = exp1_cargo
        self.exp1_ini = exp1_ini
        self.exp1_fim = exp1_fim
        self.idioma = idioma
        self.extras = extras

    def imprimir(self):
        titulo = "Curriculo Vitae " + self.nome
        pdf = canvas.Canvas('{}.pdf'.format(titulo))
        pdf.setTitle("Curriculo Vitae ")
        pdf.setFont("Helvetica-Oblique", 16)

        pdf.drawString(70,800, self.nome)
        pdf.setFont("Helvetica-Oblique", 14)

    
        pdf.drawString(245,850, self.idade)
        pdf.drawString(245,950, self.nascimento)
        pdf.drawString(245,1050, self.profissao)
        pdf.drawString(245,1050, self.nascionalidade)
        pdf.drawString(245,1050, self.cidade)
        pdf.drawString(245,1050, self.bairro)
        pdf.drawString(245,1050, self.rua)
        pdf.drawString(245,1050, self.numero_casa)
        pdf.drawString(245,1050, self.complemento)
        pdf.drawString(245,1050, self.cep)
        pdf.drawString(245,1050, self.telefone_celular)
        pdf.drawString(245,1050, self.email)
        pdf.drawString(245,1050, self.motivacao_pessoal)
        pdf.drawString(245,1050, self.formacao)
        pdf.drawString(245,1050, self.exp1_empresa)
        pdf.drawString(245,1050, self.exp1_cargo)
        pdf.drawString(245,1050, self.exp1_ini)
        pdf.drawString(245,1050, self.exp1_fim)
        pdf.drawString(245,1050, self.idioma)
        pdf.drawString(245,1050, self.extras)
    
        pdf.save()

tela = TelaPython()
dados = tela.Iniciar()

pdf_final = GerarPDF(dados[0],
                    dados[1],
                    dados[2],
                    dados[3],
                    dados[4],
                    dados[5],
                    dados[6],
                    dados[7],
                    dados[8],
                    dados[9],
                    dados[10],
                    dados[11],
                    dados[12],
                    dados[13],
                    dados[14],
                    dados[15],
                    dados[16],
                    dados[17],
                    dados[18],
                    dados[19],
                    dados[20])

pdf_final.imprimir()