import math

def calcIMC(peso, altura):
    valorIMC = peso / math.pow(altura, 2)
    return valorIMC

def classIMC(sexo, peso, altura):
    imc = calcIMC(peso, altura)
    if sexo == "f":
        if imc < 19.1:
            return 'Abaixo do peso' 
        elif imc >= 19.1 and imc < 25.8:
            return 'Peso normal'
        elif imc >= 25.8 and imc < 27.3:
            return 'Marginalmente acima do peso'
        elif imc >= 27.3 and imc < 32.3:
            return 'Acima do peso ideal'
        elif imc >= 32.3:
            return 'Obeso'
        else:
            return 'Erro de cálculo'
    elif sexo == 'm':
        if imc < 20.7:
            return 'Abaixo do peso'
        elif imc >= 20.7 and imc < 26.4:
            return 'Peso normal'
        elif imc >= 26.4 and imc < 27.8:
            return 'Marginalmente acima do peso'
        elif imc >= 27.8 and imc < 31.1:
            return 'Acima do peso ideal'
        elif imc >= 31.1:
            return 'Obeso'
        else:
            return 'Erro de cálculo'

def calcRCQ(cintura, quadril):
    valorRCQ = cintura / quadril
    return valorRCQ

def classRCQ(idade, sexo, cintura, quadril):
    rcq = calcRCQ(cintura, quadril)
    if sexo == 'm':
        if idade <= 29:
            if rcq < 0.83:
                return 'Baixo'
            elif rcq > 0.83 and rcq <= 0.88:
                return 'Moderado'
            elif rcq > 0.88 and rcq <= 0.94:
                return 'Alto'
            elif rcq > 0.94:
                return 'Muito Alto'
            else:
                return 'Valor Inválido.'
        elif idade > 29 and idade <= 39:
            if rcq < 0.84:
                return 'Baixo'
            elif rcq > 0.84 and rcq <= 0.91:
                return 'Moderado'
            elif rcq > 0.91 and rcq <= 0.96:
                return 'Alto'
            elif rcq > 0.96:
                return 'Muito Alto'
            else:
                return 'Valor Inválido.'
        elif idade > 39 and idade <= 49:
            if rcq < 0.88:
                return 'Baixo'
            elif rcq > 0.88 and rcq <= 0.95:
                return 'Moderado'
            elif rcq > 0.95 and rcq <= 1:
                return 'Alto'
            elif rcq > 1:
                return 'Muito Alto'
            else:
                return 'Valor Inválido.'
        elif idade > 49 and idade <= 59:
            if rcq < 0.90:
                return 'Baixo'
            elif rcq > 0.90 and rcq <= 0.96:
                return 'Moderado'
            elif rcq > 0.96 and rcq <= 1.02:
                return 'Alto'
            elif rcq > 1.02:
                return 'Muito Alto'
            else:
                return 'Valor Inválido.'
        elif idade > 59:
            if rcq < 0.91:
                return 'Baixo'
            elif rcq > 0.91 and rcq <= 0.98:
                return 'Moderado'
            elif rcq > 0.98 and rcq <= 1.03:
                return 'Alto'
            elif rcq > 1.03:
                return 'Muito Alto'
            else:
                return 'Valor Inválido.'
        else:
            return 'Idade Inválida!'
    elif sexo == 'f':
        if idade <= 29:
            if rcq < 0.71:
                return 'Baixo'
            elif rcq > 0.71 and rcq <= 0.77:
                return 'Moderado'
            elif rcq > 0.77 and rcq <= 0.82:
                return 'Alto'
            elif rcq > 0.82:
                return 'Muito Alto'
            else:
                return 'Valor Inválido.'
        elif idade > 29 and idade <= 39:
            if rcq < 0.72:
                return 'Baixo'
            elif rcq > 0.72 and rcq <= 0.78:
                return 'Moderado'
            elif rcq > 0.78 and rcq <= 0.84:
                return 'Alto'
            elif rcq > 0.84:
                return 'Muito Alto'
            else:
                return 'Valor Inválido.'
        elif idade > 39 and idade <= 49:
            if rcq < 0.73:
                return 'Baixo'
            elif rcq > 0.73 and rcq <= 0.79:
                return 'Moderado'
            elif rcq > 0.79 and rcq <= 0.87:
                return 'Alto'
            elif rcq > 0.87:
                return 'Muito Alto'
            else:
                return 'Valor Inválido.'
        elif idade > 49 and idade <= 59:
            if rcq < 0.74:
                return 'Baixo'
            elif rcq > 0.74 and rcq <= 0.81:
                return 'Moderado'
            elif rcq > 0.81 and rcq <= 0.88:
                return 'Alto'
            elif rcq > 0.88:
                return 'Muito Alto'
            else:
                return 'Valor Inválido.'
        elif idade > 59:
            if rcq < 0.76:
                return 'Baixo'
            elif rcq > 0.76 and rcq <= 0.83:
                return 'Moderado'
            elif rcq > 0.83 and rcq <= 0.90:
                return 'Alto'
            elif rcq > 0.90:
                return 'Muito Alto'
            else:
                return 'Valor Inválido.'
        else:
            return 'Idade Inválida!'
    else:
        return 'Entrada Inválida!'

def calcIAC(quadril, altura):
    valorIAC = (quadril / (altura * math.sqrt(altura))) - 18
    return valorIAC

def classIAC(sexo, quadril, altura):
    iac = calcIAC(quadril, altura)
    if sexo == 'f':
        if iac > 20 and iac <= 32:
            return 'Adiposidade Normal'
        elif iac > 32 and iac <= 38:
            return 'Sobrepeso'
        elif iac > 38:
            return 'Obesidade'
        else:
            return 'Inválido.'
    elif sexo == 'm':
        if iac > 7 and iac <= 20:
            return 'Adiposidade Normal'
        elif iac > 20 and iac <= 25:
            return 'Sobrepeso'
        elif iac > 25:
            return 'Obesidade'
        else:
            return 'Inválido.'
    else:
        return 'Entrada Inválida.'
