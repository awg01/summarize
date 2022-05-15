from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.conf.urls import (handler400, handler403, handler404, handler500)

# handler400 = 'app.views.bad_request'
# handler403 = 'app.views.permission_denied'
# handler404 = 'app.views.page_not_found'
# handler500 = 'users.views.server_error'

app_name = 'users'

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("dictionary/", views.dictionary, name="dictionary"),
    path("about/", views.about_us, name="about"),
    path("login/", views.login_page, name="login"),
    path("logout/", auth_view.LogoutView.as_view(template_name="users/logout.html"), name="logout"),

]

# handler404 = "users.views.page_not_found_view"
