# Generated by Django 4.1.3 on 2022-11-02 03:11

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=45)),
                ('Documento', models.CharField(max_length=25, unique=True)),
                ('Direccion', models.CharField(max_length=55)),
                ('Telefono', models.CharField(max_length=10)),
                ('Correo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Documento', models.CharField(max_length=25, unique=True)),
                ('Nombre', models.CharField(max_length=45)),
                ('Username', models.CharField(max_length=32)),
                ('Direccion', models.CharField(max_length=55)),
                ('Telefono', models.CharField(max_length=10)),
                ('Fecha_nacimiento', models.DateTimeField()),
                ('Correo', models.CharField(max_length=50)),
                ('Tipo_empleado', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Numero', models.CharField(max_length=15)),
                ('Fecha_venta', models.DateTimeField()),
                ('Valor', models.IntegerField()),
                ('Cantidad', models.IntegerField()),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='FERRETIC.cliente')),
                ('Empleado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='FERRETIC.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.CharField(max_length=20)),
                ('Nombre', models.CharField(max_length=25)),
                ('Estado', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Nombre', models.CharField(max_length=45)),
                ('Telefono', models.CharField(max_length=10)),
                ('Correo', models.CharField(max_length=50)),
                ('Token', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Codigo', models.CharField(max_length=25)),
                ('Dirreccion', models.CharField(max_length=55)),
                ('Empleado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='FERRETIC.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.CharField(max_length=20)),
                ('Nombre', models.CharField(max_length=25)),
                ('Costo', models.IntegerField()),
                ('Precio_venta', models.IntegerField()),
                ('Linea_produto', models.CharField(max_length=20)),
                ('Fecha_compra', models.DateTimeField()),
                ('Marca', models.CharField(max_length=21)),
                ('Proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='FERRETIC.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Factura_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Factura', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='FERRETIC.factura')),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='FERRETIC.producto')),
            ],
        ),
    ]