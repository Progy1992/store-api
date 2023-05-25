from flask import Flask, jsonify, request
from app.service.product_service import Product
from app.service.user_service import User

app = Flask(__name__)