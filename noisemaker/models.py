import random
from django.db import models
import pygame

class PlayMixin(object):
    """
    Add a .play() method to any object which has a .file attribute
    """
    def play(self):
        """
        Play the noise file out of the server's speakers
        """
        # Wow this is a really heavyweight way to play a sound out of the server's speakers, but oh well....
        pygame.mixer.music.load(self.file.name)
        pygame.mixer.music.play(0)


class NoiseFile(models.Model, PlayMixin):
    """
    A sound byte we can play
    """
    name = models.CharField(unique=True, help_text="A unique name which will be used to look up the noise")
    description = models.CharField()
    file = models.FileField()


class RandomNoiseFile(models.Model, PlayMixin):
    """
    Trigger one of several sound files.
    """
    name = models.CharField(unique=True, help_text="A unique name which will be used to look up the noise")
    file_choices = models.ManyToManyField(NoiseFile)

    @property
    def file(self):
        """
        Choose a random file from the list of possibilities
        """
        possible_files = self.file_choices.values_list('id', flat=True)
        file_id = random.choice(possible_files)
        noise = NoiseFile.objects.get(id=file_id)
        return noise.file

