# Generated by Django 3.2 on 2021-07-15 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0009_alter_workfeature_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='list_description',
            field=models.TextField(blank=True, verbose_name='List description'),
        ),
        migrations.AlterField(
            model_name='work',
            name='cover_image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='cover_images', verbose_name='List image'),
        ),
    ]
