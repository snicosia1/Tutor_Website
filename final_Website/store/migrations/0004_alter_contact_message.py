# Generated by Django 5.0.4 on 2024-05-07 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_contact_customer_products_customer_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(blank=True, default='', max_length=750, null=True),
        ),
    ]
