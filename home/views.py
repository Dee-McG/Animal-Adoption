from django.views.generic import TemplateView


class Index(TemplateView):
    """
    View to render the index page
    """
    template_name = 'home/index.html'
