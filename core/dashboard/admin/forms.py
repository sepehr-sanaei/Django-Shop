from django.contrib.auth import forms as auth_forms
from django import forms
from django.utils.translation import gettext_lazy as _


class AdminPasswordChangeForm(auth_forms.PasswordChangeForm):
    error_messages = {
        "password_mismatch": _("رمزعبور های جدید با هم مطابقت ندارند!"),
        "password_incorrect": _(
            "رمزعبور فعلی شما اشتباه وارد شده است. تصحیح نمایید!"
        ),
    }
    # we can Do this instead of creating a class in template
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs['class'] = "form-control dir='rtl'"
        self.fields['new_password1'].widget.attrs['placeholder'] = "رمزعبور جدید را وارد کنید"
        
        