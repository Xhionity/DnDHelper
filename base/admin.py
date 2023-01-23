from django.contrib import admin
from .models import Spells, Classes, Trinkets, Stats, Conditions, Creatures, Abilities, Races, RaceList
# Register your models here.


admin.site.register(Spells)
admin.site.register(Classes)
admin.site.register(Trinkets)
admin.site.register(Stats)
admin.site.register(Conditions)
admin.site.register(Creatures)
admin.site.register(Abilities)
admin.site.register(Races)
admin.site.register(RaceList)

