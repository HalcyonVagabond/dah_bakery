# Generated by Django 3.0.6 on 2020-05-15 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Bread',
                'verbose_name_plural': 'Breads',
            },
        ),
        migrations.CreateModel(
            name='BreadIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=25)),
                ('bread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='breadapp.Bread')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('local_source', models.CharField(max_length=100)),
                ('breads', models.ManyToManyField(through='breadapp.BreadIngredient', to='breadapp.Bread')),
            ],
            options={
                'verbose_name': 'Ingredient',
                'verbose_name_plural': 'Ingredients',
            },
        ),
        migrations.AddField(
            model_name='breadingredient',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='breadapp.Ingredient'),
        ),
        migrations.AddField(
            model_name='bread',
            name='ingredients',
            field=models.ManyToManyField(through='breadapp.BreadIngredient', to='breadapp.Ingredient'),
        ),
    ]