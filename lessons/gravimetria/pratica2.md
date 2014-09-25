title: Prática 2 - A gravidade da Terra Normal e a anomalia ar-livre
date: 16/09/2014
slug: pratica2
category: Gravimetria-práticas

### Objetivos:

* Visualizar os efeitos que a escala de cor tem na interpretação dos mapas
* Aprender a calcular a gravidade da Terra Normal e a anomalias ar-livre
* Gerar um mapa de anomalia ar-livre para o mundo todo
* Observar e entender as causas das principais feições desta anomalia

### Dados

Para esta prática usaremos o arquivo:

* `eigen-6c3sat-0_5-mundo.gdf`: Gravidade mundial. Arquivo ASCII com 4 colunas
  (lon, lat, altitude, gravidade). Malha regular com espaçamento de 0.5 grau.
  Gravidade em [mGal](http://en.wikipedia.org/wiki/Gal_%28unit%29).
  Gravidade medida na superfície da Terra.

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

### Dicas

* Entre no [site do Peter Kovesi](http://peterkovesi.com/projects/colourmaps/)
  e escolha as escalas de cor. Os arquivos disponibilizados no site devem estar
  nos computadores do LAGEX e acessíveis pelo Oasis Montaj.
  Se não estiverem, baixem o arquivo `Geosoft.zip` e peçam ajuda.
* Carregue seus dados no Excel e utilize fórmulas para calcular os
  valores das anomalias.
* Cuidado com `.` e `,` para representar decimais. O Geosoft utiliza `.` mas o
  Excel em português utiliza `,`. Utilize a função "Localizar e substituir"
  do Bloco de Notas.
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

