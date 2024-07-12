import pandas as pd
from sqlalchemy import create_engine
from django.core.management.base import BaseCommand
from myapp.models import hydrosheet  # Adjust as per your app structure

class Command(BaseCommand):
    help = 'Import data from Excel into MySQL database using Django models'

    def handle(self, *args, **kwargs):
        excel_file_path = 'C:\\Users\\bimas\\OneDrive\\Desktop\\hydropower_1.xlsx'

        # Load Excel file into Pandas DataFrame
        wb = pd.read_excel(excel_file_path, sheet_name=None)

        # MySQL connection string
        mysql_conn_str = 'mysql+mysqlconnector://bimash:Bimash123@localhost/hydro'

        # Create SQLAlchemy engine
        engine = create_engine(mysql_conn_str)

        for sheet_name, df in wb.items():
            # Save each sheet as a table in MySQL
            df.to_sql(sheet_name.lower(), con=engine, index=False, if_exists='replace')

            # Create or update HydroProject objects based on the sheet data
            for index, row in df.iterrows():
                try:
                    hydro_project, created = hydrosheet.objects.update_or_create(
                        name=row['Name'],
                        defaults={
                            'capacity': row['Capacity'],
                            'location': row['Location']
                        }
                    )
                except Exception as e:
                    print(f"Error processing row {index}: {e}")

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
