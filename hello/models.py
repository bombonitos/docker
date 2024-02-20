from django.db import models

#class Toys(models.Model):
    #kitty
    #mymelody
    #kuromi
    #keroppi
    #pochacco
    #badtzmaru
    #cinnamoroll
    #pompompurin

class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return "Пользователь %s %s" % (self.email, self.name,)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kitty = models.ForeignKey('Kitty', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)



class Kitty(models.Model):
    name = models.CharField(max_length=100)
    description1 = models.CharField(max_length=500, default='')
    description2 = models.CharField(max_length=500, default='')
    description3 = models.CharField(max_length=500, default='')
    description4 = models.CharField(max_length=500, default='')
    description5 = models.CharField(max_length=500, default='')
    description6 = models.CharField(max_length=500, default='')
    description7 = models.CharField(max_length=500, default='')
    category = models.CharField(max_length=200, default='')
    price = models.CharField(max_length=100000, default='')
    size = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='images')
    image1 = models.ImageField(upload_to='images')
    image2 = models.ImageField(upload_to='images')
    image3 = models.ImageField(upload_to='images')




class Orders(models.Model):
    name = models.CharField(max_length=100)
    card = models.CharField(max_length=16, default='')
    phonenumber = models.CharField(max_length=200, default='')
    date = models.CharField(max_length=20, default='')


from django.db import models

class Order(models.Model):
    full_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16)
    phone_number = models.CharField(max_length=15)
    # Другие поля, которые вам могут понадобиться

    def __str__(self):
        return f"Order #{self.id}"