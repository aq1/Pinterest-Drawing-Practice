# Generated by Django 3.0.1 on 2020-01-08 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dash_pictures', '0005_auto_20200109_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boards', to='dash_pictures.PinterestUser'),
        ),
    ]