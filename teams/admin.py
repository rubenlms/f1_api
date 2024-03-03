from django.contrib import admin

from teams.models import Team


@admin.register(Team)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'wins', 'car', 'engine']
    list_filter = ['name']
    search_fields = ['name']
    prepopulated_fields = {
        'slug': [
            'name',
        ]
    }
