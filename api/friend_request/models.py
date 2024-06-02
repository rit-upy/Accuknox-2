from django.db import models
from authentication.models import User

from django.core.exceptions import ValidationError

# Create your models here.
class Friends(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    pending = models.BooleanField(default=True)



    class Meta:
        constraints  = [
        models.UniqueConstraint(
            fields=['user', 'friend'],
            name='user_friend_unique_constraint', 
            violation_error_message = 'User and friend are the same'
            
        ),
        models.CheckConstraint(
            check= ~models.Q(user = models.F('friend')),
            name = 'prevent_self_friendship', 
            violation_error_message = 'User and friend are the same'
        )
        ]


