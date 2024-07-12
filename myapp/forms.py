

from django import forms
import pandas as pd

class HydroProjectForm(forms.Form):
    name = forms.CharField(max_length=100)
    capacity = forms.FloatField()
    location = forms.CharField(max_length=100)

    def save_to_excel(self, excel_file_path, project_id=None):
        df = pd.read_excel(excel_file_path)
        data = {
            'Name': self.cleaned_data['name'],
            'Capacity': self.cleaned_data['capacity'],
            'Location': self.cleaned_data['location'],
        }

        print("Data dictionary keys:", data.keys())
        print("DataFrame columns:", df.columns)

        if project_id is not None:
            # Update the specific row with the new data
            df.iloc[project_id] = pd.Series(data)
        else:
            # Add a new project
            new_df = pd.DataFrame([data])
            df = pd.concat([df, new_df], ignore_index=True)
        
        # Ensure only the necessary columns are saved
        df = df[['Name', 'Capacity', 'Location']]
        df.to_excel(excel_file_path, index=False)


# from django import forms
# from .models import HydroProject
# import pandas as pd

# class HydroProjectForm(forms.ModelForm):
#     class Meta:
#         model = HydroProject
#         fields = ['name', 'capacity', 'location']

#     def save_to_excel(self, excel_file_path, project_id=None):
#         df = pd.read_excel(excel_file_path)
#         data = {
#             'Name': self.cleaned_data['name'],
#             'Capacity': self.cleaned_data['capacity'],
#             'Location': self.cleaned_data['location'],
#         }

#         if project_id is not None:
#             df.iloc[project_id] = pd.Series(data)
#         else:
#             new_df = pd.DataFrame([data])
#             df = pd.concat([df, new_df], ignore_index=True)
        
#         df = df[['Name', 'Capacity', 'Location']]
#         df.to_excel(excel_file_path, index=False)
