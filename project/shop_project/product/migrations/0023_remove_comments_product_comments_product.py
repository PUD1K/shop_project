# Generated by Django 4.0.4 on 2022-05-28 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_alter_comments_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='product',
        ),
        migrations.AddField(
            model_name='comments',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.product'),
        ),
    ]
