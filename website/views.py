from flask import Blueprint, render_template, request, flash, jsonify
import json
from website.SEAP.SEAP import dataframe as df

views = Blueprint('views', __name__)

@views.route('/')#, method = ['GET'])
def home():
    return render_template('home.html', data = df)