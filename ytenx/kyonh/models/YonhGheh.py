# coding=utf-8
from django.db import models

#十六韻攝
class YonhCjep(models.Model):
  #通江止遇蟹臻山效果假宕梗曾流深咸
  dzih = models.CharField(max_length = 1, primary_key = True)
  
  class Meta:
    app_label = 'kyonh'
  
  def __unicode__(self):
      return self.dzih;

#韻系
class YonhGheh(models.Model):
  #代表字
  dzih = models.CharField(max_length = 2, primary_key = True)
  #攝
  cjep = models.ForeignKey(YonhCjep, db_index = True)
  
  class Meta:
    app_label = 'kyonh'
  
  def __unicode__(self):
      return self.dzih;
