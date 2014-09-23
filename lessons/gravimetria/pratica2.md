title: Prática 2 - A gravidade da Terra Normal, anomalias ar-livre e Bouguer
date: 16/09/2014
slug: pratica2
category: Gravimetria-práticas

### Objetivos:

* Aprender a calcular a gravidade da Terra Normal e as anomalias ar-livre e
  Bouguer
* Gerar mapas de anomalia ar-livre e Bouguer para o mundo todo
* Observar as principais feições destas anomalias
* Entender como as anomalias ar-livre e Bouguer auxiliaram nosso entendimento
  da crosta e litosfera

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

1. Carregar os dados de gravidade mundial `eigen-6c3sat-0_5-mundo.gdf`
   e fazer um mapa utilizando uma escala de cor linear (ver "Dicas" abaixo).
    * Como a escala de cor influencia a percepção dos dados?
2. Calcular a gravidade da Terra Normal ($\gamma$) nos mesmos pontos
   (lat, lon) em que foram medidos os dados de gravidade.
   Utilize o elipsoide WGS84.
   Faça um mapa com esses valores utilizando a mesma escala de cor que antes.
3. Calcule a diferença $\Delta g = g - \gamma$
   entre a gravidade medida ($g$) e $\gamma$.
   Faça um mapa com a diferença utilizando uma escala de cor divergente.
    * O resultado é o que você esperava?
    * Qual é a explicação para os valores negativos nas grandes cadeias de
      montanhas?
4. Calcule a anomalia ar-livre e faça um mapa com uma escala de cor divergente.
    * Por que a anomalia ar-livre não é mais parecida com a topografia? Nós
      removemos o efeito da Terra Normal e da distância então só deveria restar
      o efeito da massa topográfica.
    * Por que é muito pequena no meio do Pacífico, Brasil e Austrália?
    * Por que é positiva e grande no Havaí?
    * Por que é negativa/positiva/negativa se traçarmos um perfil cortando os
      Andes ou Himalaias?
    * Por que apresenta um par positivo/negativo nas trincheiras?
5. Calcule e faça um mapa da anomalia Bouguer
   utilizando a correção do platô de Bouguer com densidade
   $\rho = 2670\ kg/m^3$.
    * O que acontece com a correção Bouguer nos oceanos, onde a altitude da
      medição é zero (nível do mar)?
      O que foi removido com a Terra Normal nos oceanos?
6. Calcule e faça um mapa da anomalia Bouguer correta para os continentes e
   oceanos.
    * Por que é, de maneira geral, negativa nos continentes e positiva nos
      oceanos?
    * Por que é fortemente negativa nos regiões de grandes montanhas?
    * Por que a anomalia apresenta um baixo nas dorsais meso-oceânicas?

### Fórmulas e valores

Todas as fórmulas e valores foram retirados do livro de
Hofmann-Wellenhof e Moritz (2006).

A gravidade de um elipsoide calculada na sua superfície é

$$
\gamma(\varphi) =
\frac{a \gamma_a \cos^2 \varphi + b \gamma_b \sin^2\varphi}{
      \sqrt{a^2 \cos^2 \varphi + b^2 \sin^2 \varphi}},
$$

em que $\varphi$ é a latitude, $a$ é o eixo maior do elipsoide, $b$ é o
eixo menor, $\gamma_a$ é a gravidade do elipsoide no equador e $\gamma_b$ é a
gravidade no polo.

Vamos utilizar o elipsoide de referência
[WGS84](http://en.wikipedia.org/wiki/World_Geodetic_System):

* a = 6378137 metros
* b = 6356752.3142 metros
* $\gamma_a$ = 9.7803253359 $m/s^2$
* $\gamma_b$ = 9.8321849378 $m/s^2$

A anomalia ar-livre é

$$
\Delta g_{AL} = g - \gamma_P = g - (\gamma - 0.3086H) = g - \gamma + 0.3086H
$$

em que $H$ é a altitude do ponto de observação.

A anomalia Bouguer é

$$
\Delta g_{BG} = \Delta g_{AL} - 2\pi G \rho H
$$

em que $\rho$ é a densidade do platô de Bouguer e
$G = 0.00000000006673\ m^3 kg^{-1} s^{-1}$ é a constante gravitacional.

### Dicas

* Entre no [site do Peter Kovesi](http://peterkovesi.com/projects/colourmaps/)
  e escolha as escalas de cor. Os arquivos disponibilizados no site devem estar
  nos computadores do LAGEX e acessíveis pelo Oasis Montaj.
  Se não estiverem, baixem o arquivo `Geosoft.zip` e peçam ajuda.
* Carregue seus dados no Excel e utilize fórmulas para calcular os
  valores das anomalias.
* Faça todas as contas em unidades do SI (kg, m, s) e depois converta para
  mGal. Para converter de $m/s^2$ para mGal, multiplique por 100000.
* Cuidado com `sin` e `cos`! Geralmente essas funções querem ângulos em
  radianos. Converta latitude de graus para radianos multiplicando por
  $\pi/180$.

### Mapas

O arquivo
[notebooks/pratica2.ipynb](http://nbviewer.ipython.org/github/leouieda/geofisica1/blob/master/notebooks/pratica2.ipynb)
no [repositório da disciplina no Github](https://github.com/leouieda/geofisica1)
contem os mapas das tarefas acima gerados por mim.
Utilizem esses mapas como uma referência, ou objetivo,
quando forem fazer o relatório.
**Não usem esses mapas no relatório**.
Usem os mapas que vocês mesmos fizeram.

### Referências

Hofmann-Wellenhof, B., and H. Moritz (2006), Physical Geodesy, 2nd, corr. ed.
2006 edition., Springer, Wien ; New York.

