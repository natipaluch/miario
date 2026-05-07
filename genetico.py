class AlgoritmoGenetico:
    def __init__(self, tamanho_pop):
        self.tamanho_pop = tamanho_pop
        self.arquivo_save = "melhor_mario.pkl" 

    def salvar(self, dna):
        
        with open(self.arquivo_save, 'wb') as f:
            pickle.dump(dna, f)

    def carregar(self):
        
        if os.path.exists(self.arquivo_save):
            with open(self.arquivo_save, 'rb') as f:
                return pickle.load(f)
        return None

    def resolver(self, n_geracoes, n_frames, taxa_mutacao):
        
        populacao = [Individuo(n_frames) for _ in range(self.tamanho_pop)]

   
        dna_salvo = self.carregar()
        if dna_salvo:
            
            dna_ajustado = dna_salvo[:n_frames]
            while len(dna_ajustado) < n_frames:
                dna_ajustado.append(random.randint(0, 6))
            populacao[0].cromossomo = dna_ajustado

        melhor_global = 0

        for g in range(n_geracoes):
            
            for i, ind in enumerate(populacao):
                ind.avaliar_visual()
            
            
            populacao.sort(key=lambda x: x.nota_avaliacao, reverse=True)
            melhor = populacao[0]

         
            self.salvar(melhor.cromossomo)

            
            nova_pop = []
          
            nova_pop.append(Individuo(n_frames, populacao[0].cromossomo))
            nova_pop.append(Individuo(n_frames, populacao[1].cromossomo))

            
            elite = populacao[:max(3, self.tamanho_pop // 2)]
            
            
            while len(nova_pop) < self.tamanho_pop:
                pai1 = random.choice(elite)
                pai2 = random.choice(elite)
                filho = pai1.crossover(pai2)
                filho.mutacao(taxa_mutacao)
                nova_pop.append(filho)

            populacao = nova_pop
            