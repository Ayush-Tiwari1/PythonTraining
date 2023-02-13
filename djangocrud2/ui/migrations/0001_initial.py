
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=25, null=True)),
                ('age', models.IntegerField(max_length=10, null=True)),
                ('dapartment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ui.department')),
            ],
        ),
    ]
