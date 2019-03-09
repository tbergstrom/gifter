from django.db import models
import bcrypt
from django.core.exceptions import ObjectDoesNotExist
import datetime

salt = bcrypt.gensalt()


class UserManager(models.Manager):
    def validate_register(self, post_data):
        errors = []
        if not post_data['first_name'].isalpha():
            errors.append("Your name must only contain letters")
        if len(post_data['first_name']) < 2:
            errors.append("Name must be at least 2 letters")
        if not post_data['last_name'].isalpha():
            errors.append("Your name must only contain letters")
        if len(post_data['last_name']) < 2:
            errors.append("Name must be at least 2 letters")
        if len(post_data['username']) < 2:
            errors.append("Username must be at least 2 letters")
        if User.objects.filter(username=post_data['username']):
            errors.append("Username already exists")
        if len(post_data['password']) < 8:
            errors.append("Password must be at least 8 characters")
        if not post_data['password'] == post_data['confirm_password']:
            errors.append("Passwords do not match")
        if len(errors) == 0:
            hashed_pw = bcrypt.hashpw(post_data['password'].encode('utf8'), salt)
            user = User.objects.create(
                first_name=post_data['first_name'],
                last_name=post_data['last_name'],
                email=post_data['email'],
                date_of_birth=post_data['date_of_birth'],
                username=post_data['username'],
                password=hashed_pw.decode('utf8'))
            return True, user
        else:
            return False, errors

    def validate_login(self, post_data):
        try:
            user = User.objects.get(username=post_data['username'])
            password = post_data['password'].encode('utf8')
            hash_pw = user.password.encode('utf8')
            if bcrypt.checkpw(password, hash_pw):
                return True, user
            else:
                return False, "Incorrect password"
        except ObjectDoesNotExist:
            return False, "No such user"


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, default="")
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, default="example@example.com")
    date_of_birth = models.DateTimeField(default="1111, 11, 11")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
