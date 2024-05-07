# Generated by Django 5.0.4 on 2024-05-07 11:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_tutor_alter_category_options_remove_order_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('message', models.CharField(blank=True, default='', max_length=400, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='products',
            field=models.ManyToManyField(limit_choices_to={'name__in': []}, to='store.product'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='description',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]
