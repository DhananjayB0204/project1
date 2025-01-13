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

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Testing

No specific testing instructions are provided in the given code. The project should be tested manually by running the Django development server and verifying the functionality of the timeline visualization, bar chart, and file download features.
