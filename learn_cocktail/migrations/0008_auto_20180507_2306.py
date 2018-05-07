# Generated by Django 2.0.2 on 2018-05-07 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learn_cocktail', '0007_auto_20180507_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='alc_percent',
            field=models.FloatField(default=0.0, verbose_name='度数(%)'),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='base_material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='base_material', to='learn_cocktail.Material', verbose_name='ベース原料'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='unit_of_quantity',
            field=models.CharField(choices=[('ml', 'ml'), ('tsp', 'ティースプーン')], default='ml', max_length=4, verbose_name='分量単位'),
        ),
    ]
