from django.shortcuts import render
import pandas as pd
import os
import json

def home(request):
    return render(request, 'home.html')

def timeline_view(request):
    # Construct the full path to the CSV file
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'timeline_data.csv')
    df = pd.read_csv(csv_path)
    
    # Replace NaN values with empty strings
    df = df.fillna('')

    # Extract data for the chart
    categories = df['content'].tolist()
    values = [5, 7, 4, 10, 8, 6, 9]  # Dummy data, replace with actual values from your CSV file

    events = df.to_dict('records')
    options = {
        'start': '2023-01-01',
        'end': '2023-12-31',
        'editable': True
    }

    # Convert options to JSON
    options_json = json.dumps(options)
    
    return render(request, 'timeline_template.html', {
        'categories': categories,
        'values': values,
        'events': events,
        'options': options_json
    })
