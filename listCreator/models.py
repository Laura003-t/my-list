from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, primary_key=True, editable=False)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    

class Folder(models.Model):
    folderid = models.CharField(max_length=30, primary_key=True, editable=False, blank=True)
    folder_name = models.CharField(max_length=30)
    folder_description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.folder_name

    def save(self, *args, **kwargs):
        #Only create id if it doesn't already exist
        if not self.folderid:
            #Use username and '-f' to create the prefix of the id
            prefix = self.user.username + "-f"

            # Set the value of number
            current_count = Folder.objects.filter(user.username==self.user.username).count()
            number = current_count + 1

            # Set folderID
            folderID = f"{folder}{number}"


            #Add a number if this id already exists
            while Folder.objects.filter(folderid=folderID).exists():
                number += 1
                folderID = f"{prefix}{number}"

            # Set the folderid value
            self.folderid = folderID

        super().save(*args, **kwargs)



class List(models.Model):
    TYPE = [
        ("Bulletpoint", "Bulletpoint List"),
        ("Numbered", "Numbered List"),
        ("Checkbox", "Checkbox List"),
    ]

    listid = models.CharField(max_length=35, primary_key=True, editable=False, blank=True)
    list_title = models.CharField(max_length=30)
    list_description = models.CharField(max_length=255)
    list_type = models.CharField(max_length=17, choices=TYPE, default="Bulletpoint")
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.list_title

    def save(self, *args, **kwargs):
        #Only create id if it doesn't already exist
        if not self.listid:
            # Create a prefix for  the id
            prefix = self.folder.folderid + "-"

            #Set the value for the number
            current_count = List.objects.filter(folder.folderid==self.folder.folderid).count()
            number = current_count + 1

            # Set a value for the listID
            listID = f"{prefix}{number}"

            # Ensure that there is no other record with that same id
            while List.objects.filter(listid=listID).exists():
                number += 1
                listID = f"{prefix}{number}"

            # Set the value of listid
            self.listid = listID
        
        super().save(*args, **kwargs)

class ListMembers(models.Model):
    STATUS = [
        ("Nocheck", "No Check"),
        ("Checked", "Checked"),
    ]
    content = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default="Nocheck")
    parent_list = models.ForeignKey(List, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

