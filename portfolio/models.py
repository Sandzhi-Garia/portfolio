from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.title

class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return f"Image for {self.blog.title}"


class WorkExperience(models.Model):
    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200, default="Unknown Company")
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} at {self.company_name}"


class Education(models.Model):
    school_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.school_name} – {self.degree}"


class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    link = models.URLField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey('Projects', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f"Image for {self.project.title}"

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    resume_file = models.FileField(upload_to='resumes/', blank=True, null=True)
    def __str__(self):
        return self.name

class ContactMe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.title