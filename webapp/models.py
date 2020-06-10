from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.conf import settings

# Create your models here.
# custom authenticated models
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_admin=False, is_staff=False, is_customer=False, is_restaurent=False):
        if not email:
            raise ValueError("must enter email")
        if not password:
            raise ValueError("must hve a password")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password) #change or set password
        user_obj.active     = is_active
        user_obj.admin      = is_admin
        user_obj.staff      = is_staff
        user_obj.customer   = is_customer
        user_obj.restaurent = is_restaurent
        user_obj.save(using=self._db)
        return user_obj

    def create_customer(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
            is_staff=True,
            is_customer=True
        )
        return user
    
    def create_restaurent(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
            is_staff=True,
            is_restaurent=True
        )
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
            is_staff=True,
            is_admin=True,
            is_customer=True,
            is_restaurent=True,
        )
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_staff(self):
        return self.staff
    
    class Meta:
        db_table = "user_details"

class customer(models.Model):
    user        = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city  		= models.CharField(max_length=40,blank=False)
    phone 		= models.CharField(max_length=10,blank=False)
    address		= models.TextField()

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "customer_details"

class Restaurant(models.Model):
    user        = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    rname 		= models.CharField(max_length=100,blank=False)
    info	 	= models.CharField(max_length=40,blank=False)
    min_ord		= models.CharField(max_length=5,blank=False)
    location    = models.CharField(max_length=40,blank=False)
    r_logo      = models.FileField(blank=False)

    REST_STATE_OPEN    = "Open"
    REST_STATE_CLOSE   = "Closed"
    REST_STATE_CHOICES =(
    (REST_STATE_OPEN,REST_STATE_OPEN),
    (REST_STATE_CLOSE,REST_STATE_CLOSE)
    )
    status 	= models.CharField(max_length=50,choices=REST_STATE_CHOICES,default=REST_STATE_OPEN,blank=False)
    approved = models.BooleanField(blank=False,default=True)

    def __str__(self):
        return self.rname

    class Meta:
        db_table = "restaurent_details"