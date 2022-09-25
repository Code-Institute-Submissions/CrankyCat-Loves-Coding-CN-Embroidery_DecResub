from django.shortcuts import redirect, reverse
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.contrib import messages


from .models import Coupon
from .forms import CouponApplyForm


@require_POST
def coupon_apply(request):
    """a view to apply coupon"""
    now = timezone.now()
    form = CouponApplyForm(request.POST)

    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(
                code__iexact=code,
                valid_from__lte=now,
                valid_to__gte=now,
                active=True
            )
            request.session['coupon_id'] = coupon.id
            print(request.session['coupon_id'], 'coupon')
            messages.success(request, 'Discount added to your bag')

        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
            messages.error(request, 'Please add a valid promotion code')

    return redirect(reverse('view_bag'))
