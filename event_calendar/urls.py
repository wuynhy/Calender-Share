from django.urls import path
from . import views

app_name = 'event_calendar'

urlpatterns = [
    path('', views.event_list, name='event-list'),
    path('create/', views.event_create, name='event-create'),
    path('<int:id>/', views.event_detail, name='event-detail'),
    path('<int:id>/update/', views.event_update, name='event-update'),
    path('<int:id>/delete/', views.event_delete, name='event-delete'),
]
