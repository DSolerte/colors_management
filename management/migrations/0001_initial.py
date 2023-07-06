# Generated by Django 4.2.3 on 2023-07-05 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('red', models.IntegerField(max_length=255)),
                ('green', models.IntegerField(max_length=255)),
                ('blue', models.IntegerField(max_length=255)),
            ],
        ),
    ]
