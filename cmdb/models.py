from django.db import models
class Information(models.Model):
    name = models.CharField(max_length=30)
    privateip = models.GenericIPAddressField()
    publicip = models.GenericIPAddressField()
    use = models.TextField()
    zoneid = models.CharField(max_length=30)
    cpu = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)
    datadisk = models.CharField(max_length=30)
    time = models.DateTimeField()

    def __unicode__(self):
        return self.name
