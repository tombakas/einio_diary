from django.db import models


class Irasas(models.Model):
    pavadinimas = models.CharField(max_length=120, blank=True)
    tekstas = models.TextField(blank = True)
    data = models.DateField(auto_now = True)

    def __unicode__(self):
        return self.pavadinimas
