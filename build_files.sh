#!/bin/bash
pip install -r requirements-vercel.txt
python3.12 manage.py collectstatic --noinput --clear