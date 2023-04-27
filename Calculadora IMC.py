from tkinter import *


class Pessoa:
    def __init__(self, altura, peso, nome, idade):
        self.altura = altura
        self.peso = peso
        self.nome = nome
        self.idade = idade

    def calcular_IMC(self):
        return self.peso / (self.altura ** 2)
    

def pegar_nome():
    nome_digitado = nome.get().strip()
    caixa_de_mensagem_nome.configure(text = nome_digitado)
    return nome_digitado
    
def pegar_peso():
    peso_digitado = round(float(peso.get().strip()), 2) 
    mensagem = "{:.2f} kg".format(peso_digitado) 
    caixa_de_mensagem_peso.configure(text=mensagem)
    return peso_digitado
def pegar_idade():
    idade_digitada = int(float(idade.get().strip()))
    mensagem = str(idade_digitada) + " anos"
    caixa_de_mensagem_idade.configure(text=mensagem) 
    return idade_digitada


def pegar_altura():
    altura_digitada = round(float(altura.get().replace(',', '.').strip()), 2)
    mensagem = "{:.2f}".format(altura_digitada) + " m/altura"
    
    caixa_de_mensagem_altura.configure(text=mensagem)
    return altura_digitada

def calcular_IMC():
    altura_digitada = pegar_altura()
    peso_digitado = pegar_peso()
    nome_digitado = pegar_nome()
    idade_digitada = pegar_idade()
    pessoa = Pessoa(altura_digitada, peso_digitado, nome_digitado, idade_digitada)
    imc = pessoa.calcular_IMC()
    #Sobrepeso
    if 25 < imc < 30:
        caixa_de_mensagem_imc.configure(text=  f'{nome_digitado}, o valor de seu IMC é: {imc:.2f}. Isto significa que você está sobrepeso. \nÉ importante ressaltar que manter um peso adequado é fundamental para prevenir uma série de doenças e complicações de saúde, \ncomo doenças cardíacas, diabetes, problemas de mobilidade e muitas outras.')
    #Obesidade grau I
    elif 30 < imc < 35:
        caixa_de_mensagem_imc.configure(text=  f'{nome_digitado}, o valor do IMC é: {imc:.2f}. Isto significa que você está com obesidade grau I. É importante ressaltar que manter um peso adequado é fundamental para prevenir uma série de doenças e complicações de saúde, como doenças cardíacas, diabetes, problemas de mobilidade e muitas outras.')
    #Obesidade grau II
    elif 35 < imc < 40:
        caixa_de_mensagem_imc.configure(text=  f'{nome_digitado}, o valor do IMC é: {imc:.2f}. Isto significa que você está com obesidade grau II. É importante ressaltar que a obesidade grau II está associada a um risco ainda maior de doenças e complicações de saúde, como doenças cardíacas, diabetes tipo 2, apneia do sono e muitas outras. É fundamental buscar ajuda médica para iniciar um plano de perda de peso saudável e controlar os fatores de risco.')
    #Obesidade grau III (obesidade mórbida)
    elif imc >= 40:
        caixa_de_mensagem_imc.configure(text=  f'{nome_digitado}, o valor do IMC é: {imc:.2f}. Isto significa que você está com obesidade grau III, também conhecida como obesidade mórbida. A obesidade grau III é uma condição séria que pode levar a uma série de doenças graves e complicações de saúde, como doenças cardíacas, diabetes tipo 2, problemas respiratórios, e muitas outras. É fundamental buscar ajuda médica imediatamente para iniciar um tratamento.')
    #Baixo peso muito grave
    elif imc < 16:
        caixa_de_mensagem_imc.configure(text= f'{nome_digitado}, o valor do IMC é: {imc:.2f}. Isto significa que você está com baixo peso muito grave. É importante ressaltar que manter um peso adequado é fundamental para prevenir uma série de doenças e complicações de saúde, como osteoporose, anemia, problemas de fertilidade e muitas outras. É fundamental buscar ajuda médica imediatamente para iniciar um tratamento adequado e controlar os fatores de risco.')
    #Baixo peso grave
    elif 16 <= imc < 17:
        caixa_de_mensagem_imc.configure(text= f'{nome_digitado}, o valor do IMC é: {imc:.2f}. Isto significa que você está com baixo peso grave. A falta de peso também pode levar a uma série de complicações de saúde, como desnutrição, problemas cardíacos e pulmonares, e muitas outras. É fundamental buscar ajuda médica para iniciar um plano alimentar adequado e controlar os fatores de risco.')
    #Baixo peso
    elif 17 <= imc < 18:
        caixa_de_mensagem_imc.configure(text= f'{nome_digitado}, o valor do IMC é: {imc:.2f}. Isto significa que você está com baixo peso, o que pode ser indicativo de uma dieta desequilibrada ou falta de nutrientes. Manter um peso adequado é fundamental para prevenir uma série de doenças e complicações de saúde. Busque ajuda médica para identificar a causa do baixo peso e iniciar um plano alimentar adequado.')
    #Peso normal
    elif 18.50 <= imc < 24.99:
        caixa_de_mensagem_imc.configure(text=  f'{nome_digitado}, o valor do IMC é: {imc:.2f}. Isto significa que você está com um peso normal. É importante ressaltar que manter um peso adequado é fundamental para prevenir uma série de doenças e complicações de saúde, como doenças cardíacas, diabetes, problemas de mobilidade e muitas outras. É fundamental manter uma alimentação equilibrada e praticar exercícios físicos regularmente para manter a saúde em dia.')
    elif imc >= 80:
        caixa_de_mensagem_imc.configure(text=  f'{nome_digitado}, por favor, digite um peso valido.')



