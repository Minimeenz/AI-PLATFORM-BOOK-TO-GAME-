"""
manual_glue_code.py
This script represents the ~5% manual Python coding written for the R42 AI Book-to-Game platform.
It bridges AI outputs from Lovable and Rosebud into a functioning interactive experience.
"""

from flask import Flask, request, render_template
import json, datetime

# -------------------------------
# 1. Build Rosebud Prompt from Lovable Analysis
# -------------------------------
def build_rosebud_prompt(book_title, chapters):
    """Format chapter summaries into a clean Rosebud prompt."""
    prompt = f"Create a 3D first-person RPG based on '{book_title}'.\n"
    for i, ch in enumerate(chapters, 1):
        prompt += f"Chapter {i}: {ch['summary']}\n"
    return prompt.strip()


# -------------------------------
# 2. Flask Route to Connect Analysis → Game
# -------------------------------
app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze_book():
    book_title = request.form["title"]
    
    # Placeholder: AI analysis from Lovable (simulated)
    analysis = {"title": book_title, "chapters": [{"summary": "Example chapter summary"}]}
    
    if book_title.lower() == "wizard of oz":
        return render_template("result.html", 
                               analysis=analysis,
                               game_link="/play/oz3d")
    return render_template("result.html", analysis=analysis)


# -------------------------------
# 3. Clean Up NPC Dialogue
# -------------------------------
def clean_npc_dialogue(dialogue_list, max_len=150):
    """Trim AI-generated NPC dialogues to avoid overly long text."""
    return [d[:max_len] + "..." if len(d) > max_len else d for d in dialogue_list]


# -------------------------------
# 4. Event Translator: Text → 3D Game Action
# -------------------------------
event_map = {
    "fight": "start_combat()",
    "meet_npc": "spawn_npc()",
    "find_item": "add_inventory()"
}

def translate_event(event_type):
    """Map high-level AI-generated events into Rosebud-recognized game actions."""
    return event_map.get(event_type, "idle()")


# -------------------------------
# 5. Logging for Debugging
# -------------------------------
def log_ai_output(response, label="lovable"):
    """Save AI responses to JSON logs for debugging and testing."""
    with open(f"logs/{label}_{datetime.date.today()}.json", "a") as f:
        f.write(json.dumps(response, indent=2))
        f.write("\n---\n")


# -------------------------------
# Example usage (for demonstration)
# -------------------------------
if __name__ == "__main__":
    chapters = [{"summary": "Dorothy is swept away to Oz."}, {"summary": "She meets the Scarecrow."}]
    prompt = build_rosebud_prompt("The Wizard of Oz", chapters)
    print("Generated Rosebud Prompt:\n", prompt)

    dialogue = ["Hello, traveler! Welcome to Oz.", "This is a very long AI-generated dialogue that might need trimming to fit the game screen properly."]
    print("\nCleaned Dialogue:", clean_npc_dialogue(dialogue))

    print("\nTranslate Event 'fight':", translate_event("fight"))

    sample_response = {"npc": "Scarecrow", "dialogue": "If I only had a brain..."}
    log_ai_output(sample_response)
    print("\nLogged sample AI response to file.")
