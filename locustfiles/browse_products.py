from locust import HttpUser,task,between
from random import randint

class ProductUsers(HttpUser):

    wait_time=between(1,5)
    
    @task(2)
    def get_products(self):
        collection_id=randint(1,10)
        self.client.get(f'/store/products/?collection_id={collection_id}',
                        name='store/products')
        
    @task(4)
    def get_product_details(self):
        product_id=randint(1,1000)
        self.client.get(f'/store/products/{product_id}',
                        name='store/products/:id')
        

    @task(1)
    def add_product_to_carts(self):
        product_id=randint(1,10)
        self.client.post(f'/store/carts/{self.cart_id}/items',
                         name='/store/carts/items',
                         json={"product_id":product_id,"quantity":4})


    def on_start(self):
        response=self.client.post('/store/carts')
        result=response.json()
        self.cart_id=result['id']



