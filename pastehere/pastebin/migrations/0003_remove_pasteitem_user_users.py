# Generated by Django 4.0.1 on 2022-01-29 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pastebin', '0002_pasteitem_user_alter_pasteitem_languages_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pasteitem',
            name='user',
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('socialaccounts_links', models.CharField(max_length=200, null=True)),
                ('picture', models.ImageField(default='noprofile.jpg', upload_to='')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]