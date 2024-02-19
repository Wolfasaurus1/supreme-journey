from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("login-submit", views.login_submit, name="login-submit"),
    path("access", views.access_view, name="access"),
    path("requests", views.requests_view, name="requests"),
    path("irs", views.irs_view, name="irs"),
    path("createrequest/<int:ir_id>", views.access_request, name="createrequest")
]