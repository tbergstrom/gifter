from django.db import models
from ..logreg.models import User


class ItemManager(models.Manager):
    def validate_item(self, post_data):
        errors = []
        if len(post_data['name']) < 2:
            errors.append("Item name must be at least 2 characters")
        return errors

    def create_item(self, post_data):
        item = self.create(
            name=post_data['name'],
            description=post_data['description'],
            user_id=post_data['user_id']
        )
        return item

    def delete(self, item_id, user_id):
        self.get(id=item_id).added_by.remove(user_id)

    def join(self, item_id, user_id):
        self.get(id=item_id).added_by.add(user_id)


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    user = models.ForeignKey(User, related_name="items", default="", on_delete=models.CASCADE)
    added_by = models.ManyToManyField(User, related_name="items_added")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()