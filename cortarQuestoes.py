from PIL import Image
import numpy as np
import os

# Carregar a imagem
image_path = '/mnt/data/enem_empilhado_ordenado.png'
img = Image.open(image_path)

# Converter a imagem para um array NumPy
img_array = np.array(img)

# Definir os limites para a cor azul
blue_min = np.array([0, 0, 150])  # Limite inferior para o azul
blue_max = np.array([100, 100, 255])  # Limite superior para o azul

# Criar uma máscara para detectar os pixels azuis
blue_mask = np.all((img_array >= blue_min) & (img_array <= blue_max), axis=-1)

# Encontrar as linhas azuis na máscara
blue_indices = np.where(blue_mask)

# Identificar as coordenadas verticais das linhas azuis
blue_lines = np.unique(blue_indices[0])  # Posições horizontais (y) das linhas azuis

# Ordenar as linhas azuis (caso não estejam já ordenadas)
blue_lines.sort()

# Criar a pasta "questoes" caso não exista
output_dir = 'questoes'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterar pelas linhas azuis para cortar as questões
for i in range(len(blue_lines) - 1):
    # Determinar a área entre duas linhas azuis consecutivas
    top = blue_lines[i]
    bottom = blue_lines[i + 1]
    
    # Cortar a imagem entre essas linhas
    question_img = img.crop((0, top, img.width, bottom))  # (left, top, right, bottom)
    
    # Salvar a imagem cortada na pasta "questoes"
    question_img.save(f'{output_dir}/questao_{i + 1}.png')

    print(f"Questão {i + 1} salva em {output_dir}/questao_{i + 1}.png")
