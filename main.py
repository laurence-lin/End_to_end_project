from flask import Flask

import os

import numpy as np
import panda as pd



app = Flask("app")

@app.route("/", methods = ['GET'])
def main():
    return "Welcome to the first APP!"


