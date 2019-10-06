from django.db import models
from django.contrib.auth.models import User
import hashlib

# Create your models here.
class Block(models.Model):
    hash =  models.CharField(max_length=15, blank=True)
    nonce = models.IntegerField(blank=True)
    date = models.DateTimeField(blank=True)
    msg = models.CharField(max_length=3, blank=True)

    def get_hash(self):
        return self.hash

    def get_nonce(self):
        return self.nonce

    def get_date(self):
        return self.date

    def get_msg(self):
        return self.msg

    def calc_hash(self, prev_hash):
        result = prev_hash + self.text + self.nonce
        result = result.encode()
        return hashlib.sha256(result).hexdigest()
    
    def get_dict(self):
        return dict(text=self.text, nonce=self.nonce, hash=self.hash, time=self.time)