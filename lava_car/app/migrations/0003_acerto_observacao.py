# Generated by Django 4.0.2 on 2022-03-24 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_funcionario_alter_servico_data_entrada_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='acerto',
            name='observacao',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Observação'),
        ),
    ]