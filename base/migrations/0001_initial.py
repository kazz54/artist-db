# Generated by Django 2.2.4 on 2019-08-30 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('albumId', models.CharField(max_length=10)),
                ('year', models.DateField()),
                ('cover', models.ImageField(upload_to='albums/')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('cover', models.ImageField(upload_to='artists/')),
                ('bio', models.TextField()),
                ('albums', models.ManyToManyField(related_name='record', to='base.Albums')),
            ],
        ),
        migrations.AddField(
            model_name='albums',
            name='genre',
            field=models.ManyToManyField(related_name='genres', to='base.Genre'),
        ),
    ]
