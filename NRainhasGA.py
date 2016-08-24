# Clarissa SImoyama David - RA: 21015712

import random
import copy
import matplotlib.pyplot as matplot

def criaPopulacaoInicial(nrRainhas, tamanhoPopulacao):
        pop = []
        for i in range(0, tamanhoPopulacao):
            cromossomo = []
            cromossomo = random.sample(xrange(0, nrRainhas), nrRainhas)
            pop.append(cromossomo)
        return pop

def selecao(populacao, valoresFitness, fitnessObjetivo): #elitismo
    probabilide = (fitnessObjetivo * 80)/100
    for i in range(len(populacao)):
        if valoresFitness[i] > probabilide:
            return populacao[i]

def mutacao(filho):
    return troca(1, filho)


def crossover(x):
    return troca(1, x)


def getFitnessObjetivo(n):
    fitnessObjetivo = 0
    for i in range(n):
        fitnessObjetivo += i
    return fitnessObjetivo


def troca(n, alvo):
    for i in range(n):
        j = random.randint(0, len(alvo)-1)
        k = random.randint(0, len(alvo)-1)
        alvo[j], alvo[k] = alvo[k], alvo[j]
    return alvo


def algoritmoGenetico(populacao, fitness, nmax):
    n = nmax
    medias = []
    maximos = []
    fitnessObjetivo = getFitnessObjetivo(len(populacao[0]))
    print "\nTamanho do tabuleiro: ", len(populacao[0]), "x", len(populacao[0])
    print "Tamanho da populacao: ", len(populacao) 
    print "Numero maximo de geracoes: ", nmax 
    print "Fitness objetivo: ", fitnessObjetivo
    print "\nRodando..." 
    
    valoresFitness = {}
    for i in range(len(populacao)):
        valoresFitness[i] = calculaFitness(populacao[i], fitnessObjetivo)
    while n > 0: 
        novaPopulacao = []
        novosValoresFitness = {}
        a, m = getFitnessInformacoes(valoresFitness)
        medias.append(a) 
        maximos.append(m) 
        for i in range(len(populacao)):
            x = selecao(populacao, valoresFitness, fitnessObjetivo)
            filho = crossover(x)
            if random.uniform(0,1) < 0.2:
                filho = mutacao(copy.deepcopy(filho))
            filho_fitness = calculaFitness(filho, fitnessObjetivo)            
            if filho_fitness >= fitnessObjetivo: #ponto de parada
                print "...Terminado. \n\nResultado ", filho, " encontrado na geracao ", nmax-n, ".\n"
                plot(medias, maximos, fitnessObjetivo, nmax-n)
                return filho
            novosValoresFitness[i] = filho_fitness
            novaPopulacao.append(filho)
        populacao = novaPopulacao
        valoresFitness = novosValoresFitness
        n -= 1
    print "\nNao foram encontrada solucoes em ", nmax, " geracoes.\n"  
    plot(medias, maximos, fitnessObjetivo, nmax)
    return None



def calculaFitness(individuo, fitnessObjetivo):
    valorFitness = fitnessObjetivo
    for i in range(len(individuo)):
        j = 1
        while j < len(individuo)-i:
            if (individuo[i] == individuo[i+j]+j) or (individuo[i] == individuo[i+j]-j):
                valorFitness -= 1
            j += 1
    return valorFitness



def getFitnessInformacoes(valores):
    n = len(valores)
    total = 0
    for i in range(n):
        total += valores[i]
    a = total/n
    m = max(valores.values())
    return a, m 


def plot(medias, maximos, fitnessObjetivo, geracoes):
    matplot.plot(medias, 'b-')
    matplot.plot(maximos, 'r-')
    matplot.axis([0, geracoes+1, fitnessObjetivo*0.5, fitnessObjetivo*1.2])
    matplot.ylabel('media (azul), maximo (vermelho)')
    matplot.xlabel('geracoes')
    matplot.show()

if __name__ == '__main__':
    n = 8
    tamPop = 30
    nGeracoes = 500000
    populacao = criaPopulacaoInicial(n, tamPop)
    algoritmoGenetico(populacao, calculaFitness, nGeracoes)
