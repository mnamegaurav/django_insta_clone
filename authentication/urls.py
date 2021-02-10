from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView,
    )
from django.contrib.auth.decorators import login_required

from authentication.views import (
    SignInView,
    SignUpView, 
    SignOutView,
    PRView, PRDone, PRConfirm, PRComplete
    )


urlpatterns = [
    path('',  SignInView.as_view(), name='signin_view'),
    path('signup/',  SignUpView.as_view(), name='signup_view'),
    path('signout/',  SignOutView.as_view(), name='signout_view'),

    path(
        'password/change/', 
        login_required(PasswordChangeView.as_view(
                        template_name = 'authentication/password_change.html',
                        success_url=reverse_lazy('password_change_done_view')
                    )),
        name='password_change_view'
        ),
    path(
        'password/change/done/', 
        login_required(PasswordChangeDoneView.as_view(
                        template_name = 'authentication/password_change_done.html',
                    )), 
        name='password_change_done_view'
        ),
    
    # path('password/reset/', PRView.as_view(), name='password_reset'),
    # path('password/reset/done/',  PRDone.as_view() ,name='password_reset_done'),
    # path('password/reset/confirm/<uidb64>/<token>', PRConfirm.as_view() , name='password_reset_confirm'),
    # path('password/reset/complete/', PRComplete.as_view() , name='password_reset_complete'),

    path('password/reset/', 
        PasswordResetView.as_view(
            email_template_name = 'authentication/password_reset_email.html',
            template_name = 'authentication/password_reset.html',
        ), 
        name='password_reset'),
    
    path('password/reset/done/',  
        PasswordResetDoneView.as_view(
            template_name = 'authentication/password_reset_done.html'
        ) ,
        name='password_reset_done'),

    path('password/reset/confirm/<uidb64>/<token>', 
        PasswordResetConfirmView.as_view(
            template_name = 'authentication/password_reset_confirm.html'
        ) , 
        name='password_reset_confirm'),

    path('password/reset/complete/', 
        PasswordResetCompleteView.as_view(
            template_name = 'authentication/password_reset_complete.html'
        ) , 
        name='password_reset_complete'),
]

# PasswordResetView ->> Ask for Email
# PasswordResetDoneView  ->> Show him success email message
# PasswordResetConfirmView  ->> Ask to set a new password
# PasswordResetCompleteView  ->>  Successfully set your password login