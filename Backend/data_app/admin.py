from django.contrib import admin
from .models import *
#from .models import pickup,nearby_bins,complaint,check_worker_duty,details_house,user_registration,worker_registration

# Register your models here.
# admin.site.register(pickup)
# admin.site.register(nearby_bins)
# admin.site.register(complaint)
# admin.site.register(check_worker_duty)
# admin.site.register(details_house)
# admin.site.register(user_registration)
# admin.site.register(worker_registration)
admin.site.register(UserDetails)
admin.site.register(ManageBins)
admin.site.register(WorkerDetails)
admin.site.register(TrackTruck)
admin.site.register(TrackWorker)
admin.site.register(complaints)
admin.site.register(ManageHouse)
admin.site.register(pickup)