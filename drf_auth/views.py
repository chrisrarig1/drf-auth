from rest_framework import generics
from .serializer import TripSerializer
from .models import Trip
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

class TripListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TripDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Trip.objects.all()
    serializer_class = TripSerializer



# Create your views here.
