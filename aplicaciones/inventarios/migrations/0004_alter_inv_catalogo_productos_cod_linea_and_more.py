# Generated by Django 4.2.3 on 2023-08-12 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventarios', '0003_alter_inv_catalogo_productos_cod_linea_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inv_catalogo_productos',
            name='cod_linea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventarios.inv_lineas_productos', verbose_name='Línea de Producto'),
        ),
        migrations.AlterField(
            model_name='inv_catalogo_productos',
            name='cod_unidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventarios.inv_unidades_medida', verbose_name='Unidad de Medida'),
        ),
    ]
