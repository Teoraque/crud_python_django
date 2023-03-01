from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.name)
    
    def save(self):
        self.name = self.name.upper()
        super(Cat, self).save()

    class Meta:
        verbose_name_plural = 'Gatos'
