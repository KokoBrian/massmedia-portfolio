from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    raw_description = models.TextField()
    description = models.TextField(blank=True)
    media_type = models.CharField(max_length=50,
        choices=[
            ("film", "Film"),
            ("photo", "Photography"),
            ("article", "Article"),
            ("podcast", "Podcast"),
            ("design", "Design")
        ])
    thumbnail = models.ImageField(upload_to="thumbnails/")
    created_at = models.DateField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class GalleryItem(models.Model):
    image = models.ImageField(upload_to="gallery/")
    caption = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
