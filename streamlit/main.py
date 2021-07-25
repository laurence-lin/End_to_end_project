from flask import Flask

import os

import numpy as np
import pandas as pd



app = Flask(__name__)

@app.route("/", methods = ['GET'])
def main():
    return "Welcome to the first APP!"


