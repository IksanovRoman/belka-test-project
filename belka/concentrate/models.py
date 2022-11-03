from django.db import models

# Create your models here.
class Concentrate(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование сырья')
    iron = models.DecimalField(max_digits=4, decimal_places=2, default=0, verbose_name='Содержание железа')
    silicon = models.DecimalField(max_digits=4, decimal_places=2, default=0, verbose_name='Содержание кремния')
    aluminum = models.DecimalField(max_digits=4, decimal_places=2, default=0, verbose_name='Содержание алюминия')
    calcium = models.DecimalField(max_digits=4, decimal_places=2, default=0, verbose_name='Содержание кальция')
    sulfur = models.DecimalField(max_digits=4, decimal_places=2, default=0, verbose_name='Содержание серы')

    MONTHS = [
        ('Январь', 'Январь'),
        ('Февраль', 'Февраль'),
        ('Март', 'Март'),
        ('Апрель', 'Апрель'),
        ('Май', 'Май'),
        ('Июнь', 'Июнь'),
        ('Июль', 'Июль'),
        ('Август', 'Август'),
        ('Сентябрь', 'Сентябрь'),
        ('Октябрь', 'Октябрь'),
        ('Ноябрь', 'Ноябрь'),
        ('Декабрь', 'Декабрь'),
    ]

    month = models.CharField(max_length=8,
                             choices=MONTHS,
                             default="Январь",
                             )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Концентрат"
        verbose_name_plural = "Концентрат"
        ordering = ['id', ]