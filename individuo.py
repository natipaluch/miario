import random
import gym_super_mario_bros
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

class Individuo:
    def __init__(self, n_frames, cromossomo=None):
        self.n_frames = n_frames
        self.nota_avaliacao = 0
        if cromossomo:
            self.cromossomo = list(cromossomo)
        else:
          
            self.cromossomo = [random.randint(0, 5) for _ in range(n_frames)]

    def avaliar(self, visualizar=False):
        modo = 'human' if visualizar else None
        env = gym_super_mario_bros.make('SuperMarioBros-1-1-v0', render_mode=modo, apply_api_compatibility=True)
        env = JoypadSpace(env, SIMPLE_MOVEMENT)
        
        env.reset()
        dist_maxima = 0
        frames_vividos = 0
        morreu = False

        for acao in self.cromossomo:
            for _ in range(6):
                state, reward, term, trunc, info = env.step(acao)
                frames_vividos += 1
                
                if info['x_pos'] > dist_maxima:
                    dist_maxima = info['x_pos']
                
                if visualizar: env.render()
                if term:
                    morreu = True
                    break
            if morreu or trunc: break

        env.close()

   
        fitness = dist_maxima
        
      
        if morreu:
            fitness -= 500
        

        eficiencia = dist_maxima / frames_vividos if frames_vividos > 0 else 0
        fitness += eficiencia * 100

        self.nota_avaliacao = max(0, fitness)

    def mutacao(self, taxa):
        for i in range(self.n_frames):
            if random.random() < taxa:
               
                if random.random() < 0.8:
                    self.cromossomo[i] = random.choice([2, 3, 4]) 
                else:
                    self.cromossomo[i] = random.randint(0, 5)
        return self

    def crossover(self, outro):
        p1 = random.randint(1, self.n_frames // 2)
        p2 = random.randint(p1, self.n_frames - 1)
        dna_filho = self.cromossomo[:p1] + outro.cromossomo[p1:p2] + self.cromossomo[p2:]
        return Individuo(self.n_frames, dna_filho)