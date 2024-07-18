from django.contrib import admin

from refbooks.models import ElementRefBook, RefBook, VersionRefBook


class VersionRefBookInline(admin.StackedInline):
    model = VersionRefBook


@admin.register(RefBook)
class RefBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'current_version', 'start_date')
    inlines = [VersionRefBookInline]
    # @admin.display(description='Дата начала действия версии')

    def start_date(self, obj):
        if obj.current_version:
            return obj.current_version.start_date
    start_date.short_description = 'Дата начала действия версии'

    def current_version(self, obj):
        if obj.current_version:
            return obj.current_version.number
    current_version.short_description = 'Текущая версия'


class ElementRefBookInline(admin.StackedInline):
    model = ElementRefBook


@admin.register(VersionRefBook)
class VersionRefBookAdmin(admin.ModelAdmin):
    list_display = ('refbook_code', 'refbook_name', 'number', 'start_date')
    inlines = [ElementRefBookInline]

    def refbook_code(self, obj):
        return obj.refbook.code
    refbook_code.short_description = 'Код справочника'

    def refbook_name(self, obj):
        return obj.refbook.name
    refbook_name.short_description = 'Наименование справочника'


@admin.register(ElementRefBook)
class ElementRefBookAdmin(admin.ModelAdmin):
    list_display = ('version', 'code', 'value')

