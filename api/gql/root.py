from ariadne import (
    load_schema_from_path, 
    make_executable_schema,
    snake_case_fallback_resolvers
)
from api.gql.queries import query
from api.models.comic import ComicType
from ariadne import EnumType


type_defs = load_schema_from_path("schema.graphql")

comic_type = EnumType("ComicType", ComicType)

schema = make_executable_schema(
    type_defs, 
    [query, comic_type], 
    snake_case_fallback_resolvers
)