# Generated by Django 4.0.3 on 2022-03-07 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses/images', verbose_name='Imagem'),
        ),
    ]