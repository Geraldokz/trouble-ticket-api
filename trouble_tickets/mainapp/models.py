from django.db import models


class Event(models.Model):
    start_date = models.DateTimeField(verbose_name='Дата создания')
    finish_date = models.DateTimeField(verbose_name='Дата окончания', null=True, blank=True)
    description = models.TextField(verbose_name='Описание')
    impact = models.ForeignKey('Impact', verbose_name='Влияние', on_delete=models.CASCADE)

    def __str__(self):
        return f'Событие номер {self.pk}'


class Impact(models.Model):
    PRIORITY_CHOICES = (
        ('1', 'Первый приоритет'),
        ('2', 'Второй приоритет'),
        ('3', 'Третий приоритет'),
    )

    priority = models.CharField(verbose_name='Приоритет', choices=PRIORITY_CHOICES, max_length=255)
    affected_services_count = models.IntegerField(verbose_name='Количество затронутых сервисов')

    def __str__(self):
        return f'Влияние {self.pk}'
