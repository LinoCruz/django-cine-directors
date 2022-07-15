from django.db import models

# My models here.
# The Director class is a model that has a name, last_name and age.
class Director(models.Model):
    name = models.CharField(max_length=64, help_text="Write the author's name.")
    last_name = models.CharField(max_length=100, help_text="Write the last name of the author.")
    age = models.IntegerField
    
    
    def __str__(self):
        return self.name
    
    
# The Genre class is a model that has a name field that is a CharField with a max length of 30. 
# 
# The help_text is a string that will be displayed when a user hovers over the field. 
# 
# The __str__ method is a special method that returns a string representation of the object. 
# 
# In this case, it returns the name of the genre
class Genre(models.Model):
    name = models.CharField(max_length=30, help_text="Select the genre of the movie.")
    
    def __str__(self):
        return self.name
    
    
    
# The Movie class is a model that has a title, author, summary, and genre. 
# 
# The title is a CharField, which is a string. The author is a ForeignKey, which is a many-to-one
# relationship. The summary is a TextField, which is a string. The genre is a ManyToManyField, which
# is a many-to-many relationship
class Movie(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    summary  = models.TextField(max_length=200, help_text="Description of the movie")
    genre = models.ManyToManyField(Genre)
    
    def __str__(self):
        return self.title

