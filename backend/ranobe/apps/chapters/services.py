from chapters.models import Chapter
from chapters.types import ChapterObject

from apps.common.services import model_update, get_fields_to_update

import logging

logger = logging.getLogger(__name__)

def create_chapter(data: ChapterObject) -> Chapter:
    chapter = Chapter(title=data.title, ranobe_id=data.ranobe, text=data.text,
                      number=data.number, volume=data.volume)
    chapter.full_clean()
    chapter.save()

    logger.info(f"Chapter {chapter.pk} для ranobe {data.ranobe} создана")

    return chapter

def update_chapter(chapter: Chapter, data: ChapterObject) -> Chapter:
    fields = get_fields_to_update(data)

    chapter, _ = model_update(instance=chapter, fields=fields,
                              data=data.dict(), auto_updated_at=True)

    logger.info(f"Chapter {chapter.pk} data: {data.dict()} была обновлена")

    return chapter
