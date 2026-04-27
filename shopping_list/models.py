import uuid

from django.db import models

class ShoppingList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    members = models.ManyToManyField('auth.User')

    def __str__(self):
        return self.name

class ShoppingItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    shopping_list = models.ForeignKey(ShoppingList, related_name='shopping_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    purchased = models.BooleanField()

    def __str__(self):
        return f"{self.name}"