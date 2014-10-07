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

* [eigen-6c3stat-0_5-mundo.gdf](https://raw.githubusercontent.com/leouieda/geofisica1/master/data/eigen-6c3stat-0_5-mundo.gdf):
  Gravidade mundial. Arquivo ASCII com 4 colunas
  (lon, lat, altitude, gravidade). Malha regular com espaçamento de 0.5 grau.
  Gravidade em [mGal](http://en.wikipedia.org/wiki/Gal_%28unit%29).
  Gravidade medida na superfície da Terra.
* [etopo1-0_5-mundo.gdf](https://raw.githubusercontent.com/leouieda/geofisica1/master/data/etopo1-0_5-mundo.gdf):
  Topografia mundial. Mesmo formato que a gravidade mas
  com 3 colunas (lon, lat, altitude). Nos oceanos a altitude é negativa e
  reflete a batimetria. Em metros.

Os dados devem estar presentes nos computadores do laboratório.
Estes dados podem ser baixados do
da pasta `data` do
[repositório da disciplina no Github](https://github.com/leouieda/geofisica1).
Após clicar no nome do arquivo, selecione "Raw" para baixar os dados.

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
2. Carregue e faça um mapa da topografia mundial no `etopo1-0_5-mundo.gdf`.
3. Calcule e faça um mapa da anomalia Bouguer correta para os continentes
   (com densidade do platô de Bouguer $\rho = 2670\ kg/m^3$) e
   oceanos (com densidade de $\rho = 1000\ kg/m^3$).
    * Por que é, de maneira geral, negativa nos continentes e positiva nos
      oceanos?
    * Por que é fortemente negativa nos regiões de grandes montanhas?
    * Por que as montanhas Rochosas não apresentam anomalia ar-livre
      significativa mas apresentam anomalia Bouguer fortemente negativa?
    * Por que a anomalia Bouguer apresenta um baixo nas dorsais meso-oceânicas?

### Fórmulas e valores

Todas as fórmulas e valores foram retirados do livro de
Hofmann-Wellenhof e Moritz (2006).

A atração gravitacional causada por uma placa infinita com densidade $\rho$ e
espessura $t$ é

$$
g_{BG} = 2\pi G \rho t
$$

$G = 0.00000000006673\ m^3 kg^{-1} s^{-1}$ é a constante gravitacional.

A anomalia Bouguer é a anomalia ar-livre menos o efeito dessa placa infinita:

$$
\Delta g_{BG} = g - \gamma + 0.3086H -
\begin{cases}
    2\pi G \rho_{crosta} t                      & \text{se } t \geq 0 \\
    2\pi G (\rho_{agua} - \rho_{crosta})(-t)    & \text{se } t < 0 \\
\end{cases}
$$

Lembrando que $H$ é a altitude geométrica do ponto de observação
e $t$ é a altitude da topografia.
No caso dos oceanos ($t < 0$), devemos usar $-t$ na fórmula pois a topografia
no oceano é negativa (abaixo do elipsoide).

A fórmula Excel para calcular a gravidade da Terra Normal ($\gamma$) é:

      =100000*(6378137*9,7803253359*COS($E1)^2 + 6356752,3142*9,8321849378*SEN($E1)^2)/RAIZ(6378137^2*COS($E1)^2 + 6356752,3142^2*SEN($E1)^2)

Não se esqueçam de trocar `E1` pela coluna que corresponde a latitude em
radianos da sua planilha.

### Dicas

* Entre no [site do Peter Kovesi](http://peterkovesi.com/projects/colourmaps/)
  e escolha as escalas de cor. Os arquivos disponibilizados no site devem estar
  nos computadores do LAGEX e acessíveis pelo Oasis Montaj.
  Se não estiverem, baixem o arquivo `Geosoft.zip` do site.
  Lá estarão os arquivos com as escalas de cor.
* Cuidado com `.` e `,` para representar decimais. O Geosoft utiliza `.` mas o
  Excel em português utiliza `,`. Utilize a função "Localizar e substituir"
  do Bloco de Notas.
* Faça todas as contas em unidades do SI (kg, m, s) e depois converta para
  mGal. Para converter de $m/s^2$ para mGal, multiplique por 100000.
* Fórmulas no Excel devem começar com `=`.
* Para calcular $\pi$ no Excel, use `PI()`.


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
