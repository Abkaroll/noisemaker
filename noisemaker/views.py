from django.views.generic import TemplateView


class SoundBoard(TemplateView):
    """
    A simple Dashboard with buttons to make API calls to make noises.
    """
    template_name = 'soundboard.html'

