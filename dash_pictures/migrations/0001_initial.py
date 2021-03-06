# Generated by Django 3.0.1 on 2019-12-25 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predefined', models.BooleanField(default=False)),
                ('pinterest_id', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boards', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PinterestUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='pinterest', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('pinterest_id', models.CharField(max_length=255, unique=True)),
                ('access_token', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pinterest_id', models.CharField(max_length=255, unique=True)),
                ('image_url', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pins', to='dash_pictures.Board')),
            ],
        ),
    ]
