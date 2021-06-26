from django.db import models


# Create your models here.
# 文章信息表
class Paper(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)  # 论文的标题
    link = models.TextField()  # 论文链接
    content = models.TextField(null=True,default='')  # 论文的摘要
    sch_key = models.CharField(max_length=200,default='')  # 论文的搜索词
    datetime = models.CharField(max_length=20,default='')  # 论文的发表年期
    public_year = models.CharField(max_length=20,default='')  # 论文的年份
    journal = models.CharField(max_length=20,default='')  # 期刊杂志
    local_url = models.CharField(max_length=20,default='')  # 文章资源分布
    cite=models.IntegerField(default=0);# 引用数
    download=models.IntegerField(default=0);# 下载数量
    funds = models.CharField(max_length=200,default='')  # 基金
    keywords = models.CharField(max_length=200,default='')  # 关键字
    user=models.CharField(max_length=200,default='')
    class Meta:
        unique_together = (("title", "journal"))


# 关键词表
class Keyword(models.Model):
    id = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length=20,unique=True)  # 搜索过的关键词
    counts=models.IntegerField(default=1);
    url = models.TextField(null=True)  # 关键词的url


# 文章与关键词对应
class PaperToKeyword(models.Model):
    paper_id = models.ForeignKey(Paper, on_delete=models.CASCADE)
    keyword_id = models.ForeignKey(Keyword, on_delete=models.CASCADE)


# 学校
class School(models.Model):
    id = models.AutoField(primary_key=True)
    school = models.CharField(max_length=100, default='', unique=True)
    url = models.TextField()


# 文章与学校
class PaperToSchool(models.Model):
    paper_id = models.ForeignKey(Paper, on_delete=models.CASCADE)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE,)


# 作者
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100, default='',unique=True)
    url = models.TextField()


# 文章与作者对应
class PaperToAuthor(models.Model):
    paper_id = models.ForeignKey(Paper, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)


# 作者与关键词对应
class AuthorToKeyword(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    keyword_id = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    counts = models.IntegerField(default=0);


# 学校与关键词对应
class SchoolToKeyword(models.Model):
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    keyword_id = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    counts = models.IntegerField(default=0);



# 基金
class Fund(models.Model):
    id = models.AutoField(primary_key=True)
    fund = models.CharField(max_length=100, unique=True)


# 基金与关键词对应
class FundToKeyword(models.Model):
    fund_id = models.ForeignKey(Fund, on_delete=models.CASCADE)
    keyword_id = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    counts = models.IntegerField(default=0);


# 时间
class Year(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=20, unique=True)


# 时间与关键词对应
class YearToKeyword(models.Model):
    year_id = models.ForeignKey(Year, on_delete=models.CASCADE)
    keyword_id = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    counts = models.IntegerField(default=0);
