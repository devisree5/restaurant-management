from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Appointment, Order, News, Area


class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class AppointmentSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class OrderSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class NewsSeralizer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class AreaSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'
