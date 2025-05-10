import logging

from metadata.models import Tag, Genre
from metadata.types import TagObject, GenreObject

from apps.common.services import model_update

logger = logging.getLogger(__name__)

def update_tag(tag: Tag, data: TagObject) -> Tag:
    """Сервис обновления экземпляра тега"""
    fields = ['name']

    tag, _ = model_update(instance=tag, fields=fields,
                          data=data.dict())

    logger.info(f"Tag {tag.pk} data: {data.name} обновлен")

    return tag

def create_tag(data: TagObject) -> Tag:
    obj = Tag(name=data.name)
    obj.full_clean()
    obj.save()

    logger.info(f"Tag {data.name} создан")

    return obj

def create_genre(data: GenreObject) -> Genre:
    obj = Genre(name=data.name)
    obj.full_clean()
    obj.save()

    logger.info(f"Genre {data.name} создан")

    return obj

def update_genre(genre: Genre, data: GenreObject) -> Genre:
    fields = ['name']

    genre, _ = model_update(instance=genre, fields=fields,
                            data=data.dict())

    logger.info(f"Genre {genre.pk}  data: {data.name} обновлен")

    return genre
