IMAGE := credit
ROOT := $(shell dirname $(realpath $(firstword ${MAKEFILE_LIST})))
PORT := 8888
JUPYTER_KIND := lab

DOCKER_PARAMETERS := \
	--user $(shell id -u) \
	-v ${ROOT}:/Credit-default-risk \
	-w /Credit-default-risk

init:
	docker build . -t ${IMAGE} && mkdir 

jupyter:
	docker run -d --rm ${DOCKER_PARAMETERS} -e HOME=/tmp -p ${PORT}:8888 ${IMAGE} \
		bash -c "jupyter ${JUPYTER_KIND} --ip=0.0.0.0 --no-browser --NotebookApp.token=''"

