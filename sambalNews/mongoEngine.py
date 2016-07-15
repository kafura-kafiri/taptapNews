from mongoengine import *

from mongoengine import connect

db = connect('test_1')
db.drop_database('test_1')


connect('tumblelog')


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))
    meta = {'allow_inheritance': True}


class TextPost(Post):
    content = StringField()


class ImagePost(Post):
    image_path = StringField()


class LinkPost(Post):
    link_url = StringField()


if __name__ == '__main__':
    ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()

    post1 = TextPost(title='Fun with MongoEngine', author=ross)
    post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
    post1.tags = ['mongodb', 'mongoengine']
    post1.save()

    post2 = LinkPost(title='MongoEngine Documentation', author=ross)
    post2.link_url = 'http://docs.mongoengine.com/'
    post2.tags = ['mongoengine']
    post2.save()

    for post in Post.objects:
        print(post.title)
        print('=' * len(post.title))

        if isinstance(post, TextPost):
            print(post.content)

        if isinstance(post, LinkPost):
            print('Link:', post.link_url)

        print('*' * 10)

    for post in Post.objects(tags='mongodb'):
        print(post.title)

    num_posts = Post.objects(tags='mongodb').count()
    print('Found %d posts with tag "mongodb"' % num_posts)