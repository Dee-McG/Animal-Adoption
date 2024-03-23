from django.views.generic import CreateView
from .models import Adoption
from .forms import AdoptionForm

from django.contrib.auth.mixins import LoginRequiredMixin


class AddAdoption(LoginRequiredMixin, CreateView):
    template_name = 'adoptions/create.html'
    model = Adoption
    success_url = '/'
    form_class = AdoptionForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddAdoption, self).form_valid(form)
