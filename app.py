from models.post import Post
from blog import Blog
from datbase import Database
Database.initialize()
blog=Blog(author="himanshu",title="asdasd",description="adad",id=2131234213341342342)
blog.new_post()
blog.save_to_mongo()
blog.from_mongo()
blog.get_posts()