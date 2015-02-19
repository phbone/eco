#!/bin/sh
git clone https://github.com/phbone/eco.git
cd eco
virtualenv venv
. venv/bin/activate
pip install Flask
python hello.py