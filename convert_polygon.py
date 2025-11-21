import os
import cv2
import numpy as np

# pastas
pasta_imagens = "Data Segmentation/train/images/"
pasta_labels = "Data Segmentation/train/labels"
pasta_saida = "Data Segmentation/masks/"
os.makedirs(pasta_saida, exist_ok=True)

def carregar_poligono(caminho_txt):
    with open(caminho_txt, "r") as f:
        linha = f.readline().strip().split()
    # remove class_id
    coords = list(map(float, linha[1:]))
    # pares (x, y)
    pontos = [(coords[i], coords[i+1]) for i in range(0, len(coords), 2)]
    return pontos

for nome_txt in os.listdir(pasta_labels):
    if not nome_txt.endswith(".txt"):
        continue

    caminho_txt = os.path.join(pasta_labels, nome_txt)
    nome_base = nome_txt.replace(".txt", "")

    # imagem correspondente
    img_path = os.path.join(pasta_imagens, nome_base + ".jpg")
    if not os.path.exists(img_path):
        img_path = os.path.join(pasta_imagens, nome_base + ".png")
        if not os.path.exists(img_path):
            continue  # pula se não achar imagem

    img = cv2.imread(img_path)
    h, w = img.shape[:2]

    # carregar polígono normalizado
    poligono_normalizado = carregar_poligono(caminho_txt)

    # converter para coordenadas da imagem
    poligono = []
    for x, y in poligono_normalizado:
        px = int(x * w)
        py = int(y * h)
        poligono.append([px, py])

    poligono = np.array([poligono], dtype=np.int32)

    # criar máscara vazia
    mask = np.zeros((h, w), dtype=np.uint8)

    # preencher o polígono
    cv2.fillPoly(mask, poligono, 255)

    # salvar
    out_path = os.path.join(pasta_saida, nome_base + "_mask.png")
    cv2.imwrite(out_path, mask)
