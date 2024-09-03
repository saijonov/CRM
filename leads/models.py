from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE) # every lead has ONE agent assigned to it (That is why we can not write it in agent's class)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # The reason we did not use the foreignkey is because one user and have only one agent associated to it. So we used OneToOneField there

    def __str__(self):
        return self.user.email

