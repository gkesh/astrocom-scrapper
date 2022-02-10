from xmlrpc.client import boolean
from ariadne import ObjectType
from api.models.comic import Comic
from api.models.comic import Chapter


mutation = ObjectType("Mutation")


@mutation.field("visited")
async def resolve_visited(*_, comic, chapter) -> bool:
    try:
        parent: Comic = await Comic.objects.get(code=comic)
        chapter: Chapter = await parent.chapters.get(number=chapter)
        chapter.visited = True

        await parent.save()

        updated = True
    except:
        updated = False
    return updated


@mutation.field("checkpoint")
async def resolve_checkpoint(*_, comic, chapter) -> bool:
    try:
        parent: Comic = await Comic.objects.get(code=comic)

        # Removing previous checkpoint
        filtered_parent = await parent.chapters.filter(checkpoint=True)
        for ch in filtered_parent: ch.checkpoint = None

        # Setting Checkpoint
        chapter: Chapter = await parent.chapters.get(number=chapter)
        chapter.checkpoint = True

        parent.save()

        updated = True
    except:
        updated = False
    return updated