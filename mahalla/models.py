from django.db import models
from django.contrib.auth.models import User


class Sector(models.Model):
    name = models.CharField(verbose_name="Sektor nomi", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sektor"
        verbose_name_plural = "Sektorlar"
        ordering = ("id", )


class Neighborhood(models.Model):
    sector = models.ForeignKey('Sector', on_delete=models.PROTECT,
                               help_text="Mahalla qaysi sektorga tegishli ekanligini tanlang")
    name = models.CharField(verbose_name="mahalla nomi ", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahalla"
        verbose_name_plural = "Mahalalar"
        ordering = ("id", )


class Citizen(models.Model):
    GENDER = (
        ("male", "Erkak"),
        ("female", "ayol"),
    )
    EDUCATED = (
        ("middle", "O'rta malumotli"),
        ("senior", "oliy malumotli")
    )
    IRAN_NOTEBOOK = (
        ("YES", "ha"),
        ("no", "yoq")
    )
    ABROAD = (
        ("YES", "ha"),
        ("no", "yoq")
    )
    DISABILITY = (
        ("YES", "ha"),
        ("no", "yoq")
    )
    WOMANS_NOTEBOOK = (
        ("YES", "ha"),
        ("no", "yoq")
    )
    neighborhood = models.ForeignKey('Neighborhood', verbose_name="mahalani tanlang",
                                     on_delete=models.PROTECT)
    full_name = models.CharField(verbose_name='F.I.O', max_length=255)
    passport = models.CharField(verbose_name='Passport seriya raqami', max_length=20)
    birthdate = models.DateTimeField(verbose_name='tugulgan sanasi')
    gender = models.CharField(
        max_length=255,
        choices=GENDER,
        verbose_name='fuqora jinsi',
    )
    educated = models.CharField(
        verbose_name='fuqora malumoti',
        max_length=255,
        choices=EDUCATED
    )
    address = models.TextField(verbose_name='Fuqaro manzili')

    iron_notebook = models.CharField(
        verbose_name="temir daftarda bormi",
        max_length=255,
        choices=IRAN_NOTEBOOK,
    )
    abroad = models.CharField(
        verbose_name='Chet eldami hozir',
        max_length=255,
        choices=ABROAD
    )
    disabiltiy = models.CharField(
        verbose_name="nogironligi bormi",
        max_length=20,
        choices=DISABILITY
    )
    womens_notebook = models.CharField(
        verbose_name="Ayollar daftarida bormi",
        max_length=20,
        choices=WOMANS_NOTEBOOK
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Fuqora"
        verbose_name_plural = "Fuqoralar"
        ordering = ("id",)
