from django.db import models

# Create your models here.
class Worker_Catalog_FarmingPlaces(models.Model):
    farmingplace = models.CharField(max_length = 50,blank=True, null=True)

    def __str__(self):
        return self.farmingplace

class Worker_Catalog_Designations(models.Model):
    farmingplace = models.ForeignKey(Worker_Catalog_FarmingPlaces, on_delete = models.CASCADE)
    designation = models.CharField(max_length = 50,blank=True, null=True)

    def __str__(self):
        return "%s - %s" % (self.designation,self.farmingplace)
