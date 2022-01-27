from ariadne import (
    load_schema_from_path, 
    make_executable_schema,
    snake_case_fallback_resolvers,
    ObjectType
)
from api.gql.queries import (
    resolve_authors,
    resolve_publishers
)


query = ObjectType("Query")
query.set_field("authors", resolve_authors)
query.set_field("publishers", resolve_publishers)

type_defs = load_schema_from_path("schema.graphql")

schema = make_executable_schema(
    type_defs, 
    query, 
    snake_case_fallback_resolvers
)