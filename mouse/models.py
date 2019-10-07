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
        self.hash = hash
        self.nonce = nonce
        self.date = datetime.datetime.now()
        self.msg = msg

    def calc_hash(self, prev_hash):
        result = prev_hash + self.msg + str(self.nonce)
        result = result.encode()
        return hashlib.sha256(result).hexdigest()
    
    def get_dict(self):
        return dict(text=self.msg, nonce=self.nonce, hash=self.hash, time=self.time)

    def validate(self,h):
        return h.startswith('0' * 4)