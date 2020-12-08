from django.db import models

# Create your models here.



class Article(models.Model):

    title = models.CharField(verbose_name="标题",max_length=32)
    content = models.TextField(verbose_name="内容")
    tag = models.ForeignKey("Tags",on_delete=models.CASCADE) #问题删除，关联就会删除
    article_id = models.CharField(max_length=11,unique=True,verbose_name="文章id,方便查询")
    article_time = models.DateTimeField(verbose_name="添加时间",auto_now_add=True)
    star = models.BooleanField(verbose_name="是否星标",default=False)

    class Meta:
        db_table = "article"
        verbose_name = "文章"
        verbose_name_plural = verbose_name


class Tags(models.Model):
    name = models.CharField(verbose_name="tag名称",unique = True,max_length=32)
    types = models.CharField(choices=((1,"问题"),(2,"文章")))
    class Meta:
        db_table = "tags"
        verbose_name = "标签"
        verbose_name_plural = verbose_name


class Thoughts(models.Model):
    content = models.TextField(verbose_name="感想内容")
    write_time = models.DateTimeField(auto_now_add=True,verbose_name="添加时间")
    class Meta:
        db_table = "thoughts"
        verbose_name = "感想"
        verbose_name_plural = verbose_name

class Question(models.Model):#问题集合
    title = models.CharField(verbose_name="问题名称",max_length=32,unique=True)
    content = models.TextField(verbose_name="问题内容") #我使用markdown编辑器
    slove = models.BooleanField(verbose_name="是否解决",default=False)
    tag = models.ForeignKey("Tags",on_delete=models.CASCADE)

    class Meta:
        db_table = "question"
        verbose_name = "问题"
        verbose_name_plural = verbose_name

# 不打算做给其他人登录，只给自己登录使用



"""
文章和标签的关系是
    文章可以有很多的标签,一个标签也可以贴很多文章.所以应该是多对多的关系
    
"""