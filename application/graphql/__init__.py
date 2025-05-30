import graphene
from .users import GetUsers
from .posts import GetPosts, AddPost, EditPost

class Query(GetUsers, GetPosts, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    edit_post = EditPost.Field()
    add_post = AddPost.Field()

schema = graphene.Schema(
                            query=Query,
                            mutation=Mutation
                        )
