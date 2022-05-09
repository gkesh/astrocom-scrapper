from xmlrpc.client import boolean
from ariadne import ObjectType
from api.models.comic import Comic
from api.models.comic import Chapter


mutation = ObjectType("Mutation")


@mutation.field("visited")
def resolve_visited(*_, comic, chapter) -> bool:
    try:
        parent: Comic = Comic.objects.get(code=comic)
        chapter: Chapter = parent.chapters.get(number=chapter)
        chapter.visited = True

        parent.save()

        updated = True
    except:
        updated = False
    return updated


@mutation.field("checkpoint")
def resolve_checkpoint(*_, comic, chapter) -> bool:
    try:
        parent: Comic = Comic.objects.get(code=comic)

        # Removing previous checkpoint
        for ch in parent.chapters.filter(checkpoint=True): ch.checkpoint = None

        # Setting Checkpoint
        chapter: Chapter = parent.chapters.get(number=chapter)
        chapter.checkpoint = True

        parent.save()

        updated = True
    except:
        updated = False
    return updated


@mutation.field("download")
def resolve_download(*_, comic, start=0, end) -> bool:
    pass


@mutation.field("add")
def resolve_add(*_) -> bool:
    pass


@mutation.field("delete")
def resolve_delete(*_, comic) -> bool:
    pass


@mutation.field("clean")
def resolve_clean(*_, comic) -> bool:
    pass