from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from .forms import AccountSignupForm

User = get_user_model()

class AccountCreateView(CreateView):
    model = User
    template_name = "registration/signup_form.html"
    form_class = AccountSignupForm
    success_url = reverse_lazy("login")
    success_message = "Usuário criado com sucesso!"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.password = make_password(form.cleaned_data['password1'])
        user.save()
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
