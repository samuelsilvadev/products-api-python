from fastapi import FastAPI
from models.product import Product, ProductRequest

products = [
    Product(id=1, name='macbook', description='really great pc', price=1000.0),
    Product(id=2, name='mouse', description='really great pc', price=10.0),
    Product(id=3, name='keyboard', description='really great pc', price=100.0)
]

app = FastAPI()


@app.get('/')
def index():
    return {'detail': 'Invalid Path'}


@app.get('/api/products')
def get_products():
    return products


@app.post('/api/products')
def save_product(product: ProductRequest):
    new_product = Product(id=len(products) + 1, **product.dict())
    products.append(new_product)
    return new_product
