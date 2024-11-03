# Generated by Django 5.1.2 on 2024-11-03 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_projects_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='+994556449164', max_length=200, verbose_name='Number')),
            ],
            options={
                'verbose_name': 'Phone',
                'verbose_name_plural': 'Phone',
            },
        ),
        migrations.CreateModel(
            name='Telegram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='+994556449164', max_length=200, verbose_name='Number')),
            ],
            options={
                'verbose_name': 'Telegram',
                'verbose_name_plural': 'Telegram',
            },
        ),
        migrations.CreateModel(
            name='Whatsapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='+994556449164', max_length=200, verbose_name='Number')),
            ],
            options={
                'verbose_name': 'Whatsapp',
                'verbose_name_plural': 'Whatsapp',
            },
        ),
    ]