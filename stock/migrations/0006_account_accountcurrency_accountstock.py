# Generated by Django 5.0.2 on 2024-02-11 13:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_stock_logo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccountCurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.account')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.currency')),
            ],
            options={
                'unique_together': {('account', 'currency')},
            },
        ),
        migrations.CreateModel(
            name='AccountStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('average_buy_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.account')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.stock')),
            ],
            options={
                'unique_together': {('account', 'stock')},
            },
        ),
    ]
