from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=125)
    image = models.FileField()
    
    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField()

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=120)
    image1 = models.FileField()
    time = models.DateTimeField(auto_now_add=True)
    overview = models.CharField(max_length=300)
    image2 = models.FileField()
    description = models.TextField()
    author = models.CharField(max_length=300)
    author_image = models.FileField()
    author_name = models.CharField(max_length=125)
    

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=400)
    message = models.TextField()

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=125)
    image = models.FileField()
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.CharField(max_length=100)
    organizer = models.CharField(max_length=150)
    email = models.CharField(max_length=100)


    def __str__(self):
        return self.title

class Leader(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField()
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    username = models.CharField(max_length=250, default='Anonymous')
    email = models.CharField(max_length=250, default='Anonymous')
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField()
    overview = models.CharField(max_length=250)
    percent = models.CharField(max_length=10)
    raised_amount = models.CharField(max_length=20)
    goal_amount = models.CharField(max_length=20)
    sponsor = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Instagram(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField()

    def __str__(self):
        return self.title
