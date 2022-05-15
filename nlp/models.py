from django.db import models

class PSummary1(models.Model):
    id = models.IntegerField(default=1,null=False,primary_key=True)
    paragraph = models.TextField(max_length=10000)
    length = models.IntegerField(verbose_name="length of summary(sentences)", blank=True)
    summary = models.TextField(max_length=10000, default="", blank=True)

    def __str__(self):
        return "form1"

    def save(self, *args, **kwargs):
        super(PSummary1, self).save(*args, **kwargs)
        return self

    def create(self, *args, **kwargs):
        super(PSummary1, self).create(*args, **kwargs)
        return self

class PSummary2(models.Model):
    id = models.IntegerField(default=2,null=False,primary_key=True)
    paragraph = models.TextField(max_length=10000)
    length = models.IntegerField(verbose_name="length of summary(sentences)", blank=True)
    summary = models.TextField(max_length=10000, default="", blank=True)

    def __str__(self):
        return "form2"

    def save(self, *args, **kwargs):
        super(PSummary2, self).save(*args, **kwargs)
        return self

    def create(self, *args, **kwargs):
        return self.create(*args, **kwargs)

class Cookie(models.Model):
    id = models.IntegerField(default=1,null=False,primary_key=True)
    f1_submitted = models.BooleanField(default=False)
    f2_submitted = models.BooleanField(default=False)

class File(models.Model):
    length = models.IntegerField(verbose_name="length of summary(sentences)", blank=True)
    uploaded_file = models.FileField(upload_to="media", null=True, blank=True)
    file_contents = models.TextField(max_length=10000, default="", blank=True)
    summary_of_file_contents = models.TextField(max_length=10000, default="", blank=True)

class DisplayFile(models.Model):
    length = models.IntegerField(blank=True, default=1)
    file_contents = models.TextField(max_length=10000)
    summary_of_file_contents = models.TextField(max_length=10000)
