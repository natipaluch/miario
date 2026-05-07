import os
import pickle
import random
import matplotlib.pyplot as plt
from individuo import Individuo

class TreinadorMario:
    def __init__(self, tamanho_pop):
        self.tamanho_pop = tamanho_pop
        self.arquivo_save = "melhor_mario.pkl"
        self.arquivo_hist = "historico_fitness.pkl"
        self.historico_fitness = self.carregar_historico()

    def carregar_historico(self):
        if os.path.exists(self.arquivo_hist):
            with open(self.arquivo_hist, 'rb') as f:
                return pickle.load(f)
        return []

    def gerar_grafico(self):
        if not self.historico_fitness: return
        plt.figure(figsize=(10, 5))
        plt.plot(self.historico_fitness, color='red', linewidth=2)
        plt.title('Evolução do Mario - Rumo ao Final da Fase')
        plt.xlabel('Geração')
        plt.ylabel('Fitness')
        plt.grid(True)
        plt.savefig('evolucao_mario.png')
        plt.close('all')

    def iniciar_treino(self, n_geracoes, n_frames, taxa_mut_base=0.15):
        populacao = [Individuo(n_frames) for _ in range(self.tamanho_pop)]
        melhor_global = 0
        geracoes_sem_melhora = 0
        
        if os.path.exists(self.arquivo_save):
            with open(self.arquivo_save, 'rb') as f:
                dna = pickle.load(f)
                # Garante que o DNA carregado caiba nos frames atuais
                dna_ajustado = dna[:n_frames] + [random.randint(0,5) for _ in range(max(0, n_frames-len(dna)))]
                populacao[0].cromossomo = list(dna_ajustado)
                print("★ Mestre carregado. Retomando evolução...")

        for g in range(n_geracoes):
        
            if geracoes_sem_melhora > 8:
                taxa_atual = 0.45 
                print(f"\n[!] Estagnado há {geracoes_sem_melhora} gens. Aplicando Mutação Crítica (45%)")
            elif geracoes_sem_melhora > 4:
                taxa_atual = taxa_mut_base * 2
            else:
                taxa_atual = taxa_mut_base

            for i, ind in enumerate(populacao):
                ind.avaliar(visualizar=False)
                print(f"Ger {g} | Ind {i+1}/{self.tamanho_pop} | Fit: {ind.nota_avaliacao:.1f} | Mut: {taxa_atual:.2f}", end="\r")

            populacao.sort(key=lambda x: x.nota_avaliacao, reverse=True)
            melhor_da_geracao = populacao[0]
            self.historico_fitness.append(melhor_da_geracao.nota_avaliacao)

            if melhor_da_geracao.nota_avaliacao > melhor_global:
                melhor_global = melhor_da_geracao.nota_avaliacao
                geracoes_sem_melhora = 0
                with open(self.arquivo_save, 'wb') as f:
                    pickle.dump(melhor_da_geracao.cromossomo, f)
                print(f"\n▶ RECORDE QUEBRADO: {melhor_global:.1f}m")
            else:
                geracoes_sem_melhora += 1
                print(f"\n▶ Ger {g} concluída. Sem recordes.")

            self.gerar_grafico()

            # Evolução
            nova_pop = [Individuo(n_frames, populacao[0].cromossomo), 
                        Individuo(n_frames, populacao[1].cromossomo)]
            
            elite = populacao[:max(3, self.tamanho_pop // 2)]
            while len(nova_pop) < self.tamanho_pop:
                p1, p2 = random.sample(elite, 2)
                filho = p1.crossover(p2).mutacao(taxa_atual)
                nova_pop.append(filho)
            populacao = nova_pop

if __name__ == "__main__":

    TREINADOR = TreinadorMario(tamanho_pop=14)
    TREINADOR.iniciar_treino(n_geracoes=200, n_frames=2000)