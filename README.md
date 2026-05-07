
#  Super Mario Bros - Algoritmos Genéticos

Este repositório contém o projeto de aplicação de *Algoritmos Genéticos (AG)* para o treinamento de um agente autônomo capaz de completar a fase 1-1 do jogo Super Mario Bros (NES). 

O projeto foi desenvolvido como parte de uma atividade acadêmica, focando em busca em espaço de estados e otimização evolutiva.


##  Autores
* *Nathália Paluch*
* *Lucas Enzo Valim*
* *Isabella*
* *Leonidas*


##  Visão Geral do Projeto

O agente utiliza uma representação cromossômica para sequenciar comandos que maximizam o progresso horizontal do Mario. Através de gerações, o algoritmo seleciona os melhores indivíduos e aplica cruzamento e mutação para superar obstáculos e buracos.

###  Detalhes Técnicos
* *Cromossomo:* 2200 genes (cada gene = 1 ação).
* *Frame Skipping:* 6 frames por ação .
* *Espaço de Ação:* SIMPLE_MOVEMENT (7 ações básicas do Mario).
* *Fitness:*
    $$Fitness = D_{max} - P_{morte} + B_{eficiência}$$


##  Como fazer funcionar

### 1. Pré-requisitos
Certifique-se de ter o *Python 3.8* ou *3.9* instalado. Versões mais recentes podem ter conflitos com a biblioteca nes-py.

### 2. Instalação das Dependências
Abra o terminal na pasta do projeto e execute os comandos abaixo para instalar o ambiente do jogo e as bibliotecas de simulação:

bash
# Instalação das bibliotecas principais
pip install gym-super-mario-bros==7.4.0 nes-py

### 3. Executando o Projeto
   Para iniciar o processo de treinamento e evolução:
   Bash
    python train_model.py
