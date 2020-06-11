from django.db import models
from lib.helpers import generate_heating_coils, generate_cooling_coils, generate_terminal_unit_types, generate_fan

# Create your models here.
class Site(models.Model):
    STATES = (
        ("AK", "Alaska"),
        ("AL", "Alabama"),
        ("AR", "Arkansas"),
        ("AZ", "Arizona"),
        ("CA", "California"),
        ("CO", "Colorado"),
        ("CT", "Connecticut"),
        ("DC", "District of Columbia"),
        ("DE", "Delaware"),
        ("FL", "Florida"),
        ("GA", "Georgia"),
        ("HI", "Hawaii"),
        ("IA", "Iowa"),
        ("ID", "Idaho"),
        ("IL", "Illinois"),
        ("IN", "Indiana"),
        ("KS", "Kansas"),
        ("KY", "Kentucky"),
        ("LA", "Louisiana"),
        ("MA", "Massachusetts"),
        ("MD", "Maryland"),
        ("ME", "Maine"),
        ("MI", "Michigan"),
        ("MN", "Minnesota"),
        ("MO", "Missouri"),
        ("MS", "Mississippi"),
        ("MT", "Montana"),
        ("NC", "North Carolina"),
        ("ND", "North Dakota"),
        ("NE", "Nebraska"),
        ("NH", "New Hampshire"),
        ("NJ", "New Jersey"),
        ("NM", "New Mexico"),
        ("NV", "Nevada"),
        ("NY", "New York"),
        ("OH", "Ohio"),
        ("OK", "Oklahoma"),
        ("OR", "Oregon"),
        ("PA", "Pennsylvania"),
        ("PR", "Puerto Rico"),
        ("RI", "Rhode Island"),
        ("SC", "South Carolina"),
        ("SD", "South Dakota"),
        ("TN", "Tennessee"),
        ("TX", "Texas"),
        ("UT", "Utah"),
        ("VA", "Virginia"),
        ("VT", "Vermont"),
        ("WA", "Washington"),
        ("WI", "Wisconsin"),
        ("WV", "West Virginia"),
        ("WY", "Wyoming")
    )

    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATES)
    zip = models.IntegerField()


class AirSystems(models.Model):
    name = models.CharField(max_length=50)
    site_id = models.ForeignKey(Site, on_delete=models.CASCADE)


class AirHandler(models.Model):
    # Create the choices list on the fly
    hc = generate_heating_coils()
    cc = generate_cooling_coils()
    fa = generate_fan()

    hc_choices = [(h.get('id'), h.get('description')) for h in hc]
    cc_choices = [(h.get('id'), h.get('description')) for h in cc]
    f_choices = [(f.get('id'), f.get('description')) for f in fa]

    # Add in options for choice to be blank
    hc_choices.append(('None', 'None'))
    cc_choices.append(('None', 'None'))
    f_choices.append(('None', 'None'))

    name = models.CharField(max_length=50)
    site_id = models.ForeignKey(Site, on_delete=models.CASCADE)

    pre_heat_coil = models.CharField(max_length=100, choices=tuple(hc_choices))
    supp_heat_coil = models.CharField(max_length=100, choices=tuple(hc_choices))
    heating_coil_type = models.CharField(max_length=100, choices=tuple(hc_choices))
    cooling_coil_type = models.CharField(max_length=100, choices=tuple(cc_choices))
    exhaust_fan_type = models.CharField(max_length=100, choices=tuple(f_choices))
    discharge_fan_type = models.CharField(max_length=100, choices=tuple(f_choices))
    return_fan_type = models.CharField(max_length=100, choices=tuple(f_choices))


class ThermalZone(models.Model):
    name = models.CharField(max_length=50)


class TerminalUnit(models.Model):
    # Create the choices list on the fly
    tu = generate_terminal_unit_types()
    tu_choices = [(h.get('id'), h.get('description')) for h in tu]

    # Add in options for choice to be blank
    tu_choices.append(('None', 'None'))

    name = models.CharField(max_length=50)
    ahu_id = models.ForeignKey(AirHandler, on_delete=models.CASCADE)
    terminal_unit_type = models.CharField(max_length=50, choices=tuple(tu_choices))
    thermal_zone = models.OneToOneField(ThermalZone, on_delete=models.CASCADE)

# class HeatingCoil(models.Model):
#     name = models.CharField(max_length=50)

# class AirHandlerHeatingCoil(models.Model):
#     hcs = HeatingCoil.objects.get_all()
#     HEATING_COIL_CHOICES = []
#     for hc in hcs.items():
#         HEATING_COIL_CHOICES.append((hc.id, hc.description))
#
#     name = models.CharField(max_length=50)
#     heating_coil_id = models.


# class Component(models.Model):
#     CATEGORIES = (
#         ("Heating Coil", (
#             ('Modulating DX heating ')),
#          ),
#     )
#     name = models.CharField(max_length=100)
#     # category =
