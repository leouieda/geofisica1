title: Prática 4 - Anomalias de lugares interessantes
date: 16/09/2014
slug: pratica4

### Objetivos

* Calcular as anomalias ar-livre e Bouguer para os alvos: Havaí, Baía de
  Hudson, Andes e Japão.
* Fixar as diferenças entre os dois tipos de anomalias: como são calculadas,
  para que servem e quais suas principais causas.
* Fazer gráficos de perfis cortando as principais feições de cada alvo.
* Analisar a relação entre a topografia, anomalias e tectônica.

### Dados

Para esta prática usaremos os arquivos:

* [eigen-6c3stat-havai.gdf](https://raw.githubusercontent.com/leouieda/geofisica1/master/data/eigen-6c3stat-havai.gdf):
  Gravidade sobre as [ilhas do Havaí](https://www.google.com.br/maps/@20.5932929,-157.7151201,1358555m/data=!3m1!1e3?hl=en).
* [etopo1-havai.gdf](https://raw.githubusercontent.com/leouieda/geofisica1/master/data/etopo1-havai.gdf):
  Topografia e batimetria do Havaí.
* [eigen-6c3stat-japao.gdf](https://raw.githubusercontent.com/leouieda/geofisica1/master/data/eigen-6c3stat-japao.gdf):
  Gravidade sobre o [Japão](https://www.google.com.br/maps/@36.1346696,134.3822639,2344222m/data=!3m1!1e3?hl=en).
* [etopo1-japao.gdf](https://raw.githubusercontent.com/leouieda/geofisica1/master/data/etopo1-japao.gdf):
  Topografia e batimetria da região do Japão.
* [eigen-6c3stat-andes.gdf](https://raw.githubusercontent.com/leouieda/geofisica1/master/data/eigen-6c3stat-andes.gdf):
  Gravidade sobre o [altiplano dos Andes](https://www.google.com.br/maps/@-24.8423665,-69.6206081,2633999m/data=!3m1!1e3?hl=en).
* [etopo1-andes.gdf](https://raw.githubusercontent.com/leouieda/geofisica1/master/data/etopo1-andes.gdf):
  Topografia e batimetria da região Andina.
* [eigen-6c3stat-hudson.gdf](https://raw.githubusercontent.com/leouieda/geofisica1/master/data/eigen-6c3stat-hudson.gdf):
  Gravidade sobre as [baía de Hudson](https://www.google.com.br/maps/@59.8228665,-78.9606344,2918112m/data=!3m1!1e3?hl=en).
* [etopo1-hudson.gdf](https://raw.githubusercontent.com/leouieda/geofisica1/master/data/etopo1-hudson.gdf):
  Topografia e batimetria da baía de Hudson.

Todos os arquivos são em formato ASCII.
Arquivos da gravidade (`eigen-6c3stat-*.gdf`) possuem 4 colunas:
longitude, latitude, altitude da medição (metros) e gravidade (mGal).
Dados de gravidade foram calculados em uma malha regular
sobre a superfície da Terra.
Arquivos da topografia (`etopo1-*.gdf`) possuem 3 colunas:
longitude, latitude e altitude (da topografia/batimetria em metros).
Dados de topografia foram calculados nos mesmos pontos que os dados de
gravidade.

Para facilitar, juntei os dados de gravidade e topografia em arquivos `.csv`,
cada um com 5 colunas (nomes das colunas estão na primeira linha do arquivo):

* [havai.csv](https://raw.githubusercontent.com/leouieda/geofisica1/master/data/havai.csv)
* [japao.csv](https://raw.githubusercontent.com/leouieda/geofisica1/master/data/japao.csv)
* [andes.csv](https://raw.githubusercontent.com/leouieda/geofisica1/master/data/andes.csv)
* [hudson.csv](https://raw.githubusercontent.com/leouieda/geofisica1/master/data/hudson.csv)

Os dados devem estar presentes nos computadores do laboratório.
Estes dados podem ser baixados do
da pasta `data` do
[repositório da disciplina no Github](https://github.com/leouieda/geofisica1).
Após clicar no nome do arquivo, selecione "Raw" para baixar os dados.

Dados de topografia e gravidade foram gerados a partir de
[modelos de harmônicos esféricos](http://en.wikipedia.org/wiki/Spherical_harmonics)
utilizando o [serviço online da ICGEM](http://icgem.gfz-potsdam.de/ICGEM/potato/Service.html).

### Tarefas e perguntas

1. Calcular e fazer mapas da topografia, anomalia ar-livre e anomalia Bouguer
   para os dados do Havaí.
   Veja as fórmulas abaixo. Utilize escalas de cor divergentes.
2. Fazer gráficos da topografia, anomalia ar-livre e Bouguer para um perfil
   entre os pontos (lon, lat):
   $(197.5^\circ, 15^\circ)$ e $(207^\circ, 28^\circ)$.
    * Por que a anomalia ar-livre é positiva nas ilhas?
    * Por que a anomalia ar-livre tem seu mínimo logo ao lado das ilhas?
    * Olhando para o perfil de topografia, por que após o baixo ao lado da
      ilha há um alto na topografia antes de estabilizar entre -5000 m  e -6000
      m?
    * Como e por que as feições da anomalia ar-livre se correlacionam com a
      topografia?
    * Por que a anomalia Bouguer é sempre positiva?
    * Por que a anomalia Bouguer é menos positiva sobre as ilhas?
3. Gerar os mapas (mesmos da tarefa 1) para os dados do Japão e fazer um
   perfil entre os pontos
   $(130^\circ, 43^\circ)$ e $(148^\circ, 38^\circ)$.
    * Por que a anomalia ar-livre é praticamente zero na placa do Pacífico e no
      Mar do Japão (entre o Japão e as Coréias)?
    * Por que a anomalia ar-livre apresenta um par negativo-positivo quando
      passamos da crosta oceânica para as ilhas do Japão?
    * Explique a relação entre a anomalia ar-livre, a topografia e a subducção.
4. Gerar os mapas (mesmos da tarefa 1) para os dados dos Andes e fazer um
   perfil entre os pontos
   $(285^\circ, -22^\circ)$ e $(300^\circ, -19^\circ)$.
    * Por que a anomalia ar-livre tem seu minimo na fossa (onde está
      acontecendo a subducção)?
    * Por que a anomalia Bouguer é fortemente negativa na região das montanhas?
5. **Extra**: Gerar os mapas (mesmos da tarefa 1) para os dados da Baía Hudson
   e fazer um perfil entre os pontos
   $(260^\circ, 45^\circ)$ e $(300^\circ, 70^\circ)$.
    * Esta região está em equilíbrio isostático?
    * O que significa a anomalia Bouguer ser praticamente constante (na média)
      ao longo do perfil?
    * Por que a anomalia ar-livre fica cada vez mais negativa quando mais
      progredimos para o Norte do perfil?


### Fórmulas e valores

Todas as fórmulas e valores foram retirados do livro de
Hofmann-Wellenhof e Moritz (2006).

A fórmula Excel para calcular a gravidade da Terra Normal ($\gamma$)
usando a equação de Somigliana de 1976 é:

      =100000*(6378137*9,7803253359*COS(E1)^2 + 6356752,3142*9,8321849378*SEN(E1)^2)/RAIZ(6378137^2*COS(E1)^2 + 6356752,3142^2*SEN(E1)^2)

Não se esqueçam de trocar `E1` pela coluna que corresponde a latitude em
radianos da sua planilha.
O resultado já estará em mGal.

Para calcular o efeito do platô de Bouguer (correto para os continentes e
oceanos):

      =100000*SE(I1 > 0; 2*PI()*0,00000000006673*2670*I1; 2*PI()*0,00000000006673*(1000 - 2670)*(-I1))

Troquem `I1` pela coluna que contém os dados de topografia (do ETOPO1).
Valores calculados usando densidade $\rho=2.67\ g/cm^3$ para os continentes e
$\rho=1.00\ g/cm^3$ para a água dos oceanos.

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
* Para transformar a latitude de graus para radianos: `=A2*PI()/180`. Troque
  `A2` pela célula da latitude na sua planilha.
* Para calcular $\pi$ no Excel, use `PI()`.

### Mapas

O arquivo
[lessons/gravimetria/pratica4.ipynb](http://nbviewer.ipython.org/github/leouieda/geofisica1/blob/master/lessons/gravimetria/pratica4.ipynb)
no [repositório da disciplina no Github](https://github.com/leouieda/geofisica1)
contem os mapas das tarefas acima gerados por mim.
Utilizem esses mapas como uma referência, ou objetivo,
quando forem fazer o relatório.
**Não usem esses mapas no relatório**.
Usem os mapas que vocês mesmos fizeram.

### Referências

Hofmann-Wellenhof, B., and H. Moritz (2006), Physical Geodesy, 2nd, corr. ed.
2006 edition., Springer, Wien ; New York.
