# Generated by Django 3.2.9 on 2021-11-16 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20211116_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image1',
            field=models.CharField(blank=True, default='ใส่ลิงค์ภาพปกสินค้า', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_image2',
            field=models.CharField(blank=True, default='ใส่ลิงค์ภาพ1', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_image3',
            field=models.CharField(blank=True, default='ใส่ลิงค์ภาพ2', max_length=1000, null=True),
        ),
    ]