from django.db import models

#MY MODELS
class UserDetails(models.Model):
    email = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    number = models.PositiveIntegerField()
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    typeuser = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ManageBins(models.Model):
    binid = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    lon = models.DecimalField(max_digits=10,decimal_places=8,default=0)
    lat = models.DecimalField(max_digits=10,decimal_places=8,default=0)
    capacity = models.CharField(max_length=10)

    def __str__(self):
        return self.binid

class WorkerDetails(models.Model):
    email = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    number = models.PositiveIntegerField()
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    typeuser = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class TrackTruck(models.Model):
    truck = models.PositiveIntegerField()
    lon = models.DecimalField(max_digits=10,decimal_places=8)
    lat = models.DecimalField(max_digits=10,decimal_places=8)
    def __str__(self):
        return self.truck

class TrackWorker(models.Model):
    email = models.EmailField()
    lon = models.DecimalField(max_digits=10,decimal_places=8)
    lat = models.DecimalField(max_digits=10,decimal_places=8)
    def __str__(self):
        return self.email

class complaints(models.Model):
    email = models.EmailField()
    lon = models.DecimalField(max_digits=10,decimal_places=8)
    lat = models.DecimalField(max_digits=10,decimal_places=8)
    address = models.CharField(max_length=250)
    img = models.ImageField()
    complaint = models.TextField(max_length=250)
    tags = models.BooleanField(default=False)
    def __str__(self):
        return self.email

class ManageHouse(models.Model):
    houseid = models.CharField(max_length=50)
    lon = models.DecimalField(max_digits=10,decimal_places=8)
    lat = models.DecimalField(max_digits=10,decimal_places=8)
    def __str__(self):
        return self.houseid

class pickup(models.Model):
    email = models.EmailField()
    lat = models.DecimalField(max_digits=10,decimal_places=8)
    lon = models.DecimalField(max_digits=10,decimal_places=8)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.email
