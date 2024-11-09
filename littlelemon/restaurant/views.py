from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Booking
from .serializers import BookingSerializer

class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer