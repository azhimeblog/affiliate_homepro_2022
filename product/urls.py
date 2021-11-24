from django.urls import path #เลือกใช้งาน Path
from . import views #อ่านคำสั่งในไฟล์ views.py
urlpatterns = [
    path('', views.index, name='index'), 
    path('category/<str:cat_name>', views.categorys, name='categorys'), 
    path('product/<str:product_name>', views.productdetails, name='productdetails'), 
    path('policy', views.policy, name='policy'),
    path('content/top20-<str:cat_name>-most-interested', views.top20article, name='top20article'),
    path('content', views.article, name='article'),

]