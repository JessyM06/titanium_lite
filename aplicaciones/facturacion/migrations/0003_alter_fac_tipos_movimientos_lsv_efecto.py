# Generated by Django 4.2.3 on 2023-08-12 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0002_alter_fac_tipos_movimientos_lsv_efecto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fac_tipos_movimientos',
            name='lsv_efecto',
            field=models.CharField(choices=[('+', 'Aumenta Saldo'), ('-', 'Disminuye Saldo')], default='+', max_length=1, verbose_name='Efecto del Movimiento'),
        ),
    ]
