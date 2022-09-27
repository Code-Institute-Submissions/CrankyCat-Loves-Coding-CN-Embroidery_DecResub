from django.shortcuts import HttpResponse, get_object_or_create
from comment.models import User, Discussion, LikeNum
from django.contrib import messages


def addlike(request, id):
    if request.session.get('username') and request.session.get('uid'):
        username = request.session.get('username')
        user = User.objects.get(username=username)
    else:
        messages.error(request, f'Something went wrong!')
        return HttpResponse(status=500)

    try:
        if Discussion.objects.get(id=id):
            d = Discussion.objects.get(id=id)
            if user:
                record, flag = LikeNum.objects.get_object_or_create(user=user,discussion=d)
            if flag:
                d.like += 1
                d.save()
            else:
                d.like -= 1
                d.save()

                LikeNum.objects.get(user=user, discussion=d).delete()
            return render(request, 'products.html', {
                'ln':LikeNum.objects.fitter(user=user)
            })
    except Exception as e:
        messages.error(request, f'Something went wrong!')
        return HttpResponse(status=500)