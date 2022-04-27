#Fonte: https://panda.ime.usp.br/pythonds/static/pythonds_pt/03-EDBasicos/09-ExpressoesInfixaPrefixaPosfixa.html
#Data: 27/03/2021
#Aluno: Álef da Silva Fernandes

from pythonds.basic.stack import Stack
import PySimpleGUI as sg

#Função que retorna a notação pós-fixada
def infixadaparaposfixada(expressao):
    dicionary = {}                          #Criação de um dicionário com os pesos de cada caractere
    dicionary["*"] = 3
    dicionary["/"] = 3
    dicionary["+"] = 2
    dicionary["-"] = 2
    dicionary["("] = 1
    pilhao = Stack()                        #uso de uma pilha, estrutura python
    
    listaposfixada = []
    tokenizando = expressao.split()         #transforma a entrada em uma lista
    
    for token in tokenizando:              
        if token in "0123456789":           
            listaposfixada.append(token)    #Se o caracetere for um número adiciona na lista pos-fixada
            
        elif token == '(':
            pilhao.push(token)              #Se for '(' adiciona na pilha
            
        elif token == ')':                  
            topotoken = pilhao.pop()        #Se for ')' adiciona na variavel topotoken e remove da pilha
            
            while topotoken != '(':
                listaposfixada.append(topotoken)
                
                topotoken = pilhao.pop()
                
        else:
            while (not pilhao.isEmpty()) and (dicionary[pilhao.peek()] >= dicionary[token]):
                  listaposfixada.append(pilhao.pop())
                  
            pilhao.push(token)
            

    while not pilhao.isEmpty():
        listaposfixada.append(pilhao.pop())
    return " ".join(listaposfixada)


expressaoinput = sg.popup_get_text('Digite aqui uma expressão matemática:', 'Calculadora')

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

#resultado = eval((infixadaparaposfixada(expressaoinput)))
sg.popup('Expressão pós-fixada', (infixadaparaposfixada(expressaoinput)), '\nResultado:', (postfixEval((infixadaparaposfixada(expressaoinput)))))
