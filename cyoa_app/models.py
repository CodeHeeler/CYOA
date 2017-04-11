from django.db import models


class Page(models.Model):
    text = models.TextField()
    image = models.CharField(max_length=1000, null=True, blank=True)


    def __repr__(self):
        return self.text[:50] + str(self.id)

    def __str__(self):
        return self.text[:50] + str(self.id)


class Choice(models.Model):
    from_page = models.ForeignKey(Page, related_name='from_page')
    to_page = models.ForeignKey(Page, related_name='to_page')
    to_page_url = models.CharField(max_length=250, null=True)

    text = models.TextField()


    def __repr__(self):
        return self.text[:50]

    def __str__(self):
        return self.text[:50]
