from django.db import models
from django.contrib.auth.models import User
import hashlib
import datetime

# Create your models here.
class Block(models.Model):
    hash =  models.TextField(max_length=15, blank=True)
    nonce = models.IntegerField(blank=True)
    msg = models.TextField(max_length=20, blank=True)
    time = models.DateTimeField(blank=True, auto_now_add=True)

    def __init(self, hash, nonce, date, msg):
        self.hash = str(hash)
        self.nonce = nonce
        self.date = datetime.datetime.now()
        self.msg = str(msg)

    def get_hash(self):
        return self.hash

    def get_nonce(self):
        return self.nonce

    def get_date(self):
        return self.date

    def get_msg(self):
        return self.msg

    def calc_hash(self, prev_hash):
        result = prev_hash + self.msg + self.nonce
        result = result.encode()
        return hashlib.sha256(result).hexdigest()
    
    def get_dict(self):
        return dict(text=self.msg, nonce=self.nonce, hash=self.hash, time=self.time)