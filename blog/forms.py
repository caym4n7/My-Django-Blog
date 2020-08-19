from .models import Comment, Post
from django import forms
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('content',)


class PostForm(forms.ModelForm):
	content = SummernoteTextFormField()
	description = SummernoteTextField()
	class Meta:
		model = Post
		fields = ('title','category', 'post_image', 'description', 'content')
