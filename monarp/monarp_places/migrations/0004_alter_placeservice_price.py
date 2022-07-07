# Generated by Django 4.0.6 on 2022-07-07 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monarp_places', '0003_place_is_private_place_website_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeservice',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text="in local currency only, set zero for free, don't enter if unknown", max_digits=12, null=True, verbose_name='price'),
        ),
    ]
