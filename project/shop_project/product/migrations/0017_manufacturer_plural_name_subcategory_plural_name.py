# Generated by Django 4.0.4 on 2022-05-12 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_category_plural_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='plural_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='plural_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
