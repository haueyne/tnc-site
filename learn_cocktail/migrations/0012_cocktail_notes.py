# Generated by Django 2.0.5 on 2018-05-11 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_cocktail', '0011_auto_20180511_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='注釈'),
        ),
    ]
