# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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

# Create your models here.
class Videos(models.Model):
    title = models.CharField(max_length=100)
    transcript = models.CharField(max_length=1000000)
    author = models.CharField(max_length=60)
    publication_date = models.DateField()
    condition = models.CharField(max_length=4, choices=CONDITIONS)