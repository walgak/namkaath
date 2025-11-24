from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('mobile', 'Mobile Apps'),
        ('web', 'Web Platforms'),
        ('ai', 'AI & Data'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200, help_text="e.g. React, Django, AWS")
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Inquiry(models.Model):
    PROJECT_TYPES = [
        ('Mobile App', 'Mobile App'),
        ('Web Platform', 'Web Platform'),
        ('AI Integration', 'AI Integration'),
        ('Digital Marketing', 'Digital Marketing'),
        ('Retail System', 'Retail System'),
    ]
    
    # Budget field removed

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    project_type = models.CharField(max_length=50, choices=PROJECT_TYPES)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.project_type}"