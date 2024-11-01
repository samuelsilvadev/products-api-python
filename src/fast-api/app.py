from fastapi import FastAPI, Response, HTTPException
from models.product import Product, ProductRequest

products = [
    Product(id=1, name='macbook', description='really great pc', price=1000.0),
    Product(id=2, name='mouse', description='really great mouse', price=10.0),
    Product(id=3, name='keyboard',
            description='really great keyboard', price=100.0)
]

app = FastAPI()


@app.get('/')
def index():
    return {'detail': 'Invalid Path'}


@app.get('/api/products')
def get_products():
    return products


@app.get('/api/products/{id}')
def get_product_by_id(id):
    for product in products:
        if product.id == int(id):
            return product

        raise HTTPException(status_code=404, detail={
                            'message': 'Product not found.'})


@app.post('/api/products')
def create_product(product: ProductRequest):
    new_product = Product(id=len(products) + 1, **product.dict())
    products.append(new_product)
    return new_product


@app.put('/api/products/{id}')
def update_product(id, updated_product: ProductRequest):
    for index, product in enumerate(products):
        if product.id == int(id):
            products[index] = Product(id=id, **updated_product.dict())
            return products[index]

        raise HTTPException(status_code=404, detail={
            'message': 'Product not found.'})


@app.delete('/api/products/{id}')
def delete_product_by_id(id):
    for product in products:
        if product.id == int(id):
            products.remove(product)
            return Response(status_code=204)

        raise HTTPException(status_code=404, detail={
            'message': 'Product not found.'})
