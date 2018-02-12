from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Post(models.Model):

	user = models.ForeignKey(
		'auth.User',
		verbose_name='Yazar',
	 	related_name='posts',
		on_delete=models.CASCADE,
		)
	title = models.CharField(max_length=120,verbose_name='BAŞLIK')
	content = RichTextField(verbose_name='İÇERİK')
	publishing = models.DateTimeField(verbose_name='YAYINLANMA TARİHİ',auto_now_add=True)
	image = models.ImageField(null=True, blank=True)
	slug = models.SlugField(unique=True, editable=False,max_length=130)


	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('posst:detail',kwargs={'slug':self.slug})
		#return "/post/{}".format(self.id)


	def get_create_url(self):
		return reverse('posst:create')


	def get_update_url(self):
		return reverse('posst:update',kwargs={'slug':self.slug})


	def get_delete_url(self):
		return reverse('posst:delete',kwargs={'slug':self.slug})


	def get_unique_slug(self):
		slug=slugify(self.title.replace('ı','i'))
		unique_slug=slug
		counter=1
		while Post.objects.filter(slug=unique_slug).exists():
			unique_slug='{}-{}'.format(slug,counter)
			counter+=1
		return unique_slug

	def save(self,*args,**kwargs):
		if not self.slug:
			self.slug=self.get_unique_slug()
		return super(Post,self).save(*args,**kwargs)

	class Meta:
		ordering=['-publishing','id']


class Comment(models.Model):

	#ForeignKey kullanma amacımız bir postun birden fazla yorumu olabilir ama bir yorum sadece bir posta aittir
	#on_delete_models.CASCADE bir post silindiğinde yapilan yorumlarıda beraberinde siler
	post = models.ForeignKey(
		'post.Post',
		related_name='comments',
		on_delete=models.CASCADE,
		)

	name=models.CharField(max_length=200, verbose_name='ISIM')
	content = models.TextField(verbose_name='YORUM')

	createdTime=models.DateTimeField(auto_now_add=True)
