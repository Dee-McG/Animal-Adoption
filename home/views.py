from django.views.generic import ListView
from adoptions.models import Adoption


class Index(ListView):
    """
    View to render the index page
    """
    template_name = 'home/index.html'
    model = Adoption
    context_object_name = "animals"
