# urls.py
from django.urls import path
from image_gen.views import generate_image_home 

urlpatterns = [
    path('', generate_image_home, name='generate_img'),
   
]
