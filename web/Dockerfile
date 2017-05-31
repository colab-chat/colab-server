FROM python:3.5.3

#  Transfer code
RUN mkdir /colab
ADD . /colab
WORKDIR /colab

RUN pip install -r requirements.txt

CMD ["./boot.sh"]
