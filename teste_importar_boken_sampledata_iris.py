# -*- coding: utf-8 -*-
"""teste: importar boken.sampledata.iris

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nu1fMdCgXKRx3DYZDWCbQqUyBQrC5jsV
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random 
from boken.sampledata.iris import flowers as dados

from google.colab import files
uploaded = files.upload()

base = pd.read_csv("iris.csv") #Chamando pelo nome o arquivo: dataset
base.head() #ler

base.shape

np.random.seed(2345)

"""#Amostras aleatórias"""

random.seed()          # utilizou o horário do sistema como base
print(random.random())

x = random.random() 
print(x)

import random
print(random.randint(0, 9))

"""Nessa amostra aleatória de 100 amostras aleatorias a cada looping executado ele guarda em x uma execussão aleatória entre 0 e 1"""

random.seed(777) #a semente é 777, todo numero gerado partirá de 77
#agora o numero nao será aleatorio e se repetirá

X = [ ]  
for i in range (100):   
  X.append(random.random())

len(X) #cem numero aleatorios

X

nomes= ["Felipe", "Thais", "Carol", "Ailson", "Rodrigo"]
nomes

random.choice(nomes) #selecionando nome aleatorio

random.shuffle(nomes)#embaralhar

nomes

random.sample(nomes,3)#Pegar uma amostra dos nomes