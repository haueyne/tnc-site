# Generated by Django 2.0.2 on 2018-04-30 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learn_cocktail', '0004_auto_20180430_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='how_to_make',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn_cocktail.HowToMake'),
        ),
    ]