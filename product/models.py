from django.db import models
from django.urls import reverse
# Create your models here.

class Products(models.Model):
    product_title = models.CharField(max_length=255,verbose_name="ชื่อบทความ")
    product_image1 = models.CharField(max_length=1000,default="ใส่ลิงค์ภาพปกสินค้า",blank=True, null=True)
    product_image2 = models.CharField(max_length=1000,default="ใส่ลิงค์ภาพ1",blank=True, null=True)
    product_image3 = models.CharField(max_length=1000,default="ใส่ลิงค์ภาพ2",blank=True, null=True)
    product_details = models.CharField(max_length=255,default="ใส่รายละเอียดสินค้า")
    product_brand = models.CharField(max_length=255,verbose_name="ยี่ห้อสินค้า" ,blank=True, null=True)
    product_category =models.CharField(max_length=255,default="หมวดหมู่สินค้า")
    product_categorylv2 =models.CharField(max_length=255,default="หมวดหมู่สินค้า lv2")
    product_categorylv3 =models.CharField(max_length=255,default="หมวดหมู่สินค้า lv3")
    product_view = models.IntegerField(default=0)
    product_review = models.IntegerField(default=0)
    product_sale = models.IntegerField(default=0)
    product_price = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    shopee_link = models.CharField(max_length=1000,verbose_name="ลิงค์สินค้าใน Shopee",blank=True, null=True)
    lazada_link = models.CharField(max_length=1000,verbose_name="ลิงค์สินค้าใน Lazada",blank=True, null=True)
    homepro_link = models.CharField(max_length=1000,verbose_name="ลิงค์สินค้าใน Homepro",blank=True, null=True)
    powerbuy_link = models.CharField(max_length=1000,verbose_name="ลิงค์สินค้าใน Powerbuy",blank=True, null=True)
    JD_link = models.CharField(max_length=1000,verbose_name="ลิงค์สินค้าใน JD",blank=True, null=True)
    
    def __str__(self):
        return self.product_title
    
    def get_absolute_url(self):
        return reverse('productdetails', args=[str(self.name)])

class Category(models.Model):
    catagory_title = models.CharField(max_length=255,verbose_name="ชื่อหมวดสินค้า")
    catagory_details = models.CharField(max_length=1000,default="รายละเอียดหมวดสินค้า",blank=True, null=True)
    def __str__(self):
        return self.catagory_title