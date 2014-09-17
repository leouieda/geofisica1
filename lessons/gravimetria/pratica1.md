title: Prática 1 - Mapas, interpolação e a gravidade da Terra
date: 16/09/2014
slug: pratica1
category: Gravimetria-práticas

### Objetivos:

* Aprender a gerar um mapa de algum dado geofísico.
* Entender a influência da interpolação no mapa gerado.
* Entender quais interpretações podem ser feitas sobre os mapas e,
  mais importante, quais não podem.
* Visualizar os dados de gravidade mundial.
* Discutir a relação entre os mapas gerados e o conteúdo da aula de
  [gravitação](http://www.leouieda.com/geofisica1/lessons/gravimetria/1-gravitacao.html).

### Dados

Para esta prática usaremos os arquivos:

* `random-grid.txt`: Dados "fabricados". Arquivo
  [ASCII](http://en.wikipedia.org/wiki/ASCII) com 4 colunas (x, y, z, dado).
  Dados distribuídos aleatoriamente.
* `regular-grid.txt`: Versão completa dos dados fabricados. Disposto em uma
  malha regular.
* `eigen-6c3sat-0_5-mundo.gdf`: Gravidade mundial. Arquivo ASCII com 4 colunas
  (lon, lat, altitude, gravidade). Malha regular com espaçamento de 0.5 grau.
  Gravidade em [mGal](http://en.wikipedia.org/wiki/Gal_%28unit%29).
  Gravidade medida na superfície da Terra.
* `etopo1-0_5-mundo.gdf`: Topografia mundial. Mesmo formato que a gravidade mas
  com 3 colunas (lon, lat, altitude).

Os dados devem estar presentes nos computadores do laboratório.
Estes dados podem ser baixados do
da pasta `data` do
[repositório da disciplina no Github](https://github.com/leouieda/geofisica1).
Dados de topografia e gravidade foram gerados a partir de
[modelos de harmônicos esféricos](http://en.wikipedia.org/wiki/Spherical_harmonics)
utilizando o [serviço online da ICGEM](http://icgem.gfz-potsdam.de/ICGEM/potato/Service.html).
Os dados em `random-grid.txt`, `flight-grid.txt` e `regular-grid.txt` foram
gerados com o arquivo
[notebooks/pratica1.ipynb](http://nbviewer.ipython.org/github/leouieda/geofisica1/blob/master/notebooks/pratica1.ipynb).

### Tarefas e perguntas

1. Faça um mapa de curvas de contorno coloridas dos dados do arquivo `random-grid.txt`.
    * Quais são as feições gerais deste mapa?
2. Gere outros mapas do mesmo dado usando outros métodos de interpolação.
    * Como diferem os mapas gerados com diferentes métodos?
    * Onde estão as maiores diferenças?
    * *Dica*: Mostre a localização dos pontos originais nos mapas (os pontos
      aleatórios do arquivo `random-grid.txt`.
3. Gere outro mapa utilizando um valor grande (e.g., 1000 ou 1500) para o
   espaçamento do *grid*.
    * Qual mapa representa melhor "a realidade" (os dados)?
      O mapa com espaçamento pequeno (100, 200, ou 500)
      ou o mapa com espaçamento grande?
    * Como a escolha do espaçamento do  *grid* e método de interpolação
      influenciam a interpretação dos mapas?
4. Gere um mapa do arquivo `regular-grid.txt`. Estes são os dados originais
   utilizados para gerar o `random-grid.txt`.
    * Qual é a diferença entre os dados originais e os dados interpolados a
      partir de `random-grid.txt`?
    * Algum dos métodos de interpolação é capaz de representar perfeitamente os
      dados originais?
5. Faça um mapa da gravidade mundial `eigen-6c3sat-0_5-mundo.gdf`.
    * Qual é a feição mais marcante deste mapa?
    * O que causa essa feição?
    * Como a escala de cor influencia na percepção do mapa?
    * Como é a gravidade sobre as grandes montanhas (Himalaias e Andes)?
    * Por que ela é assim?
    * Como poderíamos realçar, ou focar, nas partes da gravidade que são
      causadas por feições geológicas desconhecidas? Em outras palavras, como
      isolar as partes da gravidade que são anômalas?
6. **Extra**: Faça um mapa da topografia mundial `etopo1-0_5-mundo.gdf`.
