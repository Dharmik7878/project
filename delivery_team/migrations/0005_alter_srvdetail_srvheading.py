# Generated by Django 5.1.4 on 2025-02-01 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_team', '0004_srvdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='srvdetail',
            name='srvheading',
            field=models.CharField(max_length=80),
        ),
    ]
