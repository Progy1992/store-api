from app import app
from app.apis.product_apis import *
from app.apis.user_apis import * 

if __name__ == '__main__':
    app.run(debug=True, port=8080)