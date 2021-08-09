import hashlib

from django.db import models


class Block(models.Model):
    hash = models.TextField(blank=True)
    nonce = models.IntegerField(blank=True)
    msg = models.TextField(max_length=20, blank=True)
    time = models.DateTimeField(blank=True, auto_now_add=True)

    def calc_hash(self, prev_hash: str) -> str:
        result = prev_hash + self.msg + str(self.nonce)
        result = result.encode()
        return hashlib.sha256(result).hexdigest()

    def get_dict(self) -> dict:
        return dict(text=self.msg, nonce=self.nonce, hash=self.hash, time=self.time)

    def validate(self) -> bool:
        return self.hash.startswith('000000')
