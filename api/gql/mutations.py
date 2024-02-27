from typing import Any, Dict, Tuple
from ariadne import ObjectType
from api.gql import NAME
from api.models.comic import Comic
from api.models.comic import Chapter
from api.operations import save_comic
from logger.workers import info, error


mutation = ObjectType("Mutation")

@mutation.field("visited")
def resolve_visited(*_, comic, chapter) -> bool:
    try:
        parent: Comic = Comic.objects.get(code=comic)
        chapter: Chapter = parent.chapters.get(number=chapter)
        chapter.visited = True

        parent.save()

        updated = True
        info(NAME, f"Updated visited status for chapter {chapter} of {comic}")
    except:
        updated = False
        error(NAME, f"Failed to update visited status for chapter {chapter} of {comic}")
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
        info(NAME, f"Updated checkpoint for {comic} to chapter {chapter}")
    except:
        updated = False
        error(NAME, f"Failed to update checkpoint for {comic} to chapter {chapter}")
    return updated


@mutation.field("download")
def resolve_download(*_, comic, start=0, end) -> bool:
    pass


@mutation.field("add")
def resolve_add(*_, comic: Dict[str, Any]) -> Tuple[bool, str]:
    try:
        saved_comic = save_comic(comic)
        info(NAME, f"Comic {saved_comic.title} was saved successfully!")

        return {
            "status": True,
            "data": saved_comic._id,
            "error": None
        }
    except Exception as exp:
        error(NAME, str(exp))
        return {
            "status": False,
            "data": None,
            "error": [str(exp)]
        }


@mutation.field("delete")
def resolve_delete(*_, comic: str) -> bool:
    pass


@mutation.field("clean")
def resolve_clean(*_, comic: str) -> bool:
    pass