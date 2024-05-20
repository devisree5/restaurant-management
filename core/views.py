from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Appointment, Order, News, Area
from .serializer import UserSeralizer, AppointmentSerlizer, OrderSeralizer, NewsSeralizer, AreaSeralizer


class UserViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSeralizer
    queryset = get_user_model().objects.all()


class AppointmentViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = AppointmentSerlizer
    queryset = Appointment.objects.all()


class OrderViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSeralizer
    queryset = Order.objects.all()


class NewsViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = NewsSeralizer
    queryset = News.objects.all()


class AreaViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = AreaSeralizer
    queryset = Area.objects.all()
