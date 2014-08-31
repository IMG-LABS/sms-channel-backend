from django.db import models

class PhoneBook(models.Model):
	name = models.CharField(max_length=40, null=False, blank=False)
	phone_number = models.IntegerField(null=False, blank=False)
	added_by = models.ForeignKey('user', null=False, blank=False)

	# unique_together = (("added_by", "phone_number"),)

	def __unicode__(self):
		return self.name
