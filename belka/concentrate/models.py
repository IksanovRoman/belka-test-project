from django.db import models

# Create your models here.
class Concentrate(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование сырья')
    iron = models.DecimalField(max_digits=4, decimal_places=2, default=0, verbose_name='Содержание железа')
    silicon = models.DecimalField(max_digits=4, decimal_places=2, default=0, verbose_name='Содержание кремния')
    aluminum = models.DecimalField(max_digits=4, decimal_places=2, default=0, verbose_name='Содержание алюминия')
    calcium = models.DecimalField(max_digits=4, decimal_places=2, default=0, verbose_name='Содержание кальция')
    sulfur = models.DecimalField(max_digits=4, decimal_places=2, default=0, verbose_name='Содержание серы')
    month = models.ForeignKey('Month', on_delete=models.PROTECT, verbose_name="Месяц")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Концентрат"
        verbose_name_plural = "Концентрат"
        ordering = ['id', ]

class Month(models.Model):
    name = models.CharField(max_length=15, verbose_name="Месяц", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Месяц"
        verbose_name_plural = "Месяц"
        ordering = ['id', ]