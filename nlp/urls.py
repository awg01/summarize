from django.urls import path
from . import views

app_name = 'nlp'

urlpatterns = [
    path("urlsummarizer/", views.urlsummarizer, name="urlsummarizer"),
    path("urlshowcase/", views.urlshowcase, name="urlshowcase"),
    path("paragraph/", views.paragraph, name="paragraph"),
    path("filesummarizer/", views.filesummarizer, name="filesummarizer"),

    # path("filemailtest/", views.filemailtest, name="filemailtest"),
]
