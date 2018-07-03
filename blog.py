import datetime
import uuid
from models.post import Post
from datbase import Database
class Blog(object):
    def __init__(self,author,title,description,id):
        self.author=author
        self.title=title
        self.description=description
        self.id=uuid.uuid4().hex if id is None else id
    def new_post(self):
        title=input("enter post title")
        content=input("Enter post content")

        post=Post(blog_id=self.id,
                  title=title,
                  content=content,
                  author=self.author,
                  date=datetime.datetime.utcnow())
        post.save_to_mongo()
    def get_posts(self):
        return Post.from_blog(self.id)
    def save_to_mongo(self):
        Database.insert()(collection="blogs",data=self.json())
    def json(self):
        return{
            'author':self.author,
            'title':self.title,
            'description':self.description,
            'id':self.id
        }
    @staticmethod
    def  from_mongo(self,id):
        blog_data=Database.find_one(collection='blog',query={'id':id})
        return Blog(author=blog_data['author'],
                    title=blog_data['title'],
                    description=blog_data['description'],
                    id=blog_data['id'])