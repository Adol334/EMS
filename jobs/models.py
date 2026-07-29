from django.db import models

#Job model (represents a job listing in the database)
class Job(models.Model):
    title = models.CharField(max_length=200, db_column='job_title')    
    description = models.TextField()

    def __str__(self):
        return self.title
    
    #Custom database table name
    class Meta:
        db_table = 'jobs'