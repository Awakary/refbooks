import datetime

from django.db import models


class RefBook(models.Model):
    code = models.CharField(max_length=100, unique=True, verbose_name='Код')
    name = models.CharField(max_length=300, verbose_name='Наименование')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    @property
    def current_version(self):
        current_version = (self.versions.filter(
            start_date__lte=datetime.date.today()).
                           order_by('start_date').last())
        if current_version:
            return current_version

    class Meta:
        verbose_name = 'Cправочник'
        verbose_name_plural = 'Cправочники'


class VersionRefBook(models.Model):
    refbook = models.ForeignKey(RefBook, verbose_name='Справочник',
                                related_name='versions',
                                on_delete=models.CASCADE)
    number = models.CharField(max_length=50, verbose_name='Версия')
    start_date = models.DateField(blank=True, null=True,
                                  verbose_name='Дата начала действия версии')

    def __str__(self):
        return f'{self.number} - {self.refbook}'

    class Meta:
        verbose_name = 'Версия справочника'
        verbose_name_plural = 'Версии справочников'
        unique_together = ['refbook', 'number']


class ElementRefBook(models.Model):
    version = models.ForeignKey(VersionRefBook, verbose_name='Версия справочника', on_delete=models.CASCADE)
    code = models.CharField(max_length=100, verbose_name='Код элемента')
    value = models.CharField(max_length=300, verbose_name='Значение элемента')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Элемент справочника'
        verbose_name_plural = 'Элементы справочников'
        unique_together = ['code', 'version']
