import random
import string

def code_generator(size=4,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instace,size=4):
    new_code=code_generator(size=size)
    RickUrlClass=instace.__class__
    qs_exists=RickUrlClass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        create_shortcode(size=size)
    return new_code