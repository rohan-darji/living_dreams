# Generated by Django 3.2.7 on 2021-10-03 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(upload_to='images')),
                ('product_name', models.CharField(max_length=50)),
                ('product_desc', models.CharField(max_length=1000)),
                ('product_price', models.IntegerField()),
            ],
        ),
    ]
