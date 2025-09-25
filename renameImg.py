import os
import shutil
from pathlib import Path

def juntar_e_renomear():
    pastas_origem = ["questoes", "questoes2", "questoes3"]
    pasta_destino = "todas_questoes"
    
    # Cria pasta destino se não existir
    os.makedirs(pasta_destino, exist_ok=True)
    
    contador = 1
    
    for pasta in pastas_origem:
        if not os.path.exists(pasta):
            print(f"Pasta '{pasta}' não encontrada!")
            continue
            
        # Lista e ordena imagens
        imagens = []
        for arquivo in os.listdir(pasta):
            if arquivo.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')):
                imagens.append(arquivo)
        
        imagens.sort()
        
        # Copia e renomeia para pasta única
        for imagem in imagens:
            extensao = Path(imagem).suffix
            origem = os.path.join(pasta, imagem)
            destino = os.path.join(pasta_destino, f"questao_{contador:03d}{extensao}")
            
            shutil.copy2(origem, destino)
            print(f"📂 {pasta}/{imagem} -> {pasta_destino}/questao_{contador:03d}{extensao}")
            contador += 1
    
    print(f"\n✅ {contador-1} imagens copiadas para '{pasta_destino}' em ordem sequencial!")

# Executar
juntar_e_renomear()