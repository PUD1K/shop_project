# Generated by Django 4.0.4 on 2022-05-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_manufacturer_slug_subcategory_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='plural_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
