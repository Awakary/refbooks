from django.contrib import admin

from refbooks.models import ElementRefbook, Refbook, VersionRefbook


class VersionRefbookInline(admin.StackedInline):
    model = VersionRefbook


@admin.register(Refbook)
class RefbookAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'current_version', 'start_date')
    inlines = [VersionRefbookInline]
    # @admin.display(description='Дата начала действия версии')

    def start_date(self, obj):
        if obj.current_version:
            return obj.current_version.start_date
    start_date.short_description = 'Дата начала действия версии'

    def current_version(self, obj):
        if obj.current_version:
            return obj.current_version.number
    current_version.short_description = 'Текущая версия'


class ElementRefbookInline(admin.StackedInline):
    model = ElementRefbook


@admin.register(VersionRefbook)
class VersionRefbookAdmin(admin.ModelAdmin):
    list_display = ('refbook_code', 'refbook_name', 'number', 'start_date')
    inlines = [ElementRefbookInline]

    def refbook_code(self, obj):
        return obj.refbook.code
    refbook_code.short_description = 'Код справочника'

    def refbook_name(self, obj):
        return obj.refbook.name
    refbook_name.short_description = 'Наименование справочника'


@admin.register(ElementRefbook)
class ElementRefbookAdmin(admin.ModelAdmin):
    list_display = ('version', 'code', 'value')

