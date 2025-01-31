# Generated by Django 5.0.6 on 2024-06-12 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_image', models.ImageField(upload_to='product/')),
                ('ogcost', models.IntegerField()),
                ('dcost', models.IntegerField()),
                ('desc', models.TextField()),
            ],
        ),
    ]
