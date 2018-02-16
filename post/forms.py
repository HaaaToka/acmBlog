from django import forms
from .models import Post,Comment
from captcha.fields import ReCaptchaField #sunucuya geçerken recaptcha sitesinden acmnin linkini ver!!!

class PostForm(forms.ModelForm):
	#captcha = ReCaptchaField()

	class Meta:
		model = Post
		fields=[
			'title',
			'content',
			'image',
			'tags',
		]

class CommentForm(forms.ModelForm):
	#captcha = ReCaptchaField()

	class Meta:
		model = Comment
		fields=[
			'name',
			'content',
		]
