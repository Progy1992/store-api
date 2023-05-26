from flask import Flask, jsonify, request
from app.service.product_service import Product
from app.service.user_service import User
from flask_cors import CORS

app = Flask(__name__)
CORS(app)