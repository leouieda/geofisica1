title: Prática 1 - Mapas, interpolação, gravidade da Terra
date: 16/09/2014
slug: pratica1
category: Gravimetria-práticas

### Objetivos:

* Aprender a gerar um mapa de algum dado geofísico
* Entender a influência da interpolação no mapa gerado
* Visualizar os dados de topografia e gravidade mundial e da América do Sul
* Discutir a relação entre os mapas gerados e o conteúdo da aula de
  [gravitação](http://www.leouieda.com/geofisica1/lessons/gravimetria/1-gravitacao.html)
* **Extra**: Gerar mapas com diferentes projeções

### Instruções

* Faça um mapa de curvas de contorno dos dados do arquivo `random-grid.txt`
* Gere mapas usando diferentes mapas de cor
* Gere mapas usando diferentes parâmetros e métodos de interpolação
* Repita o mesmo processo para o arquivo `flight-grid.txt`
* Gere um mapa do arquivos `regular-grid.txt`
* Faça mapas da topografia mundial `etopo1-0_5-mundo.gdf`
* Faça mapas da gravidade mundial `eigen-6c3sat-0_5-mundo.gdf`

Os dados devem estar presentes nos computadores do laboratório.
Estes dados podem ser baixados do
da pasta `data` do
[repositório da disciplina no Github](https://github.com/leouieda/geofisica1).
Dados de topografia e gravidade foram gerados a partir de
[modelos de harmônicos esféricos](http://en.wikipedia.org/wiki/Spherical_harmonics)
utilizando o [serviço online da ICGEM](http://icgem.gfz-potsdam.de/ICGEM/potato/Service.html).

Os dados em `random-grid.txt`, `flight-grid.txt` e `regular-grid.txt` foram
gerados com o arquivo
[notebooks/pratica1.ipynb](http://nbviewer.ipython.org/github/leouieda/geofisica1/blob/master/notebooks/pratica1.ipynb)
no
[repositório da disciplina no Github](https://github.com/leouieda/geofisica1).
Esse arquivo é um [IPython notebook](http://ipython.org/notebook.html).

