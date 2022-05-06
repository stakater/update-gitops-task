frOM registry.access.redhat.com/ubi7/python-38

USER 0
WORKDIR /src/update-gitops-task
ADD . /src/update-gitops-task
RUN chown -R 1001:0 ./
USER 1001

RUN pip install  /src/update-gitops-task
RUN git config http.postBuffer 524288000
CMD ["python3"]
