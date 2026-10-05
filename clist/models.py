from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Contact(models.Model):
    first_name = models.CharField(max_length=40, verbose_name="First name")
    last_name = models.CharField(max_length=60, verbose_name="Last name")
    phone = models.CharField(
        max_length=15, verbose_name="Phone number", unique=True)
    address = models.CharField(max_length=250, verbose_name="Address")
    slug = models.SlugField(max_length=50, verbose_name="Slug", unique=True,)
    objects = models.Manager()

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    def get_absolute_url(self):
        return reverse("clist:contact_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.phone, allow_unicode=True)
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['last_name']
        indexes = [models.Index(fields=['first_name', 'last_name'])]
        verbose_name = 'Contact'
