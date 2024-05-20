from select import select
from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    from_area = models.ForeignKey("Area", on_delete=models.CASCADE, verbose_name="+")
    to_area = models.ForeignKey("Area", on_delete=models.CASCADE, verbose_name='To', related_name="+")
    latitude = models.CharField(verbose_name='latitude', max_length=20, blank=False, null=True)
    longitude = models.CharField(verbose_name='longitude', max_length=20, blank=False, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_created_order', null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_updated_order', null=True)
    number_of_customer = models.IntegerField(null=False, default=1)
    appointment =models.ForeignKey("Appointment",on_delete=models.CASCADE,related_name="order_appointment",null=False)
    # price=models.ForeignKey("price", verbose_name=_(""), on_delete=models.CASCADE)

    # def total_price():

    class Meta:
        # ordering = ['name']
        verbose_name = 'Order'


class Area(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    # created_on = models.DateTimeField(auto_now_add=True)
    # updated_on = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_created_Area', null=True)
    # updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_updated_Area', null=True)

    def __str__(self):
        return self.name


class News(models.Model):
    note = models.CharField(max_length=200, default='')
    active = models.BooleanField(default=True)
    # created_on = models.DateTimeField(auto_now_add=True)
    # updated_on = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_created_news', null=True)
    # updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_updated_news', null=True)


class Appointment(models.Model):
    name = models.CharField(max_length=32, unique=True)
    active = models.BooleanField(default=True)
    time_arrive = models.TimeField()
    # from_area = models.ForeignKey(Area, on_delete=models.CASCADE,verbose_name='From')
    # to_area = models.ForeignKey(Area,on_delete=models.CASCADE,verbose_name='To',related_name="+")
    # select_time=models.DateField
    # end_date
    # color
    # driver
    # state
    latitude = models.CharField(verbose_name='latitude', max_length=20, blank=False, null=True)
    longitude = models.CharField(verbose_name='longitude', max_length=20, blank=False, null=True)

# class Price(models.Model):
# from_area = models.ForeignKey(Area, on_delete=models.CASCADE,verbose_name='From')
# to_area = models.ForeignKey(Area,on_delete=models.CASCADE,verbose_name='To',related_name="+")
# price=models.CharField(max_length=3)
