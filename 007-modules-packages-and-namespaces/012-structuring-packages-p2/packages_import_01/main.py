import common
import common.validators as validators
import common.models as models

validators.is_boolean('True')
validators.is_json('{}')
validators.is_numeric(10)
validators.is_date('2019-01-01')

print('\n\n***** self *****')
for k in dict(globals()).keys():
    print(k)

print('\n\n***** common *****')
for k in common.__dict__.keys():
    print(k)

print('\n\n***** posts (package) *****')
for k in common.models.posts.__dict__.keys():
    print(k)
    
print('\n\n***** posts (package) *****')
for k in common.models.__dict__.keys():
    print(k)

"""
This will yield:

Traceback (most recent call last):
  File "main.py", line 22, in <module>
    example_post = common.models.posts.post.Post()
AttributeError: module 'common.models' has no attribute 'posts'
"""

try:
    example_post = common.models.posts.post.Post()
except AttributeError as e:
    print(e)

"""
We would need to do something like:

import common.models.posts.post
"""
# import common.models.posts.post
# import common.models.posts.posts
# import common.models.users.user

# example_post = common.models.posts.post.Post()
# example_posts = common.models.posts.posts.Posts()
# example_user = common.models.users.user.User()

john_post = models.Post()
john_posts = models.Posts()
john = models.User()

import common.helpers as helpers

calc = helpers.Calc()
print(f"{helpers.say_hello('Python')=}")
print(f"{helpers.factorial(5)=}")

"""
Fred says that this is bad technique and we should not put functional code in __init__.py files.
"""