from django.db import models
from apps.common.models import BaseModel

class Chapter(BaseModel):
    title = models.CharField(max_length=255)
    volume = models.IntegerField(default=1)
    number = models.IntegerField(default=1)
    ranobe = models.ForeignKey('ranobes.Ranobe', on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        db_table = 'chapters'
        default_related_name = 'chapters'
        ordering = ['volume', 'number']

    def __str__(self):
        return f"{self.volume}:{self.number} - {self.title} - {self.ranobe}"
