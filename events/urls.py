from django.urls import path
from . import views

urlpatterns = [
    path('', views.Events.as_view(), name='events-home'),
    # path('registered/', views.FullInformation.as_view(), name='event-registered'),
    path('event-information/<int:pk>/', views.FullInformation.as_view(), name='event-information'),
]