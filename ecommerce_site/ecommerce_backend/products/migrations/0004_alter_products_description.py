# Generated by Django 5.1.2 on 2024-11-03 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "products",
            "0003_remove_products_category_alter_products_description_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="description",
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
    ]
