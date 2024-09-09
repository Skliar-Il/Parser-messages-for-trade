FROM python:3.12

RUN mkdir /telegram_parser

WORKDIR /telegram_parser

COPY req.txt .

RUN pip install --user -r req.txt 

COPY . . 

RUN chmod +x docker/*.sh

# WORKDIR src

# ENV PATH=/root/.local:$PATH

# CMD python -u main.py