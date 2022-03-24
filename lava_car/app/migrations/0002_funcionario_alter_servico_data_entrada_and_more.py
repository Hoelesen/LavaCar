# Generated by Django 4.0.2 on 2022-03-24 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, default='', max_length=60, verbose_name='Nome')),
            ],
        ),
        migrations.AlterField(
            model_name='servico',
            name='data_entrada',
            field=models.DateTimeField(verbose_name='Data/Hora entrada'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='data_saida',
            field=models.DateTimeField(verbose_name='Data/Hora saída'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='itens',
            field=models.ManyToManyField(db_column='', to='app.TipoServico'),
        ),
        migrations.CreateModel(
            name='Acerto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=999, verbose_name='Valor')),
                ('valor_comissao', models.DecimalField(decimal_places=2, default=0, max_digits=999, verbose_name='Valor')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.funcionario', verbose_name='Funcionario')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.servico', verbose_name='Serviço')),
            ],
        ),
    ]