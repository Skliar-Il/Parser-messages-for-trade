#!/bin/bash 

python3 -m alembic upgrade head 

cd src

python3 -u main.py

# можно писать в docker compose черещ command: ...


