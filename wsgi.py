# !/usr/bin/python 
# -*- coding: utf-8 -*-
from route import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8082, debug=True)