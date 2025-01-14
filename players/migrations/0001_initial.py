# Generated by Django 5.1.4 on 2025-01-08 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First', models.CharField(max_length=50)),
                ('Last', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Players',
            },
        ),
    ]