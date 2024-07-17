# Generated by Django 4.2.14 on 2024-07-17 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_petinfo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petinfo',
            name='petAnniv',
        ),
        migrations.RemoveField(
            model_name='petinfo',
            name='petBirth',
        ),
        migrations.RemoveField(
            model_name='petinfo',
            name='petName',
        ),
        migrations.RemoveField(
            model_name='petinfo',
            name='user',
        ),
        migrations.AddField(
            model_name='petinfo',
            name='pet_anniv',
            field=models.DateField(null=True, verbose_name='반려동물 사망일'),
        ),
        migrations.AddField(
            model_name='petinfo',
            name='pet_birth',
            field=models.DateField(null=True, verbose_name='반려동물 출생일'),
        ),
        migrations.AddField(
            model_name='petinfo',
            name='pet_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='petinfo',
            name='pet_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_pets', to='accounts.userinfo'),
        ),
    ]