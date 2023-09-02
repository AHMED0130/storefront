from rest_framework.test import APIClient
from rest_framework import status
import pytest


@pytest.mark.django_db
class TestProductCreate:
    def test_if_user_is_anonymous_user_return_401(self):
        client = APIClient()
        response = client.post('/store/products/', {"title": "aa", "slug": "--",
                                                    "description": "gg", "inventory": 82, "unit_price": 79.07, "collection": 5})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_user_return_403(self):
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/store/products/', {"title": "aa", "slug": "--",
                                                    "description": "gg", "inventory": 82, "unit_price": 79.07, "collection": 5})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    
@pytest.mark.django_db
class TestProductGet:
    def test_get_products_return_200(self):
        client=APIClient()
        response=client.get('/store/products/')
        
        assert response.status_code == status.HTTP_200_OK