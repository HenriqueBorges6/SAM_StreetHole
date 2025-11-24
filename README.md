# SAM StreetHole

* `SAM_Analisys_.ipynb`: Contém os experimentos com os modelos pré-treinados, fine tune do `VIT-L`, tanto o de 8 epochs para tarefas de `BBOX` como entradas quanto com a adição de 5 epochs para tarefa de `point` como entrada, além de também o fine tune do modelo pré-treinado com 8 epochs para tarefa de `point` como entrada. Posterior aos experimentos e comparações entre os modelos temos o Grounded-SAM, modelo de segmentação para **texto** como entrada.

* `convert_polygon.py`: script para conversão das máscaras em formato de polígonos compatível com YOLOv8 para máscaras de imagem com as classes burado e não-buraco.



[Vídeo de apresentação](https://www.youtube.com/watch?v=11M7sFsoofg)

Integrantes:
* Henrique Borges
* Paula Eduarda de Lima
* Mariana Fernandes Rocha