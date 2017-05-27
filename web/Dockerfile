FROM python:3.5.3

#  Transfer code
RUN mkdir /colab
ADD . /colab
WORKDIR /colab

# Install dependencies
RUN pip install -r requirements.txt

# Set up port an run
CMD ["./boot.sh"]
