#!/bin/bash
pip install -r requirements.txt
cd script
python download.py
python main.py