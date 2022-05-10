FROM registry.access.redhat.com/ubi8/python-38

USER 0
WORKDIR /src/update-gitops-task
ADD . /src/update-gitops-task
RUN chown -R 1001:0 ./
USER 1001

RUN pip install  /src/update-gitops-task
CMD ["python3"]