menu = Tk()
menu.title('Calculadora de IMC')
menu.geometry('415x275+400+300')
menu.maxsize(415,275)
humano = Pessoa(None, None, None, None)



#label:
nomejanela= Label(menu, font= ('Baskerville ', 10), text= 'Nome:')
nomejanela.grid(column=0, row= 0, sticky="W")
nome = Entry(menu, width=12)
nome.grid(column=1, row= 0, sticky='W')


pesojanela = Label(menu, font= ('Baskerville', 10), text='Peso:')
pesojanela.grid(column=0, row=1, sticky='W')
peso = Entry(menu, width=12)
peso.grid(column=1, row=1, sticky='W')



idadejanela= Label(menu, font= ('Baskerville', 10), text='Idade:')
idadejanela.grid(column=0, row= 2, sticky="W")
idade = Entry(menu, width=12)
idade.grid(column= 1, row= 2, sticky='W')


alturajanela= Label(menu, font= ('Baskerville ', 10), text='Altura:')
alturajanela.grid(column=0, row= 3, sticky="W")
altura = Entry(menu, width=12)
altura.grid(column=1, row=3, sticky='W')

botão_calculo = Button(text= "Medir seu IMC", font= ('Gotham', 10), command= lambda: (pegar_peso(), pegar_nome(), calcular_IMC()))
botão_calculo.grid(column=1, row= 4,)

#coluna 3 para espaçamento


primeira_coluna = Label(text = '➡', width=2)
primeira_coluna.grid(column=2, row=0)
primeira_coluna.config(foreground='black', font=('Arial', 10, 'bold'))
segunda_coluna = Label(text = '➡', )
segunda_coluna.grid(column=2, row=1)
segunda_coluna.config(foreground='black', font=('Arial', 10, 'bold'))
terceira_coluna =Label(text = '➡', )
terceira_coluna.grid(column=2, row=2)
terceira_coluna.config(foreground='black', font=('Arial', 10, 'bold'))
quarta_coluna = Label(text = '➡', ) 
quarta_coluna.grid(column=2, row=3)
quarta_coluna.config(foreground='black', font=('Arial', 10, 'bold'))
menu.columnconfigure(2, minsize=10)


caixa_de_mensagem_nome =Label(menu, text= '', anchor=CENTER, relief= 'groove', bd= 1, width=13, foreground="red")
caixa_de_mensagem_nome.grid(column=3, row= 0,)

caixa_de_mensagem_peso =Label(menu, text= '', anchor=CENTER, relief= 'ridge', bd= 1, width=13)
caixa_de_mensagem_peso.grid(column=3, row= 1)

caixa_de_mensagem_idade=Label(menu, text= '', anchor=CENTER, relief= 'ridge', bd= 1, width=13)
caixa_de_mensagem_idade.grid(column=3, row= 2)

caixa_de_mensagem_altura=Label(menu, text= '', anchor=CENTER, relief= 'ridge', bd= 1, width=13)
caixa_de_mensagem_altura.grid(column=3, row=3)


caixa_de_mensagem_imc = Label(menu, fg='black', text='', justify=LEFT ,font=('Arial',9, 'bold'))
caixa_de_mensagem_imc.grid(column=3, row=5, sticky=W)
caixa_de_mensagem_imc.config(height=10, width=36, anchor=NW, padx=2, pady=5, wraplength=250)


menu.mainloop()





