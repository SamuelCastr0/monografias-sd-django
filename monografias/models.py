from django.db import models

class Advisor(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    lattes = models.URLField()
    google_scholar = models.URLField()
    research_gate = models.URLField()
    linkedin = models.URLField()
    orcid = models.URLField()
    github = models.URLField()

    def __str__(self):
        return (self.name)

class CoAdvisor(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    lattes = models.URLField()
    google_scholar = models.URLField()
    research_gate = models.URLField()
    linkedin = models.URLField()
    orcid = models.URLField()
    github = models.URLField()

    def __str__(self):
        return (self.name)

class Author(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    lattes = models.URLField()
    google_scholar = models.URLField()
    research_gate = models.URLField()
    linkedin = models.URLField()
    orcid = models.URLField()
    github = models.URLField()

    def __str__(self):
        return (self.name)

class Monography(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    co_advisor = models.ForeignKey(CoAdvisor, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add = True)
    summary = models.TextField(max_length=100)
    key_words = models.CharField(max_length=100)
    university = models.CharField(max_length=80)
    course = models.CharField(max_length=50)
    monography = models.URLField()

    def __str__(self):
        return (self.title)

