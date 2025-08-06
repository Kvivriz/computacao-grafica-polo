from pdf2image import convert_from_path
import os

pdf_path = "imgprova2024.pdf"
output_folder = "imagens"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

resolucao_dpi = 300

print(f"convertendo '{pdf_path}' para imagens com {resolucao_dpi} DPI...")

try:
    images = convert_from_path(
        pdf_path,
        dpi = resolucao_dpi,
        output_folder = output_folder,
        fmt = "png",
        paths_only = False,
    )

    for i, image in enumerate(images):
        image_filename = os.path.join(output_folder, f"pagina_enem_{i+1}.png")
        image.save(image_filename)
        printf(f"pagina {i+1} salva como '{image_filename}'")

     printf(f"\nConversão concluida! As imagens foram salvas na pasta '{output_folder}'.")
    
except Exception as e:
    print(f"Ocorreu um erro durante a conversão:v{e}")
    print("Verifique se o poppler está instalado corretamente e se o caminho do pdf está correto")