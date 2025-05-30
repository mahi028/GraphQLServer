import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from .models import User, Post, db
from datetime import datetime

class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User

class PostType(SQLAlchemyObjectType):
    class Meta:
        model = Post

class ReturnType(graphene.ObjectType):
    message = graphene.String()
    status = graphene.Int()

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_posts = graphene.List(PostType)
    
    user = graphene.Field(UserType, id=graphene.Int(), username=graphene.String())
    posts_by_user = graphene.List(PostType, user_id=graphene.Int())
    
    def resolve_all_users(self, info):
        return User.query.all()
    
    def resolve_all_posts(self, info):
        return Post.query.all()
    
    def resolve_user(self, info, id=None, username=None):
        query = User.query
        if id:
            return query.filter(User.id == id).first()
        if username:
            return query.filter(User.username == username).first()
        return None
    
    def resolve_posts_by_user(self, info, user_id):
        return Post.query.filter(Post.user_id == user_id).all()

class Mutation(graphene.ObjectType):
    edit_post = graphene.Field(ReturnType, userid=graphene.Int(), postid=graphene.Int(), content=graphene.String())
    add_post = graphene.Field(ReturnType, user_id=graphene.Int(), title=graphene.String(), content=graphene.String())

    def resolve_edit_post(self, info, userid, postid, content):
        
        if userid and postid:
            post = Post.query.filter((Post.user_id == userid) & (Post.id == postid)).first()
            if post:
                try:
                    post.content = content
                    db.session.commit()
                except Exception as err:
                    db.session.rollback()
                    print(err)
                    return ReturnType(message="Failure", status=500)
                else:
                    return ReturnType(message="Success", status=200)   
            else:
                return ReturnType(message="Post Not Found", status=404)
        return ReturnType(message="Please Enter required Feilds", status=402)
    
    def resolve_add_post(self, info, user_id, title, content):
        user = User.query.get(user_id)
        if user:
            try:
                db.session.add(Post(title=title, content=content, user_id=user.id))
                db.session.commit()
            except Exception as err:
                db.session.rollback()
                print(err)
                return ReturnType(message="Failure", status=500)
            else:
                return ReturnType(message="Success", status=200)

schema = graphene.Schema(
                            query=Query,
                            mutation=Mutation
                        )
