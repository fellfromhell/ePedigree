from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profiles")  # extra fields not needed for this version
    #add name
    #add email

    def __unicode__(self):
        return self.user.username

    class Meta:
        ordering = ["user"]

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

class Following(models.Model):
    # We use this class to link a user_id to customer accounts
    user_id = models.ForeignKey('UserProfile', related_name="follows")
    clientID = models.ForeignKey('Client', db_column="clientID")

    def __unicode__(self):

        return str(self.user_id) + ' is following ' + str(self.clientID)

    class Meta:
        ordering = ["-user_id"]


class Client(models.Model):
    clientID = models.AutoField(primary_key=True, db_column="clientID", verbose_name="Client")
    cName = models.CharField(max_length=80, verbose_name="Client Name")
    cAddressLine1 = models.CharField(max_length=60, blank=True, null=True, verbose_name="Street Address")
    cAddressLine2 = models.CharField(max_length=60, blank=True, null=True, verbose_name="Street Address 2")
    cCity = models.CharField(max_length=30, blank=True, null=True, verbose_name="City")
    cState = models.CharField(max_length=30, blank=True, null=True, verbose_name="State")
    cPostalCode = models.CharField(max_length=15, blank=True, null=True, verbose_name="Zip")
    sName = models.CharField(max_length=80, blank=True, null=True, verbose_name="Client Ship Name")
    sAddressLine1 = models.CharField(max_length=60, blank=True, null=True, verbose_name="Street Address")
    sAddressLine2 = models.CharField(max_length=60, blank=True, null=True, verbose_name="Street Address 2")
    sCity = models.CharField(max_length=30, blank=True, null=True, verbose_name="City")
    sState = models.CharField(max_length=30, blank=True, null=True, verbose_name="State")
    sPostalCode = models.CharField(max_length=15, blank=True, null=True, verbose_name="Zip")

    name = models.CharField(max_length=20, blank=True, null=True)
    is_favorited = models.BooleanField(default=False)


    class Meta:
        ordering = ['cName']

    def __unicode__(self):
        return str(self.cName)

    # class Meta:
    #     ordering = ["-clientID"]

    @models.permalink
    def get_absolute_url(self):
        return ('client-detail', [self.clientID])


class Item(models.Model):
    name = models.CharField(max_length=170, unique=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('item-detail', [self.id])

ORDER_CHOICES = (
    (1, "archived"),
    (2, "cancelled"),
    (3, "converted"),
    (4, "declined"),
    (5, "draft"),
    (6, "expired"),
    (7, "open"),
    (8, "overdue"),
    (9, "paid"),
    (10, "partial"),
    (11, "revised"),
    (12, "sent"),
    (13, "unopen"),
)

class Order(models.Model):
    title = models.CharField(max_length=80, verbose_name="Order No")
    orderDate = models.DateField(verbose_name="Order Date", blank=True)
    description = models.TextField(blank=True)
    clientID = models.ForeignKey(Client, related_name="corders", verbose_name="Client")
    status = models.SmallIntegerField(choices=ORDER_CHOICES)
    #customer name and address and ship to

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('order-detail', [self.pk])


MEASURE_CHOICES = (
    (1, "piece"),
    (2, "liter"),
    (3, "cup"),
    (4, "tablespoon"),
    (5, "teaspoon"),
)


STATUS_CHOICES = (
    (1, "Active"),
    (2, "Hold"),
    (3, "Quarantined"),
    (4, "Returned"),
    (5, "Recalled"),
    (6, "Expired"),
)


class Lot(models.Model):
    lotNumber = models.CharField(max_length=80)
    item = models.ForeignKey(Item, related_name="items")
    expiryDate = models.DateField(verbose_name="Expiration Date", blank=True)
    ndc = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, blank=True, null=True)
    #lot related to items. one item can be in several lots with varying expiry dates
    status = models.SmallIntegerField(choices=STATUS_CHOICES)#status of of lot - active quarantined on hold etc

    def __unicode__(self):
        return self.lotNumber + " (exp " + str(self.expiryDate) + ")"

    def get_absolute_url(self):
        return reverse('lot-detail', args=(self.id,))


class LotTransactions(models.Model):
    lot = models.ForeignKey(Lot, related_name="lots")
    soldToName = models.CharField(max_length=80)
    soldToAddressLine1 = models.CharField(max_length=60)
    soldToAddressLine2 = models.CharField(max_length=60, blank=True)
    soldToCity = models.CharField(max_length=30, blank=True)
    soldToState = models.CharField(max_length=30, blank=True)
    soldToPostalCode = models.CharField(max_length=15, blank=True)
    shipToName = models.CharField(max_length=80, blank=True)
    shipToAddressLine1 = models.CharField(max_length=60, blank=True)
    shipToAddressLine2 = models.CharField(max_length=60, blank=True)
    shipToCity = models.CharField(max_length=30, blank=True)
    shipToState = models.CharField(max_length=30, blank=True)
    shipToPostalCode = models.CharField(max_length=15, blank=True)

    def __unicode__(self):
        return "%.2g %s %s (%s)" % (self.soldToAddressLine1, self.soldToName, self.lot)


class OrderLines(models.Model):
    order = models.ForeignKey(Order, related_name="orders")
    item = models.ForeignKey(Item, related_name="oitems")
    lotnum = models.ForeignKey(Lot, related_name="olines")
    amount = models.DecimalField(decimal_places=0, max_digits=6)
    measurement = models.SmallIntegerField(choices=MEASURE_CHOICES)
    # lot number number to be added and related to item

    # def __unicode__(self):
    #     return "%.2g %s %s (%s)" % (self.amount, self.get_measurement_display(), self.item, self.order)
    def __unicode__(self):
        return self.lotnum_id


class Color(models.Model):
    """
    The color's name (as used by the CSS 'color' attribute, meaning
    lowercase values are required), and a boolean of whether it's "liked"
    or not. There are NO USERS in this demo webapp, which is why there's no
    link/ManyToManyField to the User table.

    This implies that the website is only useable for ONE USER. If multiple
    users used it at the same time, they'd be all changing the same values
    (and would see each others' changes when they reload the page).
    """
    name = models.CharField(max_length=20)
    is_favorited = models.BooleanField(default=False)

    def __str__(self):
        return  self.name

    class Meta:
        ordering = ['name']
