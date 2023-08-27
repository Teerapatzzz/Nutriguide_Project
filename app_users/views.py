from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from app_users.forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode ,urlsafe_base64_decode
from django.utils.encoding import force_bytes


from .forms import UserProfileForm, ExtendedProfileForm
from .models import CustomUser
from .utils.activation_token_generator import activation_token_generator
# Create your views here.
def register(request: HttpRequest):

    #⁡⁢⁢⁢POST⁡
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            #Register User
            user: CustomUser = form.save(commit=False)
            user.save()
            user.is_active = False
            
            #login(request, user)
            #Build email body html
            context = {
                "potocol": request.scheme,
                "host": request.get_host,
                "uidb64": urlsafe_base64_encode(force_bytes(user.id)),
                "token": activation_token_generator.make_token(user)
            }
            email_body = render_to_string("app_users/activate_email.html",context)
            #send Email

            email = EmailMessage(
                to=[user.email], 
                subject="Activate account หน่อยครับ",
                body=email_body
                )
            email.send()
            #Redirect to thank you
            return HttpResponseRedirect(reverse('register_thankyou'))
    else:
        form = RegisterForm()

    #⁡⁣⁢⁢GET⁡
    form = RegisterForm()
    context = {'form': form}
    return render(request,'app_users/register.html',context)

def register_thankyou(request: HttpRequest):
    return render(request,"app_users/register_thankyou.html")


def activate(request:HttpRequest, uidb64: str,token: str):
    title = "Activate account เรียบร้อย"
    description = "คุณสามารถเข้าสู่ระบบได้เลย"
    
    #Decode user id
    id = urlsafe_base64_decode(uidb64).decode()

    try: 
        user: CustomUser = CustomUser.objects.get(id=id)
        if not activation_token_generator.check_token(user, token):
            raise Exception("Check token false")
        user.is_active = True
        user.save()
    except:
        print("Activate ไม่ผ่าน")
        title = "Activate account ไม่ผ่าน"
        description = "ลิงค์ถูกใช้ไปแล้ว หรือ หมดอายุ"

    context = {'title': title,'description':description }
    return render(request,"app_users/activate.html", context)


@login_required
def dashboard(request: HttpRequest ):
    return render(request,'app_users/dashboard.html')


@login_required
def profile(request: HttpRequest):
    user = request.user

    # POST
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user)
        is_new_profile = False
        try:
            # Will be updated profile
            extended_form = ExtendedProfileForm(request.POST, instance=user.profile)
        except:
            # Will be created profile
            is_new_profile = True
            extended_form = ExtendedProfileForm(request.POST)

        if form.is_valid() and extended_form.is_valid():
            form.save()
            if is_new_profile:
                # Create profile
                profile = extended_form.save(commit=False)
                profile.user = user
                profile.save()
            else:
                # Update profile
                extended_form.save()
            response = HttpResponseRedirect(reverse("profile"))
            response.set_cookie("is_saved", "1")
            return response
    else:
        form = UserProfileForm(instance=user)
        try:
            extended_form = ExtendedProfileForm(instance=user.profile)
        except:
            extended_form = ExtendedProfileForm()

    # GET
    is_saved = request.COOKIES.get("is_saved") == "1"
    flash_message = "บันทึกเรียบร้อย" if is_saved else None
    context = {
        "form": form,
        "extend_form": extended_form,
        "flash_message": flash_message,
    }
    response = render(request, "app_users/profile.html", context)
    if is_saved:
        response.delete_cookie("is_saved")
    return response