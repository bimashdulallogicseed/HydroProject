from .models import hydrosheet
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
import pandas as pd
from .forms import HydroProjectForm

EXCEL_FILE_PATH = "C:\\Users\\bimas\\OneDrive\\Desktop\\hydropower_1.xlsx"


def hydroproject_list(request):
    df = pd.read_excel(EXCEL_FILE_PATH)
    projects = df.to_dict('records')
    return render(request, 'myapp/hydroproject_list.html', {'projects': projects})

def hydroproject_create(request):
    if request.method == 'POST':
        
        form = HydroProjectForm(request.POST)
        if form.is_valid():
            # hydro_project = hydrosheet(
            #     name=form.cleaned_data['name'],
            #     capacity=form.cleaned_data['capacity'],
            #     location=form.cleaned_data['location']
            # )
            # hydro_project.save()
            form.save_to_excel(EXCEL_FILE_PATH)
            
            return redirect('hydroproject_list')
            
    else:
        form = HydroProjectForm()
    return render(request, 'myapp/hydroproject_form.html', {'form': form})

    
    
def hydroproject_update(request, project_id=None):
    # project_instance = get_object_or_404(hydrosheet, pk=project_id)
    # Load the Excel file
    
    df = pd.read_excel(EXCEL_FILE_PATH)

    if project_id is not None and project_id >= len(df):
        return HttpResponse("Project ID not found", status=404)

    # Initialize form with project data if updating, otherwise an empty form for adding
    if project_id is not None:
        project = df.iloc[project_id].to_dict()
    else:
        project = {}

    if request.method == 'POST':
        form = HydroProjectForm(request.POST)
        if form.is_valid():
            try:
                # project_instance.name = form.cleaned_data['name']
                # project_instance.capacity = form.cleaned_data['capacity']
                # project_instance.location = form.cleaned_data['location']
                # project_instance.save()
                # Save to Excel (handle both add and update within the form)
                form.save_to_excel(EXCEL_FILE_PATH, project_id)
            except ValueError as e:
                return HttpResponse(str(e), status=400)
            return redirect('hydroproject_list')
    else:
        form = HydroProjectForm(initial=project)
    return render(request, 'myapp/hydroproject_form.html', {'form': form})


  
def hydroproject_delete(request, project_id):
    # project_instance = get_object_or_404(hydrosheet, pk=project_id)
    if request.method == 'POST':
        # project_instance.delete()
        df = pd.read_excel(EXCEL_FILE_PATH)
        df = df.drop(project_id)
        df.to_excel(EXCEL_FILE_PATH, index=False)
        return redirect('hydroproject_list')
    return render(request, 'myapp/hydroproject_confirm_delete.html', {'project_id': project_id})



# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
# import pandas as pd
# from .models import HydroProject
# from .forms import HydroProjectForm

# EXCEL_FILE_PATH = "C:\\Users\\bimas\\OneDrive\\Desktop\\hydropower_1.xlsx"

# def hydroproject_list(request):
#     df = pd.read_excel(EXCEL_FILE_PATH)
#     projects = df.to_dict('records')
#     return render(request, 'myapp/hydroproject_list.html', {'projects': projects})

# def hydroproject_create(request):
#     if request.method == 'POST':
#         form = HydroProjectForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form.save_to_excel(EXCEL_FILE_PATH)
#             return redirect('hydroproject_list')
#     else:
#         form = HydroProjectForm()
#     return render(request, 'myapp/hydroproject_form.html', {'form': form})

# def hydroproject_update(request, project_id=None):
#     if project_id is not None:
#         project_instance = get_object_or_404(HydroProject, pk=project_id)
#         df = pd.read_excel(EXCEL_FILE_PATH)
#         if project_id >= len(df):
#             return HttpResponse("Project ID not found", status=404)
#         project = df.iloc[project_id].to_dict()
#     else:
#         project_instance = None
#         project = {}

#     if request.method == 'POST':
#         form = HydroProjectForm(request.POST, instance=project_instance)
#         if form.is_valid():
#             form.save()
#             form.save_to_excel(EXCEL_FILE_PATH, project_id)
#             return redirect('hydroproject_list')
#     else:
#         form = HydroProjectForm(initial=project, instance=project_instance)
#     return render(request, 'myapp/hydroproject_form.html', {'form': form})

# def hydroproject_delete(request, project_id):
#     project_instance = get_object_or_404(HydroProject, pk=project_id)
#     if request.method == 'POST':
#         project_instance.delete()
#         df = pd.read_excel(EXCEL_FILE_PATH)
#         df = df.drop(project_id).reset_index(drop=True)
#         df.to_excel(EXCEL_FILE_PATH, index=False)
#         return redirect('hydroproject_list')
#     return render(request, 'myapp/hydroproject_confirm_delete.html', {'project_id': project_id})
