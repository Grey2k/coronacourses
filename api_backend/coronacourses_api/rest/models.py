from django.contrib.auth.models import User
from django.db import models
import base64
import json
import os


def _gen_course_id():
    return base64.urlsafe_b64encode(os.urandom(16))[:16]


class Course(models.Model):
    course_id = models.CharField(max_length=16, unique=True, default=_gen_course_id)
    name = models.TextField(null=False)
    kind = models.TextField()
    lecturer = models.TextField()
    description = models.TextField()


class CourseMaintainer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class PDFSlide(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    source_file = models.TextField()
    files = models.TextField()  # JSON with the files

    def set_files(self, files:list):
        self.files = json.dumps({"files": files})
    
    def get_files(self):
        return json.loads(self.files)["files"]
