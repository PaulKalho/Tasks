from django.db import models
from datetime import date

class Group(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=150, null=False)
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE, null = False, blank=False, related_name='group_todo')
    pos = models.IntegerField(null = False, blank=False)
    deadline = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    @property
    def is_today(self):
        if isinstance(self.deadline, date):
            if date.today() >= self.deadline:
                return True
        return False
