# Generated by Django 4.0.5 on 2022-08-27 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_acerto_desconto_servico_desconto'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='acrescimo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Acréscimo'),
        ),
    ]
