# Generated by Django 2.2.16 on 2020-09-27 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_trasacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trasacao',
            options={'verbose_name_plural': 'Transações'},
        ),
        migrations.AlterField(
            model_name='trasacao',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='trasacao',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
