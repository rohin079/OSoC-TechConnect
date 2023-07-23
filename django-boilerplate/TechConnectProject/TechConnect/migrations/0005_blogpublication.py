# Generated by Django 4.1.10 on 2023-07-23 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TechConnect', '0004_blogsubmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPublication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year_of_education', models.CharField(max_length=50)),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_material', models.TextField()),
            ],
            options={
                'db_table': 'publishBlog',
            },
        ),
    ]