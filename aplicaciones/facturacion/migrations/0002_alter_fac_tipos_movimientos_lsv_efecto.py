# Generated by Django 4.2.3 on 2023-08-10 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fac_tipos_movimientos',
            name='lsv_efecto',
            field=models.CharField(choices=[('+', 'Aumenta Existencias'), ('-', 'Disminuye Existencias')], default='+', max_length=1, verbose_name='Efecto del Movimiento'),
        ),
    ]
