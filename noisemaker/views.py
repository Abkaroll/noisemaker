from django.views.generic import TemplateView

from noisemaker.models import NoiseFile, RandomNoiseFile


class SoundBoard(TemplateView):
    """
    A simple Dashboard with buttons to make API calls to make noises.
    """
    template_name = 'soundboard.html'

    def get_context_data(self, **kwargs):
        kwargs['noises'] = NoiseFile.objects.all()
        kwargs['groups'] = RandomNoiseFile.objects.all()
        return kwargs

