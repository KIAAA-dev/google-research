FROM continuumio/miniconda
#RUN dnf install -y python3 python3-flask python3-pip python3-setuptools
COPY ./cubert /cubert
WORKDIR /cubert
#RUN curl https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh -o anaconda.sh && chmod +x anaconda.sh && ./anaconda.sh -b
RUN conda install -y python=3.7 tensorflow=1.15 flask
RUN pip install javalang && pip install -r requirements.txt && pip install tensorflow==1.15.2 bert-tensorflow==1.0.4 numpy==1.16.0 scipy==1.5
CMD ["python", "app.py"]
