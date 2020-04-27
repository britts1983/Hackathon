from django.db import models

# Create your models here.
STATUS = [
        ('保留中','保留中'),
        ('確認中', '確認中'),
        ('承認された', '承認された'),
        ('斥ける', '斥ける'),
    ]

class hackathon_applicants(models.Model):
    名 = models.CharField(max_length=60, null=True, blank=True)
    ミドルネーム = models.CharField(max_length=61, null=True, blank=True)
    苗字=models.CharField(max_length=60, null=True, blank=True)
    性別 = models.CharField(max_length=6, null=True, blank=True)
    生年月日 = models.DateField(null=True,blank=True)
    電話 = models.CharField(max_length=11, null=True, blank=True)
    メールID = models.EmailField(max_length=100, null= True, blank=True)
    所属 = models.CharField(max_length=60, null=True, blank=True)
    部署名 = models.CharField(max_length=60, null=True, blank=True)
    FACEBOOK_ID = models.CharField(max_length=50, null=True, blank=True)
    TWITTER_ID = models.CharField(max_length=50, null=True, blank=True)
    GITHUB_ID= models.CharField(max_length=50, null=True, blank=True)
    スキル = models.CharField(max_length=150, null=True, blank=True)
    レベル=models.CharField(max_length=50, null=True, blank=True)
    経験 =models.IntegerField(null= True, blank=True)
    ポートフォリオ_URL= models.CharField(max_length=300, null=True, blank=True)
    備考 = models.CharField(max_length=10000, null=True, blank=True)
    登録済み = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    更新済み = models.DateTimeField(auto_now=True,null=True, blank=True)
    状態= models.CharField(max_length=10,choices=STATUS,null=True, blank=True, default="保留中")
    管理者の備考 = models.CharField(max_length=1000, null=True, blank=True)
    国籍 = models.CharField(max_length=1000, null=True, blank=True)

