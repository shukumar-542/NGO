# Generated by Django 3.1.3 on 2022-08-19 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientSite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voluntieer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('email', models.EmailField(blank=True, max_length=250, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('about', models.TextField(blank=True, null=True)),
                ('social_links', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='profile1.png', upload_to='volunteer/')),
            ],
        ),
    ]