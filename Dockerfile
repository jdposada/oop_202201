FROM jupyter/minimal-notebook:python-3.9.7

# Install Python packages
COPY requirements.txt /home/jovyan/requirements.txt 
RUN conda install -y --file /home/jovyan/requirements.txt

RUN conda create -n tox_env -c conda-forge -y python=3.8 tox
