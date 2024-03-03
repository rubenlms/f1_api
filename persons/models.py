from django.db import models
from django.urls import reverse

from teams.models import Team


class Person(models.Model):
    name = models.TextField()
    slug = models.SlugField()
    birthdate = models.DateField()
    country = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='team')
    image = models.URLField(blank=True)

    # class Meta:
    #     verbose_name = _("Person")
    #     verbose_name_plural = _R_co("Persons")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Person_detail", kwargs={"pk": self.pk})


class Driver(Person):
    wins = models.IntegerField()
    podiums = models.IntegerField()
    wdc = models.IntegerField()

    # class Meta:
    #     verbose_name = _("Driver")
    #     verbose_name_plural = _("Drivers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Driver_detail", kwargs={"pk": self.pk})
