from threading import local
from django.shortcuts import render,redirect
from django.views import View
from django.core.paginator import Paginator
from .forms import *

# Create your views here.
class Contact_BookView(View):
    render_template = 'index.html'
    contact_modelClass = Contact_book

    def get(self,request):
        contact_data = self.contact_modelClass.objects.all()
        data = Paginator(contact_data,10).get_page(request.GET.get('page'))
        return render(request,self.render_template,locals())

class Add_ContactView(View):
    render_template = 'add_contact.html'
    contact_formclass = Add_contactForm
    redirect_url = 'contact_book'

    def get(self,request):
        form = self.contact_formclass
        return render(request,self.render_template,locals())

    def post(self,request):
        form  = self.contact_formclass(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.redirect_url)
        return render(request,self.render_template)

class Edit_ContactView(View):
    render_template = 'edit_contact.html'
    contact_formclass = Add_contactForm
    redirect_url = 'contact_book'

    def get(self,request,**kwargs):
        contact_id = kwargs.get('contact_id')
        form = self.contact_formclass(initial={
            'name' : Contact_book.objects.filter(id=contact_id).first().name,
            'phone' : Contact_book.objects.filter(id=contact_id).first().phone
        })
        return render(request,self.render_template,locals())

    def post(self,request,**kwargs):
        contact_id = kwargs.get('contact_id')
        form  = self.contact_formclass(request.POST,instance=Contact_book.objects.get(id=contact_id))
        if form.is_valid():
            form.save()
            return redirect(self.redirect_url)
        return render(request,self.render_template)

class Delete_ContactView(View):
    redirect_url = 'contact_book'

    def post(self,request,**kwargs):
        contact_id = request.POST.get('contact_id',None)
        contact_instance = Contact_book.objects.filter(id=contact_id)
        if contact_instance.exists():
            contact_instance.delete()
            return redirect(self.redirect_url)
        return render(request,self.render_template,locals())

class View_ContactView(View):
    render_template = 'view_contact.html'

    def get(self,request,**kwargs):
        contact_id = kwargs.get('contact_id',None)
        contact_instance = Contact_book.objects.filter(id=contact_id)
        print(contact_instance,"dfdf")
        return render(request,self.render_template,locals())

    
        