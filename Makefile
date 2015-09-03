CONDAENV := geo1

setup: mkenv install_requires install_fatiando

mkenv:
	conda create -n $(CONDAENV) --yes pip python=2.7

install_requires:
	bash -c "source activate $(CONDAENV) && conda install --yes --file requirements.txt"

install_fatiando:
	bash -c "source activate $(CONDAENV) && pip install --upgrade https://github.com/fatiando/fatiando/archive/master.zip"

delete_env:
	bash -c "source deactivate; conda env remove --name $(CONDAENV)"

