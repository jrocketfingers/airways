from django.contrib.auth.models import AbstractUser
from django.db import models

from core import validators


class Model(models.Model):
    """The base set of model fields used in all models.

    :field created_at:
    :field created_by:
    :field updated_at:
    :field updated_by:
    :field deleted_at:
    :field deleted_by:
    """

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('core.User', related_name='+', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('core.User', related_name='+', null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey('core.User', null=True, blank=True,
                                   related_name='+')

    class Meta:
        abstract = True


class User(AbstractUser, Model):
    SEX_MALE = 'M'
    SEX_FEMALE = 'F'
    SEX_CHOICES = (
        (SEX_MALE, 'Male',),
        (SEX_FEMALE, 'Female',),
    )
    email = models.EmailField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    date_of_birth = models.DateField(validators=[validators.over_18], null=True, blank=True)
    company = models.ForeignKey('core.Company', null=True, blank=True,
                                related_name='employees')


class Crew(User):
    pass


class Pilot(Crew):
    pass


class Stewardess(Crew):
    pass


class Company(Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return f'{self.name}'


class Manufacturer(Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=2)  # ISO_3166-1_alpha-2
    city = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class AircraftMake(Model):
    """An aircraft make.

    :field manufacturer:
    :field name:
    :field license_prefix: Specifies the license prefixes for pilots elgible to
                           fly the plane of this make.
    """
    manufacturer = models.ForeignKey('core.Manufacturer',
                                     related_name='aircrafts')
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    capacity = models.IntegerField()
    length = models.FloatField()
    speed = models.IntegerField()
    license_prefix = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.manufacturer} {self.name}'


class Aircraft(Model):
    """An aircraft.

    :field make: The model/make of the particular aircraft.
    :field company: The airways company the aircraft belongs to.
    """
    make = models.ForeignKey('core.AircraftMake')
    company = models.ForeignKey('core.Company')

    def __str__(self):
        return f'{self.company} - {self.make}'


class Airport(Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Terminal(Model):
    name = models.CharField(max_length=100)
    airport = models.ForeignKey('core.Airport')

    def __str__(self):
        return f'{self.airport} - {self.name}'


class Gate(Model):
    name = models.CharField(max_length=100)
    terminal = models.ForeignKey('core.Terminal')

    def __str__(self):
        return f'{self.terminal} - {self.name}'


class Radar(Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class AircraftLease(Model):
    """A lease of an aircraft from one company to another.

    Can be issued by the crediting company employee.

    :field creditor: The company that lends the aircraft.
    :field debtor: The company that borrows the aircraft.
    :field aircraft: The aircraft in question.
    """
    creditor = models.ForeignKey('core.Company', related_name='credited')
    debtor = models.ForeignKey('core.Company', related_name='debted')
    aircraft = models.ForeignKey('core.Aircraft')


class Flight(Model):
    flight_no = models.CharField(max_length=10)
    company = models.ForeignKey('core.Company', related_name='flights')

    departure_airport = models.ForeignKey('core.Airport', related_name='departing_flights')
    departure_terminal = models.ForeignKey('core.Terminal', related_name='departing_flights')
    departure_gate = models.ForeignKey('core.Gate', related_name='departing_flights')
    arrival_airport = models.ForeignKey('core.Airport', related_name='arriving_flights')
    arrival_terminal = models.ForeignKey('core.Terminal', related_name='arriving_flights')
    arrival_gate = models.ForeignKey('core.Gate', related_name='arriving_flights')

    start_time = models.DateTimeField()
    duration = models.DurationField()
    route_radars = models.ManyToManyField('core.Radar')
    charter = models.BooleanField(default=False)
    plane = models.ForeignKey('core.Aircraft')
    crew = models.ManyToManyField('core.Crew')

    def __str__(self):
        return f'{self.flight_no} - {self.departure_airport} -> {self.arrival_airport}'


class FlightUpdate(Model):
    flight = models.ForeignKey('core.Flight', related_name='updates')
    loc = models.ForeignKey('core.Radar')
    FLIGHT_UPDATE_TAKE_OFF = 'TO'
    FLIGHT_UPDATE_RADAR_CONTROL = 'RC'
    FLIGHT_UPDATE_LANDING = 'LA'
    FLIGHT_UPDATE_EMERGENCY_LANDING = 'EL'

    FLIGHT_UPDATE_TYPES = (
        (FLIGHT_UPDATE_TAKE_OFF, 'Take off'),
        (FLIGHT_UPDATE_RADAR_CONTROL, 'Radar Control'),
        (FLIGHT_UPDATE_LANDING, 'Landing'),
        (FLIGHT_UPDATE_EMERGENCY_LANDING, 'Emergency Landing'),
    )
    type = models.CharField(max_length=2, choices=FLIGHT_UPDATE_TYPES)

    average_speed = models.FloatField()
    remaining_distance = models.FloatField()

    @property
    def estimated_time(self):
        return self.average_speed / self.remaining_distance

    def __str__(self):
        return f'{self.flight} at {self.loc}'
