from flask import Flask, redirect, url_for, request


app = Flask(__name__)

from app import views
