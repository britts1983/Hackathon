from django.shortcuts import render_to_response
from django.shortcuts import render, redirect
from .models import hackathon_applicants
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import ImageUploadForm
from . import forms



def register(request):

        if request.method == "POST":
          fa = request.POST.get("usrnm1")
          ml = request.POST.get("usr3")
          la = request.POST.get("usrnm2")
          ph = request.POST.get("phone")
          gn= request.POST.get("radio")
          db = request.POST.get("dob")
          md = request.POST.get("emails")
          af= request.POST.get("aff")
          dp= request.POST.get("dept")
          fbk = request.POST.get("fb")
          twt =request.POST.get("tw")
          gtb= request.POST.get("gt")
          skr = request.POST.get("sks")
          lvl = request.POST.get("lvvv")
          exp = request.POST.get("expp")
          purl= request.POST.get("upurl")
          nationality = request.POST.get("jap")

          rmrk = request.POST.get("rmks")


          user1 = 	hackathon_applicants(名=fa,ミドルネーム=ml, 苗字=la,  電話=ph,  性別=gn, 生年月日=db, メールID=md,
                 所属=af, 部署名=dp, FACEBOOK_ID=fbk,
                 TWITTER_ID=twt, GITHUB_ID=gtb, スキル=skr, レベル=lvl,経験=exp,  ポートフォリオ_URL=purl,備考=rmrk,国籍= nationality)
          user1.save()




          return redirect('/')
        else:

                return render(request, 'register.html')



def HOME(req):
        return render(req,'index.html')


def regind(request):
  if request.method == "POST":
    fa = request.POST.get("usrnm1")
    ml = request.POST.get("usr3")
    la = request.POST.get("usrnm2")

    ph = request.POST.get("phone")
    gn = request.POST.get("radio")
    db = request.POST.get("dob")
    md = request.POST.get("emails")
    af = request.POST.get("aff")
    dp = request.POST.get("dept")
    fbk = request.POST.get("fb")
    twt = request.POST.get("tw")
    gtb = request.POST.get("gt")
    skr = request.POST.get("sks")
    lvl = request.POST.get("lvvv")
    exp = request.POST.get("expp")
    purl = request.POST.get("upurl")

    rmrk = request.POST.get("rmks")
    nationality = request.POST.get("ind")

    user1 = hackathon_applicants(名=fa,ミドルネーム=ml, 苗字=la,  電話=ph,  性別=gn, 生年月日=db, メールID=md,
                 所属=af, 部署名=dp, FACEBOOK_ID=fbk,
                 TWITTER_ID=twt, GITHUB_ID=gtb, スキル=skr, レベル=lvl,経験=exp,  ポートフォリオ_URL=purl,備考=rmrk,国籍= nationality)
    user1.save()



    return redirect('/')
  else:

    return render(request, 'regind.html')


from django.http import HttpResponseForbidden
