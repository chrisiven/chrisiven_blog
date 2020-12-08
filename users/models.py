from django.db import models

# Create your models here.




class UserProfile(models.Model):
    username = models.CharField(verbose_name="作者名称(艺名)", max_length=32)
    email = models.EmailField(verbose_name="邮箱")
    user_id = models.CharField(verbose_name="作者id,方便查询的时候用",unique=True)
    articles = models.ForeignKey("Article", on_delete=models.CASCADE, verbose_name="文章",
                                 related_name="A")  # 一个作者应该有很多的文章,而通常来说 一篇文章只有一个作者 所以是一对多
    class Meta:
        db_table = "userprofile"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

