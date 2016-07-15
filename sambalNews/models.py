from django.db import models

import mongoengine
from mongoengine import *
from mongoengine.django.auth import User
import datetime

# Create your models here.


class CustomUser(Document):
    user = ReferenceField(User)
    tags = ListField(StringField(max_length=30))
    validation_number = IntField(default=1)

class Comment(EmbeddedDocument):
    content = StringField()
    #  name = StringField(max_length=120)
    author = ReferenceField(CustomUser)
    date = DateTimeField()
    like = IntField(default=0)

class Summary(Document):
    image_index = FileField()
    publish_date = DateTimeField(default=datetime.datetime.now)
    title = StringField(max_length=120, required=True)

    source = URLField()
    category = StringField()
    tags = ListField(StringField(max_length=30))

    summary = StringField()
    like = IntField(default=0)
    dislike = IntField(default=0)

    seen = IntField(default=0)
    cum_num = IntField(default=0)

    is_hot = BooleanField(default=False)
    is_condid = BooleanField(default=False)

    is_valid = BooleanField(default=False)

    meta = {'indexes': [
        {'fields': ['$title', "$summary"],
         'default_language': 'english',
         'weights': {'title': 10, 'summary': 2}
        }
    ]}

class News(Document):
    summary = ReferenceField(Summary, reverse_delete_rule=mongoengine.CASCADE)
    #  image_index = FileField()
    #  publish_date = DateTimeField()
    #  title = StringField(max_length=120, required=True)

    #  source = URLField()
    #  category = StringField()
    #  tags = ListField(StringField)

    #  summary = StringField()
    text = StringField()
    gallery = ListField(FileField)

    comments = ListField(EmbeddedDocumentField(Comment))
    #  like = IntField()
    #  dislike = IntField()

    #  seen = IntField()
    #  cum_num = IntField()
