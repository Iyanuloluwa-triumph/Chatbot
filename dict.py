import json

chatbot_dict = {
    "AC machines": {
        "longdef": "AC machines are electrical devices that operate using alternating current (AC). They encompass both motors, which convert electrical energy into mechanical energy, and generators, which convert mechanical energy into AC electrical energy.",
        "shortdef": "An AC is an electric motor that converts alternating current into mechanical power"
    },
    "Transformers": {
        "longdef": "transformer, device that transfers electric energy from one alternating-current circuit to one or more other circuits, either increasing (stepping up) or reducing (stepping down) the voltage",
        "shortdef": "an apparatus for reducing or increasing the voltage of an alternating current."
    }
}

pydict = json.dumps(chatbot_dict, indent=4)



fake_NLP = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! What do you want to learn or ask?",
        "how are you": "I'm just code, but I'm running perfectly!",
        "your name": "I'm StudyPal, your AI-powered study companion.",
        "what can you do": "I can help you study, explain engineering terms, fetch weather data, and more!",
        "help": "Try typing things like '/explain transformer' or 'add task at 8pm'",
        "bye": "Goodbye! Stay focused and keep learning.",
        "thank you": "You're welcome! 😊",
        "thanks": "No problem!",
        "exam": "Do you have an upcoming exam? I can help you prepare!",
        "fluid mechanics": "Need help with Fluid Mechanics? Use /explain fluid mechanics or /ask fluid mechanics",
        "weather": "Use '/weather [city]' to get current weather updates.",
        "who made you": "I was created by a brilliant learner on a mission to master AI/ML!",
        "study": "Stay consistent. Little by little, a little becomes a lot.",
        "motivate me": "You’re not behind — you’re building. Keep going!",
        "ac machine": "An AC machine is an electric device that uses alternating current to operate.",
        "transformer": "A transformer is a device that transfers electrical energy between two or more circuits."
  }

fallback_responses = {
    "study": {
        "responses": [
            "Keep going, future you is counting on this.",
            "Books may be heavy, but ignorance is heavier.",
            "Study hard now, so life gets easier later.",
            "Every hour of study is a brick in your empire.",
            "You're not tired—you’re growing.",
            "Focus! The world needs your brilliance.",
            "Discipline creates freedom.",
            "One more page, one step closer.",
            "Learning is your rebellion against mediocrity.",
            "This effort won’t go to waste.",
            "No one remembers easy victories—earn yours.",
            "Your future self will brag about this grind.",
            "Read now. Flex later.",
            "Smart work beats hard luck.",
            "You’re building a weapon—your mind.",
            "Study is fuel for your dream.",
            "Nobody said it’d be easy, just worth it.",
            "Study while they sleep. Live how they dream.",
            "Every great person once sat just like this—learning.",
            "Power comes from understanding."
        ]
    },
    "wisdom": {
        "responses": [
            "Wisdom is applied knowledge.",
            "Listen more than you speak—that’s where wisdom hides.",
            "The wise admit they know little.",
            "Pain is a great teacher. So is reflection.",
            "Read books. Avoid mistakes.",
            "Seek truth, not applause.",
            "You grow wise by learning from others’ scars.",
            "Wisdom listens before it answers.",
            "Knowledge speaks. Wisdom whispers.",
            "Silence is sometimes the loudest wisdom."
        ]
    },
    "machine": {
        "responses": [
            "Machines follow logic. You define it.",
            "You control the machine—code it wisely.",
            "Machines wait. Humans create.",
            "The future is built on machines. You’re early.",
            "Machines are only as smart as their makers.",
            "Behind every machine is a mind.",
            "Code is power—machines obey it.",
            "Teach machines, shape the world.",
            "Machines are fast, but heartless. Combine both.",
            "Even AI was once just lines of code."
        ]
    },
    "motivation": {
        "responses": [
            "You have what it takes. You just forgot.",
            "Get up and make it happen.",
            "You didn’t come this far to only come this far.",
            "Progress, not perfection.",
            "You're one decision away from a new path.",
            "The grind pays in silence. Results speak later.",
            "No one is coming—be your own hero.",
            "Fall seven times, stand up eight.",
            "Dreams don't work unless you do.",
            "Be stronger than your excuses."
        ]
    },
    "ai": {
        "responses": [
            "AI is not the future—it’s the present.",
            "You’re not learning code, you’re shaping the future.",
            "Understanding AI means understanding humanity.",
            "AI will obey. You must decide wisely.",
            "Train models. Train minds.",
            "With great data comes great responsibility.",
            "AI is what you make it.",
            "Make AI solve Africa’s problems—not mimic the West.",
            "AI isn’t just code, it’s civilization redefined.",
            "Only those who understand AI will lead tomorrow."
        ]
    },
    "focus": {
        "responses": [
            "Eliminate distractions. Lock in.",
            "Focus is your secret weapon.",
            "Multitasking is a lie. Go deep.",
            "Cut the noise. Tune into your mission.",
            "Every minute focused is fuel.",
            "Stay locked in—momentum is real.",
            "Attention is the new currency.",
            "You’re not tired. You’re unfocused.",
            "Do the hard thing first. Then win.",
            "Laser focus breaks limits."
        ]
    },
    "coding": {
        "responses": [
            "Bug? Good. Learn from it.",
            "Code now. Debug later.",
            "Every programmer once Googled 'how to print in Python'.",
            "Keep building—even errors teach.",
            "Code today. Change the world tomorrow.",
            "You write the logic. Machines obey.",
            "There’s elegance in every function.",
            "Programming isn’t typing—it’s thinking.",
            "Your future self will thank this commit.",
            "Error means progress. Keep going."
        ]
    },
    "failure": {
        "responses": [
            "Failure is not the end—it's feedback.",
            "Every success is built on failures.",
            "Fail forward. Fall with direction.",
            "Learn fast. Fail faster.",
            "The road to mastery is paved with errors.",
            "Don’t fear failure—fear regret.",
            "Each L is a lesson, not a loss.",
            "Fail today, succeed forever.",
            "Even champions miss.",
            "Fall. Reflect. Rise."
        ]
    },
    "discipline": {
        "responses": [
            "Discipline is choosing what you want most.",
            "You won’t always feel like it—do it anyway.",
            "Routine beats talent.",
            "Discipline makes hard things look easy.",
            "Every great has discipline. Not motivation.",
            "Set the alarm. Ignore the snooze.",
            "Control yourself, master everything.",
            "Discipline now. Freedom later.",
            "Habits shape destiny.",
            "You either suffer the pain of discipline or regret."
        ]
    },
    "purpose": {
        "responses": [
            "Find your 'why'. Everything else follows.",
            "Purpose fuels persistence.",
            "Without purpose, effort is scattered.",
            "You were born for something big.",
            "Don’t chase approval—chase purpose.",
            "Purpose turns pain into power.",
            "You exist for more than survival.",
            "Work for a cause, not applause.",
            "Purpose wakes you up early.",
            "If it doesn’t align with purpose, say no."
        ]
    }
}
