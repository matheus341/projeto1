# Generated by Django 4.0.3 on 2022-03-23 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_nasc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nasc',
            field=models.DateField(null=True),
        ),
    ]