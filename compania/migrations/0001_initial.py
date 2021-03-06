# Generated by Django 3.1.2 on 2020-10-11 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ciudad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Titulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_titulo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Empleador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empleado', models.CharField(max_length=255)),
                ('ciudad_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ciudad_empleado', to='compania.ciudad')),
                ('titulo_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titulo_empleado', to='compania.titulo')),
            ],
        ),
    ]
