# Generated by Django 3.0.6 on 2020-05-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cupcakes', '0002_calls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calls',
            name='id',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
