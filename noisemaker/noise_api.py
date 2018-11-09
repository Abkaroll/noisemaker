from rest_framework import views

from noisemaker.models import NoiseFile, RandomNoiseFile


class PlayNoise(views.APIView):
    """
    Issue a GET request here to play a specific noise from the server's speakers
    """
    model = NoiseFile

    def get(self, request, noise_name):
        noise_file = self.model.objects.get(name=noise_name)
        noise_file.play()


class PlayRandomNoise(PlayNoise):
    """
    Issue a GET request here to play a random noise out of a specific collection
    """
    model = RandomNoiseFile
