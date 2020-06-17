
from django.urls import path, include
from . import views 
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('item', views.ItemView)
urlpatterns = [
	path('', include(router.urls)), 
	path('', views.home, name="home"), 
]