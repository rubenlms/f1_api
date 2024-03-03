from django.db import models
from django.urls import reverse


class Team(models.Model):
    name = models.TextField()
    slug = models.SlugField(blank=True)
    wins = models.IntegerField()
    pole_positions = models.IntegerField()
    wdc = models.IntegerField()
    car = models.TextField(blank=True)
    engine = models.TextField(blank=True)
    factory_base = models.TextField(blank=True)
    # team_principal = models.ForeignKey(
    #     Person, on_delete=models.PROTECT, related_name='team_principal'
    # )
    # drivers = models.ManyToManyField(Driver)

    # class Meta:
    #     verbose_name = _("Team")
    #     verbose_name_plural = _("Teams")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Team_detail", kwargs={"pk": self.pk})
