# Generated by Django 3.2.8 on 2021-10-15 10:15

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('friendly_name', models.CharField(max_length=90)),
                ('product_type', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Earrings'), (2, 'Pendants / Necklaces'), (3, 'Rings'), (4, 'Bracelets / Bangles'), (5, 'Tops'), (6, 'Knitwear'), (7, 'Skirts'), (8, 'Shorts'), (9, 'Trousers'), (10, 'Jeans'), (11, 'Ponchos'), (12, 'Beanie Hats'), (13, 'Scarves'), (14, 'Beanie Hats'), (15, 'Leather Bags'), (16, 'Beltbags / Bumbags'), (17, 'Wallets / Purses'), (18, 'Belts')], default='Earrings', max_length=3, verbose_name='Type')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=90)),
                ('product_properties', multiselectfield.db.fields.MultiSelectField(choices=[('SS', 'sterling silver'), ('GP', 'gold plated'), ('PW', 'wool'), ('HC', 'hand crafted'), ('FP', 'fairly produced'), ('LI', 'low environmental impact')], default='FP', max_length=11)),
                ('product_sku', models.CharField(max_length=90)),
                ('product_description', models.TextField()),
                ('product_is_bestseller', models.BooleanField(default=False)),
                ('ring_size_matrix', models.BooleanField(blank=True, default=False, null=True)),
                ('clothing_size_matrix', models.BooleanField(blank=True, default=False, null=True)),
                ('one_size', models.BooleanField(blank=True, default=True, null=True)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rrp_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image_url', models.URLField(max_length=1024)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('friendly_name', models.CharField(max_length=90)),
                ('product_categories', models.CharField(choices=[('jewellery', 'Jewellery'), ('leather_accessories', 'Leather Accessories'), ('blankets', 'Blankets'), ('knitted_accessories', 'Knitted Accessories'), ('clothing', 'Clothing')], max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Product Types',
            },
        ),
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product')),
                ('clothing_sizes', multiselectfield.db.fields.MultiSelectField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], default='XS', max_length=11)),
            ],
            bases=('products.product',),
        ),
        migrations.CreateModel(
            name='Ring',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product')),
                ('jewellery_properties', models.CharField(choices=[('SR', 'silver'), ('GD', 'gold')], max_length=2)),
                ('ring_sizes', multiselectfield.db.fields.MultiSelectField(choices=[('6', 'L'), ('7', 'N'), ('8', 'P'), ('9', 'S'), ('10', 'U')], default='6', max_length=11)),
            ],
            bases=('products.product',),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.type'),
        ),
    ]
