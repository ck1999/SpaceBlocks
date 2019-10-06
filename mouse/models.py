from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Block(models.Model){
    hash =  models.CharField(max_length=15)
    nonce = models.IntegerField()
    date = models.DateTimeField()

    def get_hash(self):
        return self.hash

    def get_nonce(self):
        return self.nonce

    def get_date(self):
        return self.date
}