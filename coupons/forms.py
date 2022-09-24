from django import forms


class CouponApplyForm(forms.Form):
    """form to allow user to enter coupon"""
    code = forms.CharField()
