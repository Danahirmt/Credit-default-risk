FROM continuumio/miniconda3

ADD ./environment.yml ./environment.yml

RUN conda env create -f ./environment.yml

ENV PATH /opt/conda/envs/credit/bin:$PATH
