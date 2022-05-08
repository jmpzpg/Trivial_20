# Generated by Django 3.2.8 on 2022-05-04 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0002_pregunta_tarjeta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido_paterno', models.CharField(max_length=20, verbose_name='Apellido Paterno')),
                ('apellido_materno', models.CharField(max_length=20, verbose_name='Apellido Materno')),
                ('nombres', models.CharField(max_length=20, verbose_name='Nombres')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
            ],
            options={
                'verbose_name': 'Docente',
                'verbose_name_plural': 'Docentes',
                'db_table': 'docente',
                'ordering': ['apellido_paterno', '-apellido_materno'],
            },
        ),
        migrations.RemoveField(
            model_name='pregunta',
            name='tematica_id',
        ),
        migrations.RemoveField(
            model_name='tarjeta',
            name='pregunta_id',
        ),
        migrations.RemoveField(
            model_name='tarjeta',
            name='respuesta_id',
        ),
        migrations.AddField(
            model_name='pregunta',
            name='tematica',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='juego.tematica'),
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='pregunta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='juego.pregunta'),
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='respuesta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='juego.respuesta'),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='texto',
            field=models.CharField(max_length=150),
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('creditos', models.PositiveSmallIntegerField()),
                ('docente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='juego.docente')),
            ],
        ),
    ]
