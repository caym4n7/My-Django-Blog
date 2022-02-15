from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from slugify import slugify

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
	slug = models.SlugField(max_length=50, unique=True, null=True, blank=True)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def get_absolute_url(self):
		from django.urls import reverse
		return reverse("profile", kwargs={"slug": str(self.slug)})

	def save(self, *args, **kwargs):
		self.slug = slugify(self.user.username)
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)



