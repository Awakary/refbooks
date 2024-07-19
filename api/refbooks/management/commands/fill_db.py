from django.core.management import BaseCommand

from refbooks.models import ElementRefbook, Refbook, VersionRefbook


class Command(BaseCommand):

    help = 'Filling database'

    def handle(self, *args, **options):
        refbook = Refbook.objects.get_or_create(code='1', name='Специальности медицинских работников')
        version = VersionRefbook.objects.update_or_create(refbook_id=refbook[0].id, number='1.0', start_date='2022-01-01')
        values = [('1', 'Врач-терапевт'), ('2', 'Травматолог-ортопед'), ('3', 'Хирург')]
        for j in values:
            ElementRefbook.objects.update_or_create(version_id=version[0].id, code=j[0], value=j[1])
        refbook = Refbook.objects.get_or_create(code='2', name='Международный классификатор болезней')
        version = VersionRefbook.objects.update_or_create(refbook_id=refbook[0].id, number='МКБ-11', start_date='2022-02-11')
        values = [('CA01', 'Острый риносинусит'), ('CA02', 'Острый фарингит'), ('CA03', 'Острый тонзиллит')]
        for j in values:
            ElementRefbook.objects.update_or_create(version_id=version[0].id, code=j[0], value=j[1])
