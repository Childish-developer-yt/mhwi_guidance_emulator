# Generated by Django 2.2.8 on 2019-12-18 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuidanceArea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('level', models.IntegerField()),
                ('kind', models.IntegerField()),
            ],
            options={
                'db_table': 'guidance_area',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Monsters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('isveteran', models.BooleanField(db_column='isVeteran')),
                ('material_name', models.CharField(max_length=50)),
                ('isalchemize', models.BooleanField(db_column='isAlchemize')),
            ],
            options={
                'db_table': 'monsters',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReferenceCustomRareMonsters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'reference_custom_rare_monsters',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReferenceMonstersArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'reference_monsters_area',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReferencePartsWepnameMonsters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'reference_parts_wepname_monsters',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReferenceUpgradeMaterials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'reference_upgrade_materials',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReferenceWeaponsFrame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_nums', models.IntegerField()),
            ],
            options={
                'db_table': 'reference_weapons_frame',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeaponsCustom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('grade', models.IntegerField()),
                ('effect', models.CharField(max_length=50)),
                ('frame_num', models.IntegerField()),
            ],
            options={
                'db_table': 'weapons_custom',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeaponsName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'weapons_name',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeaponsPartsEffect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('effect', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'weapons_parts_effect',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeaponsRare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'weapons_rare',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeaponsUpgrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'weapons_upgrade',
                'managed': False,
            },
        ),
    ]