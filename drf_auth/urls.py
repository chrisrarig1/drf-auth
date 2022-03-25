from django.urls import path
from .views import TripDetailView,TripListView

urlpatterns = [
    path('',TripListView.as_view(), name ='trip_list'),
    path('<int:pk>/', TripDetailView.as_view(), name ='trip_detail'),
]