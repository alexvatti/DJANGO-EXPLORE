from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def bmi_calculator(request):
    bmi = None  # Default value for BMI
    message = ""

    if request.method == 'POST':
        weight = float(request.POST.get('weight', 0))
        height = float(request.POST.get('height', 0))
        if height > 0:
            bmi = round(weight / (height ** 2), 2)
            if bmi < 18.5:
                message = "Underweight"
            elif 18.5 <= bmi <= 24.9:
                message = "Normal weight"
            elif 25 <= bmi <= 29.9:
                message = "Overweight"
            else:
                message = "Obese"

    return render(request, 'bmi_calculator.html', {'bmi': bmi, 'message': message})
from datetime import datetime

def age_calculator(request):
    age = None
    error = None

    if request.method == 'POST':
        dob = request.POST.get('dob')  # Get Date of Birth
        today = request.POST.get('today')  # Get Today's Date

        try:
            # Convert string inputs to datetime objects
            dob_date = datetime.strptime(dob, '%Y-%m-%d')
            today_date = datetime.strptime(today, '%Y-%m-%d')

            if today_date < dob_date:
                error = "Today's date cannot be earlier than your date of birth."
            else:
                # Calculate age
                age = today_date.year - dob_date.year
                if today_date.month < dob_date.month or (today_date.month == dob_date.month and today_date.day < dob_date.day):
                    age -= 1  # Adjust if the birthday hasn't occurred yet this year
        except ValueError:
            error = "Invalid date format. Please try again."

    return render(request, 'age_calculator.html', {'age': age, 'error': error})