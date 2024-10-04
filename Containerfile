FROM registry.access.redhat.com/ubi9/ubi

RUN dnf install -y python3 pip && dnf clean all

RUN mkdir /app
WORKDIR /app
COPY *.* /app/

RUN pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt 

USER 1001

EXPOSE 8080
ENTRYPOINT ["python3"]

CMD [ "helloworld.py" ]