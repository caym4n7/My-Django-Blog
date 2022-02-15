from .models import Comment, Post
from django.forms import ModelForm, Form
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ('content',)


class PostForm(ModelForm):
	content = SummernoteTextFormField()
	description = SummernoteTextField()
	class Meta:
		model = Post
		fields = ('title','category', 'post_image', 'description', 'content')
