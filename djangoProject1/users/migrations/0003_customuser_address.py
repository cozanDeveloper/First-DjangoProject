# Generated by Django 4.2.16 on 2024-09-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.TextField(default='pshtap bari shilanan'),
        ),
    ]
