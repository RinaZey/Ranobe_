from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel

from PIL import Image

def _get_image_save_path(instance, filename):
    extension = filename.split(".")[-1]
    return f"ranobe_covers/{instance.title}.{extension}"

class Ranobe(BaseModel):
    STATUS = (
        ('continues', _("Continues")),
        ('finished', _("Finished")),
        ('frozen', _("Frozen")),
        ('licensed', _("Licensed"))
    )

    title = models.CharField(max_length=255, unique=True)

    cover = models.ImageField(default="default_ranobe_cover.png",
                              upload_to=_get_image_save_path)

    creator = models.CharField(max_length=255, unique=True)

    slug = models.SlugField(max_length=255, default=title, db_index=True)
    status = models.CharField(choices=STATUS, default=STATUS[0][0])
    tags = models.ManyToManyField("metadata.Tag", db_index=True)
    genres = models.ManyToManyField("metadata.Genre", db_index=True)

    class Meta:
        ordering = ["-created_at"]
        db_table = "ranobes"

    def _resize_cover(self):
        cover = Image.open(self.cover.path)
        output_size = (600, 800)
        if cover.width != output_size[0] or cover.height != output_size[1]:
            cover = cover.resize(
                size=output_size, resample=Image.Resampling.LANCZOS
            )
            cover.save(self.cover.path)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if kwargs.get("update_fields"):
            kwargs["update_fields"].append("slug")

        super().save(*args, **kwargs)

        self._resize_cover()

    def __str__(self):
        return f"{self.title} - {self.status}"
