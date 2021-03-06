# Generated by Django 3.0.7 on 2020-08-10 19:02
import os

from django.db import migrations

from rdflib import Graph, Namespace

PH = Namespace("https://project-haystack.org/def/ph/3.9.9#")
PHICT = Namespace("https://project-haystack.org/def/phIct/3.9.9#")
PHSCIENCE = Namespace("https://project-haystack.org/def/phScience/3.9.9#")
PHIOT = Namespace("https://project-haystack.org/def/phIoT/3.9.9#")


def generate_haystack_equipment_types(apps, schema_editor):
    hv = '3.9.9'
    HaystackVersion = apps.get_model('mapp', 'HaystackVersion')
    HaystackMarkerTag = apps.get_model('mapp', 'HaystackMarkerTag')
    HaystackEquipmentType = apps.get_model('mapp', 'HaystackEquipmentType')
    haystack_version_model = HaystackVersion.objects.get(version=hv)
    p = os.path.join(os.getcwd(), f"mapp/resources/haystack/{hv}/defs.ttl")

    g = Graph()
    g.bind("ph", PH)
    g.bind("phict", PHICT)
    g.bind("phscience", PHSCIENCE)
    g.bind("phiot", PHIOT)
    g.parse(p, format="ttl")

    # We use everything that is a subclass of an equip
    q = """SELECT ?m WHERE {
            ?m rdfs:subClassOf* phIoT:equip
        }
        """
    match = g.query(q)

    all_equip = [m[0] for m in match]
    for equip in all_equip:
        het = HaystackEquipmentType(haystack_tagset=equip.split("#")[1], version=haystack_version_model)
        het.save()
        hmm = HaystackMarkerTag.objects.filter(tag=equip.split("#")[1])

        if len(hmm) == 1:
            het.marker_tags.add(hmm[0])
        elif len(hmm) == 0:
            print(f"Haystack tag: {equip.split('#')[1]} is not a marker tag in version {hv}")
            print(f"A record for following equip will not be created: {equip.split('#')[1]}")
            het.delete()
            break
        else:
            print(f"Haystack tag: {equip.split('#')[1]} has multiple tags in version {hv}")
            print(f"A record for following proto will not be created: {equip.split('#')[1]}")
            het.delete()
            break


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0007_haystackequipmenttype'),
    ]

    operations = [
        migrations.RunPython(generate_haystack_equipment_types)
    ]
