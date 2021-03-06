from django.db import models
class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    time_to_read=models.PositiveIntegerField()
    main_image = models.ImageField(upload_to="blogs")
    image1=models.BooleanField(default=True)
    first_image=models.ImageField(upload_to="blogs",null=True,blank=True)
    image2=models.BooleanField(default=True)
    second_image=models.ImageField(upload_to="blogs",null=True,blank=True)
    image3=models.BooleanField(default=True)
    third_image=models.ImageField(upload_to='blogs',null=True,blank=True)
    image4=models.BooleanField(default=True)
    fourth_image=models.ImageField(upload_to="blogs",null=True,blank=True)
    
   
    paragraph1=models.BooleanField(default=True)
    paragraph_1=models.TextField(null=True,blank=True)
    heading2=models.BooleanField(default=True)
    heading_2=models.CharField(max_length=200,null=True,blank=True)
    paragraph2=models.BooleanField(default=True)
    paragraph_2=models.TextField(null=True,blank=True)
    heading3=models.BooleanField(default=True)
    heading_3=models.CharField(max_length=200,null=True,blank=True)
    paragraph3=models.BooleanField(default=True)
    paragraph_3=models.TextField(null=True,blank=True)
    heading4=models.BooleanField(default=True)
    heading_4=models.CharField(max_length=200,null=True,blank=True)
    paragraph4=models.BooleanField(default=True)
    paragraph_4=models.TextField(null=True,blank=True)

    date = models.DateField(auto_now_add=True)
    link1=models.BooleanField(default=False)
    link_1=models.CharField(max_length=200,null=True,blank=True)
    link_1_url=models.CharField(max_length=200,null=True,blank=True)
    link2=models.BooleanField(default=False)
    link_2=models.CharField(max_length=200,null=True,blank=True)
    link_2_url=models.CharField(max_length=200,null=True,blank=True)
    trending=models.BooleanField(default=False)
    def __str__(self):
        return self.title
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name