# Timeline Visualization

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/timeline-visualization.git
   ```
2. Navigate to the project directory:
   ```
   cd timeline-visualization
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Django development server:
   ```
   python manage.py runserver
   ```
2. Open your web browser and navigate to `http://localhost:8000/`.
3. You will see a timeline visualization and a bar chart.
4. Use the buttons to download the timeline and chart as PDF or JPG files.

## API

The project uses the following APIs:

- [Vis.js Timeline](https://visjs.org/docs/timeline/) for the timeline visualization.
- [Chart.js](https://www.chartjs.org/) for the bar chart.
- [html2canvas](https://html2canvas.hertzen.com/) and [jsPDF](https://parall.ax/products/jspdf) for generating PDF and JPG files.
