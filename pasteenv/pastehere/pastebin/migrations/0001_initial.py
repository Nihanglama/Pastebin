# Generated by Django 4.0.1 on 2022-01-28 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pasteitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, null=True)),
                ('pasteitems', models.TextField(null=True)),
                ('added_time', models.DateField(auto_now_add=True, null=True)),
                ('languages', models.CharField(choices=[('py', 'python'), ('C++', 'Cplusplus'), ('C', 'Cprogramming'), ('java', 'Java')], max_length=100, null=True)),
                ('visible', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], max_length=100, null=True)),
            ],
        ),
    ]
