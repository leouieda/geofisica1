title: Prática 3 - Anomalia Bouguer
date: 16/09/2014
slug: pratica3
category: Gravimetria-práticas

### Objetivos:

* Aprender a calcular a anomalia Bouguer
* Gerar um mapa de anomalia Bouguer para o mundo todo
* Observar e entender as causas das principais feições desta anomalia

### Dados

Para esta prática usaremos os arquivos:

* `eigen-6c3sat-0_5-mundo.gdf`: Gravidade mundial. Arquivo ASCII com 4 colunas
  (lon, lat, altitude, gravidade). Malha regular com espaçamento de 0.5 grau.
  Gravidade em [mGal](http://en.wikipedia.org/wiki/Gal_%28unit%29).
  Gravidade medida na superfície da Terra.
* `etopo1-0_5-mundo.gdf`: Topografia mundial. Mesmo formato que a gravidade mas
  com 3 colunas (lon, lat, altitude). Nos oceanos a altitude é negativa e
  reflete a batimetria. Em metros.

Os dados devem estar presentes nos computadores do laboratório.
Estes dados podem ser baixados do
da pasta `data` do
[repositório da disciplina no Github](https://github.com/leouieda/geofisica1).

Dados de topografia e gravidade foram gerados a partir de
[modelos de harmônicos esféricos](http://en.wikipedia.org/wiki/Spherical_harmonics)
utilizando o [serviço online da ICGEM](http://icgem.gfz-potsdam.de/ICGEM/potato/Service.html).

### Tarefas e perguntas

1. Carregue os dados de anomalia ar-livre calculados na
   [prática 2](http://www.leouieda.com/geofisica1/lessons/gravimetria-praticas/pratica2.html)
   e faça um mapa utilizando uma escala de cor divergente.
    * Revisar as principais feições da anomalia ar-livre.
    * Em que altitude foram medidos os dados de gravidade?
    * Como remover o efeito da topografia para poder investigar as estruturas
      internas da crosta?
    * Como deve ser essa correção nos oceanos?
2. Carregue e faça um mapa da topografia mundial no arquivo
   `etopo1-0_5-mundo.gdf`.
3. Calcule e faça um mapa da anomalia Bouguer correta para os continentes
   (com densidade do platô de Bouguer $\rho = 2670\ kg/m^3$) e
   oceanos.
    * Por que é, de maneira geral, negativa nos continentes e positiva nos
      oceanos?
    * Por que é fortemente negativa nos regiões de grandes montanhas?
    * Por que as montanhas Rochosas não apresentam anomalia ar-livre
      significativa mas apresentam anomalia Bouguer fortemente negativa?
    * Por que a anomalia Bouguer apresenta um baixo nas dorsais meso-oceânicas?

### Fórmulas e valores

Todas as fórmulas e valores foram retirados do livro de
Hofmann-Wellenhof e Moritz (2006).

A anomalia Bouguer é

$$
\Delta g_{BG} = \Delta g_{AL} - 2\pi G \rho H
$$

em que $\Delta g_{AL}$ é a anomalia ar-livre,
$\rho$ é a densidade do platô de Bouguer e
$G = 0.00000000006673\ m^3 kg^{-1} s^{-1}$ é a constante gravitacional.

### Dicas

* Entre no [site do Peter Kovesi](http://peterkovesi.com/projects/colourmaps/)
  e escolha as escalas de cor. Os arquivos disponibilizados no site devem estar
  nos computadores do LAGEX e acessíveis pelo Oasis Montaj.
  Se não estiverem, baixem o arquivo `Geosoft.zip` e peçam ajuda.
* Cuidado com `.` e `,` para representar decimais. O Geosoft utiliza `.` mas o
  Excel em português utiliza `,`. Utilize a função "Localizar e substituir"
  do Bloco de Notas.
* Faça todas as contas em unidades do SI (kg, m, s) e depois converta para
  mGal. Para converter de $m/s^2$ para mGal, multiplique por 100000.

### Mapas

O arquivo
[notebooks/pratica3.ipynb](http://nbviewer.ipython.org/github/leouieda/geofisica1/blob/master/notebooks/pratica3.ipynb)
no [repositório da disciplina no Github](https://github.com/leouieda/geofisica1)
contem os mapas das tarefas acima gerados por mim.
Utilizem esses mapas como uma referência, ou objetivo,
quando forem fazer o relatório.
**Não usem esses mapas no relatório**.
Usem os mapas que vocês mesmos fizeram.

### Referências

Hofmann-Wellenhof, B., and H. Moritz (2006), Physical Geodesy, 2nd, corr. ed.
2006 edition., Springer, Wien ; New York.
