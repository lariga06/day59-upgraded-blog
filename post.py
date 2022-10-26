import requests

BLOG_API_ENDPOINT = 'https://api.npoint.io/589c0b92da9cdc2fc6ca'
# https://www.npoint.io/docs/589c0b92da9cdc2fc6ca


class AllPosts:
    def __init__(self):
        response = requests.get(BLOG_API_ENDPOINT)
        response.raise_for_status()
        self.result = response.json()

class Post:
    def __init__(self):
        self.id_ = None
        self.title_=None
        self.subtitle_=None
        self.body_=None
        self.author_=None
        self.date_=None


# print(all_posts.result)
#
# post = Post()
# for p in all_posts.result:
#     if p['id']==2:
#         post.id_ = p['id']
#         post.title_ = p['title']
#         post.subtitle_ = p['subtitle']
#         post.body_ = p['body']
#
#
# print(post.id_)
# print(post.title_)
