# Generated by Django 3.2.8 on 2021-11-08 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stockist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockist_name', models.CharField(max_length=60)),
                ('buyer_name', models.CharField(max_length=60)),
                ('buyer_phone', models.CharField(max_length=20)),
                ('buyer_email', models.EmailField(max_length=200)),
                ('accounts_phone', models.CharField(max_length=20)),
                ('accounts_email', models.EmailField(max_length=200)),
                ('address_1', models.CharField(max_length=80)),
                ('address_2', models.CharField(blank=True, max_length=80, null=True)),
                ('town_or_city', models.CharField(max_length=35)),
                ('county_or_state', models.CharField(max_length=35)),
                ('postcode', models.CharField(max_length=12)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('purchasing_currency', models.CharField(choices=[(1, 'GBP'), (2, 'EUR')], max_length=30)),
                ('stockist_channel', models.CharField(choices=[(1, 'Pureplay Ecomm'), (2, 'Physical Only'), (3, 'Multi-Channel')], max_length=30)),
                ('stockist_market', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Women'), (2, 'Home'), (3, 'Jewellery'), (4, 'Accessories'), (5, 'Clothing'), (6, 'Gifting')], max_length=30)),
                ('website_url', models.URLField(blank=True, null=True)),
                ('categories', multiselectfield.db.fields.MultiSelectField(choices=[('jewellery', 'Jewellery'), ('leather_accessories', 'Leather Accessories'), ('blankets', 'Blankets'), ('knitted_accessories', 'Knitted Accessories'), ('clothing', 'Clothing')], max_length=30)),
                ('stockist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]