# Generated by Django 3.0.6 on 2020-05-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cupcakes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Calls',
            },
        ),
    ]