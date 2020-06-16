# Generated by Django 3.0.7 on 2020-06-12 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirHandler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pre_heat_coil', models.CharField(choices=[('35', 'Modulating DX heating coil'), ('37', 'Modulating electric heating coil'), ('42', 'Modulating natural gas heating coil'), ('43', '2-stage DX heating coil'), ('45', '2-stage electric heating coil'), ('46', '2-stage natural gas heating coil'), ('55', 'Single Stage DX heating coil'), ('57', 'Modulating hot water coil'), ('58', 'Modulating steam coil'), ('60', 'Single stage electric heating coil'), ('61', 'Single stage natural gas heating coil'), ('None', 'None')], max_length=100)),
                ('supp_heat_coil', models.CharField(choices=[('35', 'Modulating DX heating coil'), ('37', 'Modulating electric heating coil'), ('42', 'Modulating natural gas heating coil'), ('43', '2-stage DX heating coil'), ('45', '2-stage electric heating coil'), ('46', '2-stage natural gas heating coil'), ('55', 'Single Stage DX heating coil'), ('57', 'Modulating hot water coil'), ('58', 'Modulating steam coil'), ('60', 'Single stage electric heating coil'), ('61', 'Single stage natural gas heating coil'), ('None', 'None')], max_length=100)),
                ('heating_coil_type', models.CharField(choices=[('35', 'Modulating DX heating coil'), ('37', 'Modulating electric heating coil'), ('42', 'Modulating natural gas heating coil'), ('43', '2-stage DX heating coil'), ('45', '2-stage electric heating coil'), ('46', '2-stage natural gas heating coil'), ('55', 'Single Stage DX heating coil'), ('57', 'Modulating hot water coil'), ('58', 'Modulating steam coil'), ('60', 'Single stage electric heating coil'), ('61', 'Single stage natural gas heating coil'), ('None', 'None')], max_length=100)),
                ('cooling_coil_type', models.CharField(choices=[('44', '2-stage DX cooling coil'), ('56', 'Single Stage DX cooling coil'), ('59', 'Modulating chilled water coil'), ('None', 'None')], max_length=100)),
                ('discharge_fan_type', models.CharField(choices=[('4', 'On/off discharge fan'), ('5', 'Variable speed discharge fan'), ('48', '2-speed discharge fan'), ('None', 'None')], max_length=100)),
                ('return_fan_type', models.CharField(choices=[('7', 'On/off return fan'), ('8', 'Variable speed return fan'), ('50', '2-speed return fan'), ('None', 'None')], max_length=100)),
                ('exhaust_fan_type', models.CharField(choices=[('10', 'On/off exhaust fan'), ('11', 'Variable speed exhaust fan'), ('49', '2-speed exhaust fan'), ('None', 'None')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(choices=[('AK', 'Alaska'), ('AL', 'Alabama'), ('AR', 'Arkansas'), ('AZ', 'Arizona'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DC', 'District of Columbia'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('IA', 'Iowa'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('MA', 'Massachusetts'), ('MD', 'Maryland'), ('ME', 'Maine'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MO', 'Missouri'), ('MS', 'Mississippi'), ('MT', 'Montana'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('NE', 'Nebraska'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NV', 'Nevada'), ('NY', 'New York'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VA', 'Virginia'), ('VT', 'Vermont'), ('WA', 'Washington'), ('WI', 'Wisconsin'), ('WV', 'West Virginia'), ('WY', 'Wyoming')], max_length=2)),
                ('zip', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ThermalZone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TerminalUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('terminal_unit_type', models.CharField(choices=[('TU-001', 'VAV Box Cooling Only'), ('TU-002', 'CAV Terminal Unit'), ('None', 'None')], max_length=50)),
                ('ahu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generate.AirHandler')),
                ('thermal_zone', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='generate.ThermalZone')),
            ],
        ),
        migrations.CreateModel(
            name='AirSystems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('site_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generate.Site')),
            ],
        ),
        migrations.AddField(
            model_name='airhandler',
            name='site_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generate.Site'),
        ),
    ]
