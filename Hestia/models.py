# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime

CONDITIONS = (
        ("ASD", "Autism Spectrum Disorders"),
        ("AD", "Attachment Disorders"),
        ("ADHD", "Attention Deficit/Hyperactivity Disorder"),
        ("A", "Autism"),
        ("CD", "Conduct Disorder"),
        ("DoWE", "Disorder of Written Expression"),
        ("DMDD", "Disruptive Mood Dysregulation Disorder"),
        ("Enc", "Encopresis"),
        ("Enu", "Enuresis"),
        ("ELD", "Expressive Language Disorder"),
        ("MD", "Mathematics Disorder"),
        ("ID", "Intellectual Disability"),
        ("OCD", "Obsessive-Compulsive Disorder"),
        ("ODD", "Oppositional Defiant Disorder"),
        ("ReD", "Reading Disorder"),
        ("RuD", "Rumination Disorder"),
        ("SM", "Selective Mutism"),
        ("SAD", "Separation Anxiety Disorder"),
        ("SCD", "Social Communication Disorder"),
        ("SMD", "Stereotypic Movement Disorder"),
        ("S", "Stuttering"),
        ("TD","Tourette's Disorder"),
        ("TTD", "Transient Tic Disorder"),
)


province_choices = {
	('AB','Alberta'),
	('BC','British Columbia'),
	('SK','Saskatchewan'),
	('MB','Manitoba'),
	('ON','Ontario'),
	('QC','Quebec'),
	('PE','Prince Edward Island'),
	('NS','Nova Scotia'),
	('NL','Newfoundland and Labrador'),
	('NB','New Brunswick'),
	('NT','Northwest Territories'),
	('NU','Nunavut'),
	('YT','Yukon')
}

phone_regex = RegexValidator(regex=r'^\+?1?\d{10,12}$',
				message="Phone number must be entered in the format: '+16045555555'.")

# Create your models here.
class Question(models.Model):
	author  = models.ForeignKey("User", on_delete=models.CASCADE, default="")
	title   = models.CharField(max_length=150)
	body    = models.TextField(max_length=1000)
	date    = models.DateTimeField(default=datetime.now, blank=True)
	upvotes = models.IntegerField()
	#answers = models.ManyToManyField("Answer") #error, reverse query clash

	def __str__(self):
		return self.title + "-" + str(self.upvotes)

class Answer(models.Model):
	author   = models.ForeignKey("User", on_delete=models.CASCADE, default="")
	question = models.ForeignKey("Question", on_delete=models.CASCADE, default="")
	body     = models.TextField(max_length=1000)
	date     = models.DateTimeField(default=datetime.now, blank=True)
	upvotes  = models.IntegerField()

class Video(models.Model):

    title = models.CharField(max_length=100, verbose_name="Title")
    transcript = models.CharField(max_length=1000000, verbose_name="Transcript")
    author = models.CharField(max_length=60, verbose_name="Author")
    publication_date = models.DateField()
    conditionName = models.ForeignKey("Condition", on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.title + '-' + self.author

class Condition(models.Model):
    conditionName = models.CharField(max_length=10, choices=CONDITIONS, verbose_name="Condition Name")
    subCondition = models.CharField(max_length=50, verbose_name="Symptoms")
    description = models.CharField(max_length=1000, verbose_name="Description")
    writtenBy = models.CharField(max_length=1000, verbose_name="Source/Written by")

    def __str__(self):
        return self.conditionName + '-' + self.description


class User(models.Model):
    firstName = models.CharField(max_length=75, verbose_name="First Name")
    lastName = models.CharField(max_length=75, verbose_name="Last Name")
    email = models.EmailField(verbose_name="E-mail")
    phoneNumber = models.CharField(validators=[phone_regex], max_length=12, blank=True, null=True,
                                        verbose_name="Number")

    city = models.CharField(max_length=30, blank=True, null=True, verbose_name="City")
    province = models.CharField(max_length=20, choices=province_choices, blank=True, null=True,
                                    verbose_name="Province")
    postalCode = models.CharField(max_length=6, blank=True, null=True, verbose_name="Postal Code")


    numberOfUpvotes = models.IntegerField(blank=True, null=True, verbose_name="Number of Upvotes")
    userSince = models.DateField(max_length=75, default="", blank=True, null=True, verbose_name="User Since")

    def __str__(self):
        return self.firstName + "-" + str(self.numberOfUpvotes)

