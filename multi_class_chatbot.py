import streamlit as st
import random

st.set_page_config(page_title="Exam-Time Chatbot", page_icon="📚", layout="centered")
st.title("📚 Multi-Class Exam Chatbot (Demo)")

st.write("This is a demo chatbot for Class 10, 11, and 12 students (Maths & Science).")

# Data (exam schedule, notes, questions)
data = {
    "10": {
        "maths": {
            "exam_date": "Class 10 Maths exam: 5 Oct, 10AM–1PM. Chapters: Algebra, Trigonometry.",
            "notes": "Algebra: Factorisation rules, quadratic equations.\nTrigonometry: sin²θ + cos²θ = 1, tanθ = sinθ/cosθ",
            "questions": [
                "Solve: 2x + 3 = 7",
                "Find sin30° + cos60°",
                "What is the probability of getting a head in one coin toss?"
            ]
        },
        "science": {
            "exam_date": "Class 10 Science exam: 7 Oct, 10AM–1PM. Chapters: Life Processes, Electricity.",
            "notes": "Life Processes: Nutrition, Respiration, Excretion.\nElectricity: Ohm's Law, Resistance, Series & Parallel.",
            "questions": [
                "Write the equation of photosynthesis.",
                "State Ohm's Law.",
                "What is the unit of resistance?"
            ]
        }
    },
    "11": {
        "maths": {
            "exam_date": "Class 11 Maths exam: 12 Oct, 10AM–1PM. Chapters: Sets, Relations, Functions.",
            "notes": "Sets: Union, Intersection, Complement.\nFunctions: Domain & Range, Graphs.",
            "questions": [
                "Define a universal set.",
                "What is the domain of f(x) = 1/x?",
                "Find the range of f(x) = x²."
            ]
        },
        "science": {
            "exam_date": "Class 11 Science exam: 14 Oct, 10AM–1PM. Chapters: Thermodynamics, Waves.",
            "notes": "Thermodynamics: Laws, Heat transfer.\nWaves: Types, frequency, wavelength.",
            "questions": [
                "State the 1st Law of Thermodynamics.",
                "Differentiate longitudinal & transverse waves.",
                "Define wavelength."
            ]
        }
    },
    "12": {
        "maths": {
            "exam_date": "Class 12 Maths exam: 18 Oct, 10AM–1PM. Chapters: Calculus, Vectors.",
            "notes": "Integration: ∫x dx = x²/2 + C.\nVectors: Dot & Cross product.",
            "questions": [
                "Find ∫2x dx.",
                "If a=(1,2,3), b=(4,5,6), find a·b.",
                "Differentiate f(x) = x²."
            ]
        },
        "science": {
            "exam_date": "Class 12 Science exam: 20 Oct, 10AM–1PM. Chapters: Modern Physics, Organic Chemistry.",
            "notes": "Modern Physics: Photoelectric effect, Atomic models.\nOrganic Chemistry: Aldehydes, Amines.",
            "questions": [
                "State Einstein’s photoelectric equation.",
                "Write the IUPAC name of CH3CHO.",
                "Define half-life of a radioactive element."
            ]
        }
    }
}

# User inputs
class_choice = st.selectbox("Choose your class:", ["10", "11", "12"])
subject_choice = st.selectbox("Choose subject:", ["maths", "science"])
query = st.selectbox("What do you want?", ["exam_date", "notes", "questions"])

if st.button("Show Answer"):
    result = data[class_choice][subject_choice][query]
    if query == "questions":
        result = random.sample(result, min(3, len(result)))  # 3 random questions
        result = "\n".join([f"{i+1}. {q}" for i, q in enumerate(result)])
    st.success(result)
