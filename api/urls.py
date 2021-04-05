from django.urls import path
from api import views 

urlpatterns = [
    path('generic', views.GenericTeamView.as_view()),
    path('generic/<int:pk>', views.GenericTeamView.as_view()),
]