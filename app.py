import random

def genai_response(user_input):
    user_input_lower = user_input.lower()

    # STUDY / TIMETABLE
    if "study" in user_input_lower or "timetable" in user_input_lower:
        subjects = ["Maths", "Programming", "AI", "Data Science", "English"]
        random.shuffle(subjects)

        return f"""
📚 Generated Study Timetable:

9:00 - 11:00 → {subjects[0]}  
1:00 - 3:00 → {subjects[1]}  
4:00 - 6:00 → {subjects[2]}  
7:00 - 8:00 → Revision  
"""

    # TRIP
    elif "trip" in user_input_lower:
        places = ["Local sightseeing", "Famous attractions", "Shopping", "Food exploration"]
        random.shuffle(places)

        return f"""
🧳 Generated Travel Plan:

Day 1: {places[0]}  
Day 2: {places[1]}  
Day 3: {places[2]}  
"""

    # ASSIGNMENT
    elif "assignment" in user_input_lower:
        topics = ["Introduction", "Key Concepts", "Examples", "Applications", "Conclusion"]
        random.shuffle(topics)

        return f"""
📝 Generated Assignment Content Structure:

- {topics[0]}  
- {topics[1]}  
- {topics[2]}  
- {topics[3]}  
- {topics[4]}  
"""

    # DEFAULT
    else:
        return f"""
Generated Content:

This is a dynamically generated response for: {user_input}
"""
    # -------- Generative AI --------
def genai_response(user_input):
    user_input_lower = user_input.lower()

    

    # STUDY / TIMETABLE
    if "study" in user_input_lower or "timetable" in user_input_lower:
        return """
📚 Generated Study Timetable:

9:00 - 11:00 → Maths  
1:00 - 3:00 → Programming  
6:00 - 8:00 → Revision  
"""

    # TRIP
    elif "trip" in user_input_lower:
        return """
🧳 Generated Travel Plan:

Day 1: Arrival & sightseeing  
Day 2: Main attractions  
Day 3: Return journey  
"""

    # ASSIGNMENT
    elif "assignment" in user_input_lower:
        return """
📝 Generated Assignment Content:

- Introduction to the topic  
- Key concepts and explanation  
- Real-world applications  
- Conclusion  
"""

    # IMAGE
    elif "image" in user_input_lower:
        return """
🖼️ Generated Image Description:

A scenic mountain landscape with a river and sunset sky.
"""

    # AUDIO
    elif "audio" in user_input_lower:
        return """
🎧 Generated Audio Script:

"Hello! This is your personalized assistant helping you stay productive."
"""

    # DEFAULT
    else:
        return f"""
Generated Content:

This is a generated response for: {user_input}
"""


# -------- Agentic AI --------
def search_flights(destination):
    return f"Flights to {destination} found starting at ₹5000"

def search_hotels(destination):
    return f"Hotels in {destination} found starting at ₹2000/night"


def agentic_response(user_input):
    user_input_lower = user_input.lower()

    # -------- TRIP --------
    if "trip" in user_input_lower:
        if "to" in user_input_lower:
            destination = user_input_lower.split("to")[-1].strip().title()
        else:
            destination = "Unknown"

        flights = search_flights(destination)
        hotels = search_hotels(destination)

        return f"""
Goal: {user_input}

Step 1: Destination identified → {destination} ✅
Step 2: {flights} ✈️
Step 3: {hotels} 🏨
Step 4: Create itinerary 📅
Step 5: Travel ready 🎒

Final Status: Trip planned successfully ✅
"""

    # -------- STUDY --------
    elif "study" in user_input_lower or "timetable" in user_input_lower:
        return f"""
Goal: {user_input}

Step 1: Identify subjects 📚
Step 2: Allocate time slots ⏰
Step 3: Create timetable 🗓️
Step 4: Track progress 📊

Final Status: Study routine planned successfully ✅
"""

    # -------- ASSIGNMENT --------
    elif "assignment" in user_input_lower:
        return f"""
Goal: {user_input}

Step 1: Understand assignment topic 📌
Step 2: Research content 🔍
Step 3: Create outline 📝
Step 4: Generate content ✍️
Step 5: Review and finalize ✅

Final Status: Assignment completed successfully 🎯
"""

    # -------- DEFAULT --------
    else:
        return f"""
Goal: {user_input}

Step 1: Analyze task
Step 2: Plan actions
Step 3: Execute steps

Final Status: Task completed
"""


# -------- MAIN --------
if __name__ == "__main__":
    user_input = input("Enter your task: ")

    print("\n🟢 Generative AI Output:\n")
    print(genai_response(user_input))

    print("\n" + "="*50)

    print("\n🔴 Agentic AI Output:\n")
    print(agentic_response(user_input))