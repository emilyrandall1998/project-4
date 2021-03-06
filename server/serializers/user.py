from app import ma
from models.user import User
from marshmallow import fields

class UserSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = User
        load_instance = True
        exclude = ('password_hash',)
        load_only = ('email', 'password')

    password = fields.String(required=True)
    photos = fields.Nested('PhotoSchema', many=True)
    following_users = fields.Nested('FollowingSchema', many=True)
    following_current_user = fields.Nested('FollowingSchema', many=True)
    # following_user = fields.Nested('FollowingSchema', many=True)
    comments = fields.Nested('CommentSchema', many=True)

class SimpleUserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ('password_hash', 'email')

