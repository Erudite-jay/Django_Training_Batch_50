from .models import Contact
from django.http import JsonResponse
from django.shortcuts import render
from .forms import ContactForm
# Create your views here.


def contact_view(request):
    if request.method == "POST":
        try:
            form = ContactForm(request.POST, request.FILES)  # -> name and file
            if form.is_valid():
                form.save()
                
                # file_upload = Contact(name=form.cleaned_data["name"], file=form.cleaned_data["file"])
                # file_upload.save()
                return JsonResponse(
                    {
                        "success": True,
                    }, status=201
                )
        except Exception as e:
            return JsonResponse(
                {
                    "error": str(e),
                }, status=500
            )
    else:
        form = ContactForm()

    return render(request, "Forms_app/contact.html", {"form": form})
