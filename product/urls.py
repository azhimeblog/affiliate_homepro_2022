from django.urls import path #เลือกใช้งาน Path
from . import views #อ่านคำสั่งในไฟล์ views.py
urlpatterns = [
    path('', views.index, name='index'), 
    path('category/<str:cat_name>', views.categorys, name='categorys'), 
    path('product/<str:product_name>', views.productdetails, name='productdetails'), 
    path('policy', views.policy, name='policy'),

]