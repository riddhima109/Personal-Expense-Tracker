# Importing the required libraries
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Project, Category, Expense
from django.views.generic import CreateView
from django.utils.text import slugify
from .forms import ExpenseForm
import json

#------------------------ Views ------------------------#

# View for the project list page
# It will return the list of projects
def project_list(request):
    
    # Getting the list of projects
    project_list = Project.objects.all()
    
    # Returning the project list page
    return render(request,'budget/project-list.html',{'project_list':project_list})

# View for the project detail page
# It will return the details of the project and the list of expenses
def project_detail(request, project_slug):
    
    # Getting the project object
    project = get_object_or_404(Project,slug=project_slug)
    
    # Checking the request method
    # If the request method is GET, then it will return the project detail page
    if request.method == 'GET':
        category_list = Category.objects.filter(project=project)
        return render(request,'budget/project-detail.html',{'project':project, 'expense_list': project.expenses.all(), 'category_list':category_list})
    
    # If the request method is POST, then it will create a new expense
    elif request.method == 'POST':
        # Getting the form data and checking if it is valid
        form = ExpenseForm(request.POST)
        if form.is_valid():
            
            # Getting the form data if it is valid
            title = form.cleaned_data['title']
            amount = form.cleaned_data['amount']
            category_name = form.cleaned_data['category']
            category= get_object_or_404(Category, project = project, name= category_name)
            
            # Creating the expense object and saving it
            Expense.objects.create(
                project=project,
                title=title,
                amount=amount,
                category=category
            ).save()
            
    # If the request method is DELETE, then it will delete the expense
    elif request.method == 'DELETE':
        
        # Getting the expense id from the request body and deleting the expense
        id = json.loads(request.body)['id']
        expense = get_object_or_404(Expense,id =id)
        expense.delete()
        return HttpResponse('')
    
    # Redirecting to the project detail page
    return HttpResponseRedirect(project_slug)

# View for the add project page
# It will create a new project
class ProjectCreateView(CreateView):
    
    # Defining the model, template and fields
    model = Project
    template_name = 'budget/add-project.html'
    fields = {'name','budget'}
    
    # Defining the form_valid method to create the categories
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        categories = self.request.POST['categoriesString'].split(',')
        
        # Creating the categories and saving them
        for category in categories:
            Category.objects.create(
                project = Project.objects.get(id=self.object.id),
                name = category
            ).save()
        return HttpResponseRedirect(self.get_success_url())
    
    # Defining the get_success_url method to redirect to the project detail page
    def get_success_url(self):
        return slugify(self.request.POST['name'])