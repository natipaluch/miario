import pickle
import gym_super_mario_bros
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
import time

def rodar_demonstracao():
    arquivo_save = "melhor_mario.pkl"
    

    try:
        with open(arquivo_save, 'rb') as f:
            melhor_dna = pickle.load(f)
        print(f"★ DNA Mestre carregado! Iniciando demonstração com {len(melhor_dna)} ações.")
    except FileNotFoundError:
        print("Erro: Arquivo 'melhor_mario.pkl' não encontrado!")
        return

   
    env = gym_super_mario_bros.make('SuperMarioBros-1-1-v0', render_mode='human', apply_api_compatibility=True)
    env = JoypadSpace(env, SIMPLE_MOVEMENT)
    
    state = env.reset()
    dist_maxima = 0

  
    for i, acao in enumerate(melhor_dna):
        
        for _ in range(6):
            state, reward, term, trunc, info = env.step(acao)
            
            if info['x_pos'] > dist_maxima:
                dist_maxima = info['x_pos']
            
            env.render()
            
        
            if term or trunc:
                print(f"Fim da execução na ação {i}. Distância: {dist_maxima}m")
                env.close()
                return

    print(f"DNA finalizado! Distância total: {dist_maxima}m")
    env.close()

if __name__ == "__main__":
    rodar_demonstracao()