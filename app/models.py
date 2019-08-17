from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.TextField(unique=True)
    description = models.TextField()
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    @property
    def children_count(self):
        return self.category_set.count()
    
    @property
    def items_count(self):
        return self.item_set.count()

    def __str__(self):
        return f' {self.id} | {self.name} '

class Item(models.Model):
    name = models.TextField(unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.TextField()
    photo = models.ImageField(upload_to='item_images/')
    count_views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.id} | {self.name} '
