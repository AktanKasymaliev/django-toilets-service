# Generated by Django 3.1.7 on 2021-03-16 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_side', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='restroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restroom', to='api_side.entity'),
        ),
    ]