# Generated by Django 4.2.14 on 2024-07-16 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_petinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userinfo'),
        ),
    ]
