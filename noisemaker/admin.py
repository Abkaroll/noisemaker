from django.contrib import admin

from noisemaker.models import NoiseFile, RandomNoiseFile

admin.site.register(NoiseFile)
admin.site.register(RandomNoiseFile)
