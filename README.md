# BMI Calculator – Flask Web App

## Project Title
BMI Calculator Web App (Flask)

## Overview
This is a simple `BMI` (Body Mass Index) calculator built with Flask. It takes weight, height, and age as input, converts units to metric if needed, calculates BMI using the standard formula, and displays the BMI value along with the corresponding weight category.

## Features
- Input fields for weight, height, and age  
- Support for kg/lb and cm/m/in with automatic unit conversion  
- BMI calculation using the standard formula  
- Categorization as Underweight, Healthy weight, Overweight, or Obese  
- Simple web UI using HTML and CSS  
- Basic validation for non-positive or invalid values  

## Technologies / Tools Used
- Python  
- Flask  
- HTML, CSS  
- Jinja2 templates (via Flask)

## Installation and Running the Project

1. Clone the repository:

 --git clone (your-repo-url)
 --cd (BMI-CALCULATOR)


2. (Optional) Create and activate a virtual environment:
Open py file, open terminal and run this.

--`Windows`
  (venv\Scripts\activate)

--`macOS/Linux` 
  source venv/bin/activate


3. Install dependencies:
pip install -r requirements.txt


4. Run the Flask app:
python bmi_app.py


5. Open your browser and go to:
http://127.0.0.1:5000/


## Instructions for Testing

- Open the home page in your browser.  
- Enter:
- Weight and select unit (kg or pounds).  
- Height and select unit (cm or inches).  
- Age in years.  
- Submit the form.  
- Verify that:
- A BMI value (with two decimal places) is shown.  
- The displayed category matches the BMI range.  
- Error messages appear for empty, negative, or invalid values.

## Screenshots

### Home Page
![Home Page](screenshots/SS1.png)

### Result Page
![Result Page](screenshots/SS2.png)






