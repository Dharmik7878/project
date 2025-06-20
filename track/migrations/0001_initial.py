# Generated by Django 5.1.4 on 2025-03-18 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=20)),
                ('tracknumber', models.CharField(max_length=9)),
                ('status', models.CharField(max_length=10)),
                ('origin', models.CharField(max_length=10)),
                ('destination', models.CharField(max_length=10)),
                ('estimatedlv', models.DateTimeField()),
                ('carrier', models.CharField(max_length=10)),
                ('dateshiped', models.DateTimeField()),
            ],
        ),
    ]
