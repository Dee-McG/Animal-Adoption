from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Adoption
from .forms import AdoptionForm

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class AddAdoption(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    View to render the add adoption page and form
    """
    template_name = 'adoptions/create.html'
    model = Adoption
    success_url = '/'
    form_class = AdoptionForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddAdoption, self).form_valid(form)

    def test_func(self):
        """
        Ensure user is superuser or throw 403 error
        """
        return self.request.user.is_superuser


class EditAdoption(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View to render the edit adoption page and form
    """
    template_name = 'adoptions/create.html'
    model = Adoption
    success_url = '/'
    form_class = AdoptionForm

    def test_func(self):
        """
        Ensure user is superuser or throw 403 error
        """
        return self.request.user.is_superuser


class DeleteAdoption(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    VIew to render delete page and form to delete adoption advert
    """
    model = Adoption
    success_url = '/'

    def test_func(self):
        """
        Ensure user is superuser or throw 403 error
        """
        return self.request.user.is_superuser
