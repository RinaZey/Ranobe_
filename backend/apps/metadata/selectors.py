from metadata.models import Tag, Genre

def tag_list() -> list[Tag]:
    return Tag.objects.all()

def get_tag(pk: int) -> Tag:
    return Tag.objects.get(pk=pk)

def get_genre(pk: int) -> Genre:
    return Genre.objects.get(pk=pk)

def genre_list() -> list[Genre]:
    return Genre.objects.all()
