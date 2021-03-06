# Generated by Django 3.2.4 on 2022-02-16 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=50)),
                ('about', models.CharField(max_length=300)),
                ('file', models.ImageField(upload_to='items_images')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('shipping_address', models.CharField(max_length=225, null=True)),
                ('Is_payment_success', models.CharField(choices=[('1', 'success'), ('2', 'pending'), ('3', 'processing')], default='2', max_length=10)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp1.items')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Cateogry title', max_length=100)),
                ('image', models.ImageField(upload_to='Product_image')),
            ],
            options={
                'verbose_name_plural': 'Cateogries',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_success', models.BooleanField(default=False)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp1.order')),
            ],
        ),
        migrations.AddField(
            model_name='items',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp1.products'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp1.items')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
