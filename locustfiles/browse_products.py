from locust import HttpUser, task, between, events
from random import randint
import requests

class ProductUsers(HttpUser):

    wait_time = between(1, 5)
    cart_id = None

    @task(2)
    def get_products(self):
        collection_id = randint(1, 10)
        self.client.get(f'/store/products/?collection_id={collection_id}',
                        name='store/products')

    @task(4)
    def get_product_details(self):
        product_id = randint(1, 1000)
        self.client.get(f'/store/products/{product_id}',
                        name='store/products/:id')

    @task(1)
    def add_product_to_carts(self):
        if not self.cart_id:
            print("Cart ID is not initialized. Make sure on_start is executed.")
            return

        product_id = randint(1, 10)
        self.client.post(f'/store/carts/{self.cart_id}/items',
                         name='/store/carts/items',
                         json={"product_id": product_id, "quantity": 4})

    def on_start(self):
        response = self.client.post('/store/carts')

        try:
            result = response.json()
            self.cart_id = result['id']
        except requests.exceptions.JSONDecodeError:
            print(f"Failed to parse JSON from response: {response.text}")
            ProductUsers.cart_id = "e32bc2cd-b31b-48c1-bbba-6d52f1a7d65c"  

# Register an event to check if on_start is being called
@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    print("Locust initialized")
