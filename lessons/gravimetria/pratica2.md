title: Prática 2 - A gravidade da Terra Normal, anomalias Ar-livre e Bouguer
date: 16/09/2014
slug: pratica2
category: Gravimetria-práticas

### Objetivos:

* Aprender a calcular a gravidade da Terra Normal e as anomalias Ar-livre e
  Bouguer
* Gerar mapas de anomalia Ar-livre e Bouguer para o mundo todo
* Observar as principais feições destas anomalias
* Entender como as anomalias Ar-livre e Bouguer auxiliaram nosso entendimento
  da crosta e litosfera

### Dados

Para esta prática usaremos os arquivos:

* `eigen-6c3sat-0_5-mundo.gdf`: Gravidade mundial. Arquivo ASCII com 4 colunas
  (lon, lat, altitude, gravidade). Malha regular com espaçamento de 0.5 grau.
  Gravidade em [mGal](http://en.wikipedia.org/wiki/Gal_%28unit%29).
  Gravidade medida na superfície da Terra.
* `etopo1-0_5-mundo.gdf`: Topografia mundial. Mesmo formato que a gravidade mas
  com 3 colunas (lon, lat, altitude). Nos oceanos a altitude é negativa e
  reflete a batimetria.

Os dados devem estar presentes nos computadores do laboratório.
Estes dados podem ser baixados do
da pasta `data` do
[repositório da disciplina no Github](https://github.com/leouieda/geofisica1).
Dados de topografia e gravidade foram gerados a partir de
[modelos de harmônicos esféricos](http://en.wikipedia.org/wiki/Spherical_harmonics)
utilizando o [serviço online da ICGEM](http://icgem.gfz-potsdam.de/ICGEM/potato/Service.html).

### Tarefas e perguntas

* Por que a anomalia Ar-livre não é mais parecida com a topografia? Nós
  removemos o efeito da Terra Normal e da distância então só deveria restar o
efeito da massa topográfica.
* Por que a anomalia Ar-livre apresenta um par positivo-negativo nas
  trincheiras?
* Por que a anomalia Ar-livre é negativa-positiva-negativa se traçarmos um
  perfil cortando os Andes ou Himalaias?
* O que acontece com a correção Bouguer nos oceanos, onde a altitude é zero? O
  que foi removido com a Terra Normal nos oceanos?
* Por que a anomalia Bouguer é negativa nos continentes e positiva nos oceanos?
* Por que a anomalia Bouguer apresenta um baixo nas dorsais meso-oceânicas?

### Mapas

O arquivo
[notebooks/pratica2.ipynb](http://nbviewer.ipython.org/github/leouieda/geofisica1/blob/master/notebooks/pratica2.ipynb)
no [repositório da disciplina no Github](https://github.com/leouieda/geofisica1)
contem os mapas das tarefas acima gerados por mim.
Utilizem esses mapas como uma referência, ou objetivo,
quando forem fazer o relatório.
Não usem esses mapas no relatório.
Vocês devem usar os mapas que vocês mesmos fizeram.
