# Generated by Django 3.0.5 on 2023-03-20 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0004_auto_20230320_0300'),
    ]

    operations = [
        migrations.CreateModel(
            name='myuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='sample',
        ),
    ]
