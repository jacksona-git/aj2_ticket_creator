from django.db import models

# Create Ticket Model ... This is reflect in the SQL DB automation when migration occurs
 
class Ticket(models.Model):
    problem_desc = models.CharField(max_length=100)
    asset_name = models.CharField(max_length=100)
    asset_id = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When i was update
    #creator is a foriegn key and delete ticket creator if all reference connecting are deleted 
    creator = models.ForeignKey('auth.User', related_name='tickets', on_delete=models.CASCADE)





