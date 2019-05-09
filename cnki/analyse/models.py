from django.db import models


# Create your models here.
# 文章信息表
class Paper(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)  # 论文的标题
    url = models.TextField()  # 论文链接
    description = models.TextField(null=True)  # 论文的摘要
    sch_key = models.CharField(max_length=200)  # 论文的搜索词
    public_year = models.CharField(max_length=20)  # 论文的发表日期
    source_type = models.CharField(max_length=20,default='')  # 文章资源分布
    local_url = models.CharField(max_length=20,default='')  # 文章资源分布
    paper_funds = models.CharField(max_length=200,default='')  # 文章资源分布
    paper_keywords = models.CharField(max_length=200,default='')  # 文章资源分布


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
