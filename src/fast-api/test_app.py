from fastapi.testclient import TestClient
from app import app
from models.product import ProductRequest

client = TestClient(app)


def test_index():
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'detail': 'Invalid Path'}


def test_get_products():
    response = client.get('/api/products')
    parsed_response = response.json()

    assert response.status_code == 200
    assert parsed_response[0]['id'] == 1
    assert parsed_response[0]['name'] == 'macbook'
    assert parsed_response[0]['description'] == 'really great pc'
    assert parsed_response[0]['price'] == 1000.0


def test_get_product_by_id():
    response = client.get('/api/products/1')
    parsed_response = response.json()

    assert response.status_code == 200
    assert parsed_response['id'] == 1
    assert parsed_response['name'] == 'macbook'
    assert parsed_response['description'] == 'really great pc'
    assert parsed_response['price'] == 1000.0


def test_get_product_by_id_with_not_found():
    response = client.get('/api/products/100')
    parsed_response = response.json()

    assert response.status_code == 404
    assert parsed_response['detail']['message'] == 'Product not found.'


def test_create_product():
    response = client.post(
        '/api/products', json={'name': 'amazing new product', 'description': 'amazing description', 'price': 1})
    parsed_response = response.json()

    assert response.status_code == 200
    assert parsed_response['id'] == 4
    assert parsed_response['name'] == 'amazing new product'
    assert parsed_response['description'] == 'amazing description'
    assert parsed_response['price'] == 1.0

    response = client.get('/api/products')
    parsed_products_response = response.json()
    last_product = parsed_products_response[len(parsed_products_response) - 1]

    assert last_product['id'] == 4


def test_update_product():
    response = client.get('/api/products')
    parsed_products_response = response.json()

    assert parsed_products_response[0]['id'] == 1
    assert parsed_products_response[0]['name'] == 'macbook'

    response = client.put('/api/products/1', json={
                          'name': 'updated macbook', 'description': 'updated description', 'price': 2})
    parsed_response = response.json()

    assert response.status_code == 200
    assert parsed_response['id'] == 1
    assert parsed_response['name'] == 'updated macbook'


def test_update_product_with_not_found():
    response = client.put('/api/products/100', json={
        'name': 'updated macbook', 'description': 'updated description', 'price': 2})
    parsed_response = response.json()

    assert response.status_code == 404
    assert parsed_response['detail']['message'] == 'Product not found.'


def test_delete_product_successfully():
    response = client.delete('/api/products/1')

    assert response.status_code == 204


def test_delete_product_with_not_found():
    response = client.delete('/api/products/100')
    parsed_response = response.json()

    assert response.status_code == 404
    assert parsed_response['detail']['message'] == 'Product not found.'
