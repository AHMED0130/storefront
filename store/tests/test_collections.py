from rest_framework.test import APIClient
from rest_framework import status
import pytest


@pytest.mark.django_db
class TestCollectionCreate:
    def test_if_user_anonamous_user_return_401(self):
        client=APIClient()
        response=client.post('/store/collections/',{'title':'x'})
        response.status_code==status.HTTP_401_UNAUTHORIZED

    def test_if_user_authintacated_user_return_403(self):
        client=APIClient()    
        client.force_authenticate(user={})
        response=client.post('/store/collections/',{'title':'x'})
        response.status_code==status.HTTP_403_FORBIDDEN

@pytest.mark.django_db   
class TestCollectionGet:
    def test_get_collection_return_200(self):
        client=APIClient()
        response=client.get('/store/collections/')
        response.status_code==status.HTTP_200_OK

