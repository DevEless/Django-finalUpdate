# Generated by Django 4.2.1 on 2023-07-29 23:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnonymousUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.CharField(max_length=1000)),
                ('img2', models.CharField(max_length=1000)),
                ('img3', models.CharField(max_length=1000)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('name', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('promo', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('stock', models.JSONField(default=dict)),
                ('selected_size', models.CharField(default='S', max_length=10)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('text', models.TextField(default='valeur_par_défaut', max_length=300)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('anonymous_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.anonymoususer')),
            ],
        ),
    ]
