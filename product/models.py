from django.db import models
from django_resized import ResizedImageField
# Create your models here.

class Products(models.Model):
    product_title = models.CharField(max_length=255,verbose_name="ชื่อบทความ")
    product_image1 = ResizedImageField(size=[500, 300],crop=['middle', 'center'],upload_to="movie", blank=True, null=True)
    product_image2 = ResizedImageField(size=[500, 300],crop=['middle', 'center'],upload_to="movie", blank=True, null=True)
    product_image3 = ResizedImageField(size=[500, 300],crop=['middle', 'center'],upload_to="movie", blank=True, null=True)
    product_details = models.CharField(max_length=255,default="ใส่รายละเอียดสินค้า")
    product_category =models.CharField(max_length=255,default="หมวดหมู่สินค้า")
    product_categorylv2 =models.CharField(max_length=255,default="หมวดหมู่สินค้า lv2")
    product_categorylv3 =models.CharField(max_length=255,default="หมวดหมู่สินค้า lv3")
    product_view = models.IntegerField(default=0)
    product_review = models.IntegerField(default=0)
    product_sale = models.IntegerField(default=0)
    product_price = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    shopee_link = models.CharField(max_length=1000,verbose_name="ลิงค์สินค้าใน Shopee",null=True)
    lazada_link = models.CharField(max_length=1000,verbose_name="ลิงค์สินค้าใน Lazada",null=True)
    homepro_link = models.CharField(max_length=1000,verbose_name="ลิงค์สินค้าใน Homepro",null=True)
    powerbuy_link = models.CharField(max_length=1000,verbose_name="ลิงค์สินค้าใน Powerbuy",null=True)
    JD_link = models.CharField(max_length=1000,verbose_name="ลิงค์สินค้าใน JD",null=True)
    
    def __str__(self):
        return self.product_title