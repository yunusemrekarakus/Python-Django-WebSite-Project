# Generated by Django 4.1.5 on 2023-02-05 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atakumbungalov', '0003_anasayfa'),
    ]

    operations = [
        migrations.CreateModel(
            name='iletisimForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_soyad', models.CharField(max_length=50, verbose_name='Ad Soyad')),
                ('email', models.CharField(max_length=30, verbose_name='E-mail')),
                ('tel_no', models.CharField(max_length=13, verbose_name='Telefon Numarası')),
                ('mesaj', models.TextField()),
            ],
        ),
    ]