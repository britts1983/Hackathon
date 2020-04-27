from django.contrib import admin
from import_export import resources
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from .models import hackathon_applicants
from import_export import resources
from import_export.admin import  ImportExportActionModelAdmin, ExportActionMixin, ImportExportModelAdmin
from django.utils.safestring import mark_safe




class userAdmin(ImportExportActionModelAdmin):


    list_display = ('国籍','名', 'ミドルネーム','苗字', '電話','性別','生年月日','メールID','所属','部署名',
                    'FACEBOOK_ID','TWITTER_ID','GITHUB_ID','スキル','レベル','経験','ポートフォリオ_URL','備考','登録済み','更新済み','管理者の備考','状態')
    list_filter = ('レベル','性別','状態','国籍')
    search_fields = ('名','スキル', '経験')
    admin.site.site_header = "ハッカソン"
    admin.site.site_title = "ハッカソン"
    admin.site.index_title = "ハックソンプロジェクト"

    change_list_template = 'change_list_graph.html'
    js = 'list_filter_collapse.js'



admin.site.register(hackathon_applicants,userAdmin)
