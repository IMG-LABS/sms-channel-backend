from django.db import models

class UserPriviledges(models.Model):
	"""
	Contains the user priviledges (e.g.: HOD, Hobbies Club OC, etc)
	"""
	code = models.CharField(max_field=40, null=False, blank=False)
	description = models.TextField()

	def __unicode__(self):
		return self.code

class PhoneBookGroup(models.Model):
	"""
	Contains the segment into which phone book is divided
	"""
	name = models.CharField(max_length=40, null=False, blank=False)

	def __unicode__(self):
		return self.name

class PhoneBook(models.Model):
	"""
	Contact database
	"""
	name = models.CharField(max_length=40, null=False, blank=False)
	phone_number = models.IntegerField(null=False, blank=False)
	added_by = models.ForeignKey('user', null=False, blank=False)

	# unique_together = (("added_by", "phone_number"),)

	def __unicode__(self):
		return self.name

class SMSLog(models.Model):
	"""
	Log of the sent SMSs
	"""
	SUCCESS_MSG = (
		('0', 'SUCCESS'),
		('1', 'FAILED')
	)
	user = models.ForeignKey('user', null=False, blank=False)
	sent_to = models.ForeignKey('phoneBookGroup', null=False, blank=False)
	sent_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)
	success = models.IntegerField(null=False, blank=False, choices=SUCCESS_MSG)

	def __unicode__(self):
		return self.user + " - " self.sent_to