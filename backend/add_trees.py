import csv
from pathlib import Path
from trees.models import Tree, Region
from datetime import datetime

SOURCE_FILE = Path("/Users/nicholasmiller/Documents/acnh_trees.csv")

now = datetime.now()

with SOURCE_FILE.open() as source:
    reader = csv.DictReader(source)
    for row in reader:
        kind = row['kind']
        region = row['region']
        matching_region = Region.objects.filter(name=region)[0]
        region_id = matching_region.id
        notes = row['notes']
        print("Creating {} tree in {} ({}) ({})".format(kind, region,
            region_id, notes))
        Tree.objects.create(kind=kind, region=matching_region, notes=notes,
                last_harvest=now, last_wasp=now)
