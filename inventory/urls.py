from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required
from . import views


from inventory.views import (
    index,
    sobre,
    registro,
    confirmar_troca,
    recusar_troca,
    excluir_registro,
    listar_usuarios,
    excluir_usuarios,
)

from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import RedirectView
from accounts.views import AccountCreateView  # Ajuste este import conforme necessário
from . import views  # Ajuste conforme necessário

urlpatterns = [
    path("index/", login_required(views.index), name="index"),
    path("sobre/", login_required(views.sobre), name="sobre"),
    path("registro/", login_required(views.registro), name="registro"),
    path("confirmar/<int:produto_id>/", login_required(views.confirmar_troca), name="confirmar_troca"),
    path("recusar/<int:produto_id>/", login_required(views.recusar_troca), name="recusar_troca"),
    path("excluir/<int:produto_id>/", login_required(views.excluir_registro), name="excluir_registro"),
    path("editar/<int:produto_id>/", login_required(views.editar_produto), name="editar_produto"),
    path('listar_usuarios/', login_required(views.listar_usuarios), name='listar_usuarios'),
    path('excluir_usuarios/', login_required(views.excluir_usuarios), name='excluir_usuarios'),
    path('pagina_de_confirmacao/', login_required(views.pagina_de_confirmacao), name='pagina_de_confirmacao'),

    # URL de cadastro de usuários
    path('signup/', AccountCreateView.as_view(), name='signup'),

    # URLs de autenticação
    path("accounts/", include("django.contrib.auth.urls")),
    path("", RedirectView.as_view(pattern_name="login", permanent=False)),
    path("login/", LoginView.as_view(), name="login"),
]
