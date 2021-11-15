from django.urls import path #เลือกใช้งาน Path
from . import views #อ่านคำสั่งในไฟล์ views.py
urlpatterns = [
    path('', views.index, name='index'), #ให้เรียกใช้ฟักง์ชั่น index ในไฟล์ views.py
]