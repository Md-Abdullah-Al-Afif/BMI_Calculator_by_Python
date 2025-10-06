# BMI_Calculator_by_Python
A Python-based BMI Calculator with an interactive graphical interface.  
Users can input or adjust their height and weight using sliders to view their BMI in real time, along with a health classification and short message.

---

## 🚀 Features (Functional Requirements)

### 🖥️ User Interface
- User-friendly GUI with labeled fields, buttons, and result display.

### 📥 User Input
- Input height (cm) and weight (kg) manually or through sliders.

### ⚙️ Dynamic Adjustment
- Real-time update of values when sliders are adjusted.

### 👀 Visual Feedback
- Displays a figure image that changes with height adjustment.

### 📊 “View Report” Button
- Generates a BMI report showing:
  1. Calculated BMI (1 decimal precision)
  2. BMI classification:
     - Underweight (≤18.5)
     - Normal (18.5–25)
     - Overweight (25–30)
     - Obese (>30)
  3. A short message for each category.

### ⚠️ Error Handling
- Detects invalid (non-numeric) inputs and shows appropriate error messages.

---

## 🛠️ Requirements
No external libraries required — uses Python’s built-in **tkinter** and **math** modules.

---

## ▶️ Run the Application
```bash
main.py
