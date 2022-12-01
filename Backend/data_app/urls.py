from django.urls import path
from .views import *
#from account.views import SendPasswordResetEmailView, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView, UserPasswordResetView
urlpatterns = [
    # path('register/', UserRegistrationView.as_view(), name='register'),
    # path('login/', UserLoginView.as_view(), name='login'),
    # path('profile/', UserProfileView.as_view(), name='profile'),
    # path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    # #path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    # path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path("api/",UserDetailsView.as_view()),
    path("binsapi/",ManageBinsView.as_view()),
    path("wrkdetapi/",WorkerDetailsView.as_view()),
    path("trktrkapi/",TrackTruckView.as_view()),
    path("trkwrkapi/",TrackWorkerView.as_view()),
    path("cmptapi/",complaintView.as_view()),
    path("mnghsapi/",ManageHouseView.as_view()),
    path("pkpapi/",pickupView.as_view())
]