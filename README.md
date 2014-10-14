# Geofísica 1 - Gravimetria e magnetometria

http://leouieda.com/geofisica1

Material para o curso "Geofísica 1" da graduação em Geologia da
[Universidade do Estado do Rio de Janeiro](http://www.uerj.br/).

Este repositório contem as fontes para compilar o site,
lições teóricas,
instruções para as atividades práticas,
dados e [IPython notebooks](http://ipython.org/notebook.html) para as práticas.

## Compilar o site

O site é gerado pelo sistema [Pelican](http://docs.getpelican.com/).

Requisitos para compilação:

* Pelican (3.4.0)
* markdown (2.4)
* pillow
* beautifulsoup4
* nodejs

Para instalar as componentes em Python (todos menos nodejs):

    pip install pelican==3.4.0 markdown==2.4 pillow beautifulsoup4

Para instalar nodejs no Ubuntu:

    sudo apt-get install nodejs

Entre no repositório e use o `Makefile` para compilar o HTML do site:

    cd geofisica1
    make
    make serve

O comando `make serve` iniciará um servidor na pasta `output` onde estão os
arquivos HTML gerados.
Abra um navegador e vá para `http://127.0.0.1:8003` para visualizar o site.
Use Ctrl+C para interromper o servidor.

## Atualização automática usando TravisCI

Este site é compilado automaticamente quando um novo *commit* é empurrado para
o *master*.
Veja os arquivos `.travis.yml` e `.update-website.sh`.
Inspirado nas mágicas por
[Sleepy Coders](http://sleepycoders.blogspot.com.au/2013/03/sharing-travis-ci-generated-files.html)
e
[Mathieu Leplatre](http://blog.mathieu-leplatre.info/publish-your-pelican-blog-on-github-pages-via-travis-ci.html).

[![TravisCI status](http://img.shields.io/travis/leouieda/geofisica1.svg?style=flat)](https://travis-ci.org/leouieda/geofisica1)

## License

[![Creative Commons
License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
This work is licensed under a
[Creative Commons Attribution 4.0 International
License](http://creativecommons.org/licenses/by/4.0/).

