from django.contrib import admin

from persons.models import Driver, Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'birthdate', 'team']
    list_filter = ['name']
    search_fields = ['name']
    prepopulated_fields = {
        'slug': [
            'name',
        ]
    }


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'birthdate', 'team', 'wins', 'podiums']
    list_filter = ['name']
    search_fields = ['name']
    prepopulated_fields = {
        'slug': [
            'name',
        ]
    }
