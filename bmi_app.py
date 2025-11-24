from flask import Flask, render_template, request, redirect, url_for
# We import the necessary tools from the Flask library to build our web app.


#SETUP OF THE APPLICATION


# Initialize the Flask application. This is our main web app object.
app = Flask(__name__)


#BMI CALCULATION LOGIC



@app.route("/", methods=["GET", "POST"])
def calculate_bmi():
    
    final_result_message = ""

    
    if request.method == "POST":
        
        #We convert inputs to floating-point numbers for calculation.
        input_weight = float(request.form["Weight"])
        input_height = float(request.form["Height"])
        weight_unit_selection = request.form["unitWeight"]
        height_unit_selection = request.form["unitHeight"]

        #Validation Check
        if input_weight <= 0 or input_height <= 0:
            final_result_message = "Oops! Please enter positive values for weight and height."
        else:
            #Unit Conversion to Standard (kg and meters)

            # Start with the input values, which we will convert if needed.
            weight_in_kg = input_weight
            height_in_meters = input_height

            # Convert weight to Kilograms (kg) if the user chose Pounds
            if weight_unit_selection == "Pounds":
                # 1 Pound ≈ 0.45359237 Kilograms
                weight_in_kg = weight_in_kg * 0.45359237

            # Convert height to Meters (m)
            if height_unit_selection == "Centimetres":
                # 100 Centimeters = 1 Meter
                height_in_meters = height_in_meters / 100.0
            elif height_unit_selection == "Inches":
                # 1 Inch ≈ 0.0254 Meters
                height_in_meters = height_in_meters * 0.0254

            
            # BMI Formula: weight (kg) / height (m)^2
            bmi_value = weight_in_kg / (height_in_meters ** 2)

            #Determine BMI Category
            health_category = ""
            if bmi_value < 18.5:
                health_category = "Underweight"
            elif bmi_value < 25:
                health_category = "Healthy weight"
            elif bmi_value < 30:
                health_category = "Overweight"
            else:
                health_category = "Obese"

            
            # Format the BMI to two decimal places for readability.
            final_result_message = f"Your BMI is {bmi_value:.2f} ({health_category})."

        # After calculating and generating the message, we redirect the user's browser.
        
        return redirect(url_for("calculate_bmi", result=final_result_message))

    #DISPLAY THE PAGE

    # Get the result 
    result_to_display = request.args.get("result", "")


    
    return render_template("index.html", result=result_to_display)


# 4. RUN THE SERVER

if __name__ == "__main__":
    # Start the web server in debug mode).
    app.run(debug=True)

    # I am using simple arithematic formula for calculating BMI. It is the most efficient code and also short and simple, to understand and to explain. I have also used HTML & CSS for styling the layout of tis project.