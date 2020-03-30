from django.db import models

# Create your models here.
class Tree(models.Model):
    kind = models.CharField(max_length=20, default="unk")
    last_harvest = models.DateTimeField(null=True)
    last_wasp = models.DateTimeField(null=True)
    notes = models.TextField(null=True)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    
    def __str__(self):
        return "{} in {}".format(self.kind, self.region)


class Region(models.Model):
    name = models.CharField(max_length=200, default="unk") 
    map_area = models.CharField(max_length=200, default="unk",)
    nw_marker = models.CharField(max_length=200, default="unk")
    sw_marker = models.CharField(max_length=200, default="unk")
    ne_marker = models.CharField(max_length=200, default="unk")
    se_marker = models.CharField(max_length=200, default="unk")

    def __str__(self):
        return "{} in {}".format(self.name, self.map_area)

