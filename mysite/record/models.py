#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models, utils
import os
from uuid import uuid4
from django.utils.encoding import python_2_unicode_compatible




def pic_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join('records/', filename)





@python_2_unicode_compatible
class Record(models.Model):
    class Meta:
        verbose_name='记录'
        verbose_name_plural='我的流水账'
    title=models.CharField(max_length=100,verbose_name='标题')
    banner=models.ImageField(
        upload_to=pic_upload_path,
        verbose_name='顶部封面',
    )
    article_description=models.CharField(max_length=200,verbose_name='全文概览')

    def __str__(self):
        return self.title


