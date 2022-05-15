from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from file_summary import *
from . forms import PSummaryForm1, PSummaryForm2, FileForm, DisplayFileForm
from . models import *
from sumyUrl import *
from summary_algo import *
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_sameorigin
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import re
import docx

@login_required
def urlsummarizer(request):
    if 'url' in request.POST:
        url = request.POST['url'].strip()
        length = request.POST['length'].strip()
        if length == "":
            length=10
        else:
            length = int(length)
        # print(type(length))
        if length < 0:
            length = 10
        # print("length ")
        # print(length)
        summary = summarize(url, length)
        # summary = "hello"
        print("summary returned "+summary)
        return render(request, "url_summarizer.html", {"summary":summary, "url":url, "length":length})

    return render(request, "url_summarizer.html")

@login_required
def urlshowcase(request):
    request.session.setdefault('how_many_visits', 0)
    return render(request, "url_showcase.html")

@login_required
def filemailtest(request):
    return render(request, "file_summarizer_op0.html")

@login_required
def filesummarizer(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            # print("inside form is valid")
            # print("data inside file is ")
            # newfile = File(uploaded_file = request.FILES['uploaded_file'])
            # newfile.save()
            length = request.POST['length'].strip()
            if length == "":
                length=1
            else:
                length = int(length)
            # print(type(length))
            if length < 0:
                length = 1

            # paragraph = form1.cleaned_data['paragraph'].strip()

            # READ FILE FROM POSTED FORM
            file_uploaded = request.FILES['uploaded_file']
            #
            file_ext = re.search(r"\.([^.]+)$", str(file_uploaded)).group(1)

            if file_ext=="pdf" or file_ext=="PDF":
                with fitz.open(stream=file_uploaded.read(), filetype="application/pdf") as doc:
                    text = ""
                    for page in doc:
                        text += page.get_text()
                decoded_file_data=text
            elif file_ext=="docx" or file_ext=="DOCX":
                doc = docx.Document(file_uploaded)
                text = ""
                for para in doc.paragraphs:
                    if len(para.text)==0:
                        pass
                    else:
                        text+=para.text
                print("docx text")
                print(text)
                decoded_file_data=text
            else:
                fs = FileSystemStorage()
                # filename = fs.save(file_uploaded.name, file_uploaded)
                uploaded_file_path = fs.path(file_uploaded.name)
                # # absolute file path /home/akash/Projects/authsystem/summarizer/uploads/file_to_summarize_kcBM8GZ.txt
                print('absolute file path', uploaded_file_path)

                decoded_file_data = request.FILES['uploaded_file'].read().decode("utf-8")
                print("decoded file data")
                print(decoded_file_data)

            filesummary = file_summary(decoded_file_data, length)

            print("summarized file data")
            print(filesummary)
            # file_contents
            # summary_of_file_contents
            # file_url =
            # file_contents=decoded_file_data, summary_of_file_contents=filesummary, uploaded_file=""
            fileModel = DisplayFile(file_contents=decoded_file_data, summary_of_file_contents=filesummary)
            form = DisplayFileForm(instance=fileModel)
            # uploaded_file = models.FileField(upload_to="media", null=True, blank=True)
            # file_contents = models.TextField(max_length=10000, default="", blank=True)
            # summary_of_file_contents = models.TextField(max_length=10000, default="", blank=True)


            # form = DisplayFileForm(file_contents=decoded_file_data, file_url=uploaded_file_path,summary_of_file_contents=filesummary)
            # form = DisplayFileForm(file_contents="decoded_file_data", file_url="https://stackoverflow.com/questions/6418072/accessing-media-files-in-django",summary_of_file_contents="filesummary")
            return render(request, "file_summarizer_op0.html", {
                "file_contents": decoded_file_data,
                "file_summary": filesummary,
                "length": length,
            })
    else:
        form = FileForm()

    return render(request, "file_summarizer_ip.html", {
        "form": form
    })

@xframe_options_sameorigin
@login_required
def paragraph(request):
    model1 = PSummary1(id=1, paragraph="", length="", summary="")
    form1 = PSummaryForm1(instance=model1)
    model2 = PSummary2(id=2, paragraph="", length="", summary="")
    form2 = PSummaryForm2(instance=model2)
    paragraph_summary1 = ""
    paragraph_summary2 = ""
    cookie = Cookie.objects.get(id=1)
    print(cookie)
    print("form1_already_submitted "+str(cookie.f1_submitted))
    print("form2_already_submitted "+str(cookie.f2_submitted))

    f1_submitted = cookie.f1_submitted
    f2_submitted = cookie.f2_submitted

    # if both forms are submitted then delete the data and set cookies as false
    if f1_submitted and f2_submitted:
        PSummary1.objects.filter(id=1).delete()
        PSummary2.objects.filter(id=2).delete()

        Cookie.objects.filter(id=1).update(f1_submitted=False, f2_submitted=False)
        # temp_cookie = Cookie(id=1, f1_submitted=False, f2_submitted=False)
        # temp_cookie.save()

    # return render(request, 'paragraph.html', {'form1': form1, 'form2': form2 })
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # form1 = PSummaryForm1(request.POST)
        # form2 = PSummaryForm2()
        if request.POST.get("form_type") == 'formOne':
            print("sumiteed form1")
            # create a form instance and populate it with data from the request:
            form1 = PSummaryForm1(request.POST)
            form2 = PSummaryForm2()

            print(form1.errors)

            if form1.is_valid():
                # process the data in form.cleaned_data as required
                paragraph = form1.cleaned_data['paragraph'].strip()
                if type(form1.cleaned_data['length']).__name__ == "NoneType":
                    length=1
                else:
                    length = form1.cleaned_data['length']
                # print(type(form1.cleaned_data['length']))

                # paragraph_summary1 = retrieve_input(paragraph, length)
                paragraph_summary1 = generate_summary(str(paragraph), length)
                print("@@@@@@@@@@@@@@@@@@@SUMMARY@@@@@@@@@@@@@@@@@@@")
                print(paragraph_summary1)
                print("@@@@@@@@@@@@@@@@@@@SUMMARY@@@@@@@@@@@@@@@@@@@")

                # paragraph_summary1 = "summary of "+paragraph

                # if there is data already in table then retrive and delete
                PSummary1.objects.filter(id=1).delete()
                form = PSummary1(id=1, paragraph=paragraph, length=length, summary=paragraph_summary1)
                form.save()
                data_of_model1 = PSummary1.objects.get(id=1)
                form1 = PSummaryForm1(instance=data_of_model1)

                # set form1 cookie true
                Cookie.objects.filter(id=1).update(f1_submitted=True, f2_submitted=f2_submitted)
                # Cookie.objects.filter(id=1).delete()
                # temp_cookie = Cookie(id=1, f1_submitted=True, f2_submitted=f2_submitted)
                # temp_cookie.save()

                print("line 91 "+str(f1_submitted)+str(f2_submitted))

                cookie = Cookie.objects.get(id=1)
                # check if form2 has data already sumitted and retrieve if there is any
                if cookie.f2_submitted:
                    try:
                        data_of_model2 = PSummary2.objects.get(id=2)
                        print("form2 already submitted")
                        # messages.success(request, "form2 already submitted")
                    except PSummary2.DoesNotExist:
                        print("EXCEPT form 2 no data")
                        data_of_model2 = None
                    form2 = PSummaryForm2(instance=data_of_model2)
                else:
                    form2 = PSummaryForm2()


                # return render(request, "paragraph.html", {'paragraph_summary1':paragraph_summary1, 'form1': form1, 'form2': form2})
                # return render(request, 'paragraph.html')
        elif request.POST.get("form_type") == 'formTwo':
            print("sumiteed form2")
            # create a form instance and populate it with data from the request:
            form2 = PSummaryForm2(request.POST)
            form1 = PSummaryForm1()
            print(form2.errors)

            if form2.is_valid():
                # process the data in form.cleaned_data as required
                paragraph = form2.cleaned_data['paragraph'].strip()
                if type(form2.cleaned_data['length']).__name__ == "NoneType":
                    length=1
                else:
                    length = form2.cleaned_data['length']
                paragraph_summary2 = generate_summary(str(paragraph), length)
                # paragraph_summary2 = "summary of "+paragraph
                PSummary2.objects.filter(id=2).delete()
                form = PSummary2(id=2, paragraph=paragraph, length=length, summary=paragraph_summary2)
                form.save()
                data_of_model2 = PSummary2.objects.get(id=2)
                form2 = PSummaryForm2(instance=data_of_model2)

                # set form1 cookie true
                Cookie.objects.filter(id=1).update(f1_submitted=f1_submitted, f2_submitted=True)
                # Cookie.objects.filter(id=1).delete()
                # temp_cookie = Cookie(id=1, f1_submitted=f1_submitted, f2_submitted=True)
                # temp_cookie.save()

                print("line 136 "+str(f1_submitted)+str(f2_submitted))

                cookie = Cookie.objects.get(id=1)

                # check if form1 has data already sumitted and retrieve if there is any
                if cookie.f1_submitted:
                    try:
                        data_of_model1 = PSummary1.objects.get(id=1)
                        print("form1 already submitted")
                        # messages.success(request, "form1 already submitted")
                    except PSummary1.DoesNotExist:
                        print("EXCEPT form 1 no data")
                        data_of_model1 = None
                    form1 = PSummaryForm1(instance=data_of_model1)
                else:
                    form1 = PSummaryForm1()


                # return render(request, "paragraph.html", {'paragraph_summary2':paragraph_summary2, 'form1': form1, 'form2': form2})

    return render(request, 'paragraph.html', {'form1': form1, 'form2': form2})
