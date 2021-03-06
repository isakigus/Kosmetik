# Generated by Django 3.1 on 2020-08-30 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtributoCosmetico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaCosmetica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaIngrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('comentario', models.TextField(default='')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.categoriaingrediente')),
                ('propiedades', models.ManyToManyField(blank=True, to='api.AtributoCosmetico')),
            ],
        ),
        migrations.CreateModel(
            name='IngredienteReceta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje', models.DecimalField(decimal_places=4, max_digits=8)),
                ('ingrediente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ingrediente')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('comentario', models.TextField(default='')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.categoriacosmetica')),
                ('propiedades', models.ManyToManyField(blank=True, to='api.AtributoCosmetico')),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredientes', models.ManyToManyField(to='api.IngredienteReceta')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateTimeField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=8)),
                ('currency', models.TextField(default='EUR')),
                ('ingrediente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ingrediente')),
                ('tienda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.tienda')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='images')),
                ('categoria', models.TextField(choices=[('imagen', 'imagen'), ('etiqueta', 'etiqueta')])),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.producto')),
            ],
        ),
    ]
