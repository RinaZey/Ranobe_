from django.db import models
from apps.core.exceptions import AlreadyExistError

class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "tags"

    def clean(self):
        instance = Tag.objects.filter(name=self.name)

        if instance.exists():
            raise AlreadyExistError(
                f"{self.__class__} уже используется")

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "genres"

    def clean(self):
        instance = Genre.objects.filter(name=self.name)

        if instance.exists():
            raise AlreadyExistError(
                f"{self.__class__} уже используется")

    def __str__(self):
        return self.name
