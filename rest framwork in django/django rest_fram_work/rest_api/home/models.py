from django.db import models
import uuid
# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key = True,editable=False,default=uuid.uuid4())
    created_at = models.DateField(auto_now=True)
    update_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class todo(BaseModel):
    todo_title = models.CharField(max_length=100)
    todo_discription = models.TextField()
    is_done = models.BooleanField(default = False)
