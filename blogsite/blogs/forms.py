from django.forms import modelform_factory
from .models import blog,topic

topicform = modelform_factory(topic,fields=['topicname'])
blogform = modelform_factory(blog,fields=['title','body','date','topicname','thumb'])