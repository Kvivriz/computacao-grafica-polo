import os
import shutil
from pathlib import Path
import re

def juntar_e_renomear_por_idioma():
    pasta_origem = "todas_questoes"
    pastas_destino = {
        "ingles": "questoes_ingles",
        "espanhol": "questoes_espanhol", 
        "portugues": "questoes_portugues"
    }
    
    # Cria pastas destino se não existirem
    for pasta in pastas_destino.values():
        os.makedirs(pasta, exist_ok=True)
    
    # Verifica se pasta origem existe
    if not os.path.exists(pasta_origem):
        print(f"❌ Pasta '{pasta_origem}' não encontrada!")
        return
    
    # Lista todas as imagens
    imagens = []
    for arquivo in os.listdir(pasta_origem):
        if arquivo.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')):
            imagens.append(arquivo)
    
    # Função para ordenação natural (1, 2, 3, ..., 10, 11, ...)
    def natural_sort_key(text):
        return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', text)]
    
    # Ordena as imagens numericamente
    imagens.sort(key=natural_sort_key)
    
    print("📊 Imagens ordenadas:")
    for i, img in enumerate(imagens, 1):
        print(f"  {i:2d}. {img}")
    print()
    
    contadores = {
        "ingles": 1,
        "espanhol": 1, 
        "portugues": 6
    }
    
    total_imagens = len(imagens)
    
    print(f"📊 Total de imagens encontradas: {total_imagens}")
    print("📁 Iniciando organização por idioma...\n")
    
    for i, imagem in enumerate(imagens, 1):
        extensao = Path(imagem).suffix
        origem = os.path.join(pasta_origem, imagem)
        
        # Define o grupo baseado na posição da imagem
        if i <= 5:
            # Primeiras 5 imagens: Inglês
            grupo = "ingles"
            nome_destino = f"questao_{contadores[grupo]}_ingles{extensao}"
        elif i <= 10:
            # Imagens 6 a 10: Espanhol
            grupo = "espanhol"
            nome_destino = f"questao_{contadores[grupo]}_espanhol{extensao}"
        else:
            # Demais imagens: Português
            grupo = "portugues"
            nome_destino = f"questao_{contadores[grupo]}{extensao}"
        
        destino = os.path.join(pastas_destino[grupo], nome_destino)
        
        # Copia a imagem
        shutil.copy2(origem, destino)
        print(f"#{i:02d} 📂 {imagem} -> {pastas_destino[grupo]}/{nome_destino}")
        
        contadores[grupo] += 1
    
    print(f"\n✅ Organização concluída!")
    print(f"📚 Inglês: {contadores['ingles']-1} imagens (questões 1-5)")
    print(f"📚 Espanhol: {contadores['espanhol']-1} imagens (questões 6-10)") 
    print(f"📚 Português: {contadores['portugues']-1} imagens (questões 11-{total_imagens})")

# Versão que lê os números dos arquivos originais
def juntar_e_renomear_preservando_numeros():
    pasta_origem = "todas_questoes"
    pastas_destino = {
        "ingles": "questoes_ingles",
        "espanhol": "questoes_espanhol", 
        "portugues": "questoes_portugues"
    }
    
    # Cria pastas destino
    for pasta in pastas_destino.values():
        os.makedirs(pasta, exist_ok=True)
    
    if not os.path.exists(pasta_origem):
        print(f"❌ Pasta '{pasta_origem}' não encontrada!")
        return
    
    # Lista e ordena imagens numericamente
    imagens = []
    for arquivo in os.listdir(pasta_origem):
        if arquivo.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')):
            imagens.append(arquivo)
    
    # Ordenação natural que funciona com números
    def extract_number(filename):
        # Tenta encontrar números no nome do arquivo
        numbers = re.findall(r'\d+', filename)
        return int(numbers[0]) if numbers else 0
    
    imagens.sort(key=extract_number)
    
    print("🔢 Imagens ordenadas por número:")
    for img in imagens:
        print(f"  - {img}")
    print()
    
    contadores = {
        "ingles": 1,
        "espanhol": 1, 
        "portugues": 1
    }
    
    total_imagens = len(imagens)
    
    print(f"📊 Processando {total_imagens} imagens...\n")
    
    for i, imagem in enumerate(imagens, 1):
        extensao = Path(imagem).suffix
        origem = os.path.join(pasta_origem, imagem)
        
        # Extrai o número original do arquivo
        numero_original = extract_number(imagem)
        
        # Define o grupo baseado na posição
        if i <= 5:
            grupo = "ingles"
            nome_destino = f"questao_{contadores[grupo]}_ingles{extensao}"
        elif i <= 10:
            grupo = "espanhol"
            nome_destino = f"questao_{contadores[grupo]}_espanhol{extensao}"
        else:
            grupo = "portugues"
            nome_destino = f"questao_{contadores[grupo]}{extensao}"
        
        destino = os.path.join(pastas_destino[grupo], nome_destino)
        
        shutil.copy2(origem, destino)
        print(f"#{i:02d} 📂 {imagem} (nº{numero_original}) -> {nome_destino}")
        
        contadores[grupo] += 1
    
    print(f"\n✅ Organização concluída!")
    print(f"📚 Inglês: {contadores['ingles']-1} imagens")
    print(f"📚 Espanhol: {contadores['espanhol']-1} imagens")
    print(f"📚 Português: {contadores['portugues']-1} imagens")

# Executar
if __name__ == "__main__":
    print("🌐 ORGANIZADOR DE QUESTÕES POR IDIOMA")
    print("=" * 50)
    
    print("Escolha o método de ordenação:")
    print("1 - Ordenação natural (recomendado)")
    print("2 - Ordenação por números extraídos")
    
    opcao = input("Digite 1 ou 2: ").strip()
    
    if opcao == "1":
        juntar_e_renomear_por_idioma()
    elif opcao == "2":
        juntar_e_renomear_preservando_numeros()
    else:
        print("Opção inválida! Usando ordenação natural...")
        juntar_e_renomear_por_idioma()