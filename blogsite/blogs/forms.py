from django.forms import modelform_factory
from .models import blog

blogform = modelform_factory(blog,fields=['title','slug','body','date'])