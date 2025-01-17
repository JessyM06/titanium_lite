# Generated by Django 4.2.3 on 2023-08-16 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_alter_adm_contactos_avisos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adm_contactos',
            name='avisos',
            field=models.BooleanField(verbose_name='Recibir Notificaciones'),
        ),
        migrations.AlterField(
            model_name='adm_contactos',
            name='mensaje',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='adm_contactos',
            name='tipo_consulta',
            field=models.IntegerField(choices=[(0, 'Consulta'), (1, 'Reclamo'), (2, 'Sugerencia'), (3, 'Comentario')], default=0, verbose_name='Tipo Consulta'),
        ),
    ]
