# Generated by Django 3.1.2 on 2020-11-13 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_gpu_imagen_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='almacenamiento',
            name='imagen_detail',
            field=models.ImageField(null=True, upload_to='almacenamiento_detail/'),
        ),
        migrations.AddField(
            model_name='fuentespoder',
            name='imagen_detail',
            field=models.ImageField(null=True, upload_to='fuentedepoder_detail/'),
        ),
        migrations.AddField(
            model_name='gabinete',
            name='imagen_detail',
            field=models.ImageField(null=True, upload_to='gabinete_detail/'),
        ),
        migrations.AddField(
            model_name='monitore',
            name='imagen_detail',
            field=models.ImageField(null=True, upload_to='monitor_detail/'),
        ),
        migrations.AddField(
            model_name='ram',
            name='imagen_detail',
            field=models.ImageField(null=True, upload_to='ram_detail/'),
        ),
    ]
