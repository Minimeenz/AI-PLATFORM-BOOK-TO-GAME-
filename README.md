# Manual Glue Code (5% Contribution)

This repository contains the **manual Python coding (~5%)** that was integrated into the **R42 AI Book-to-Game Platform** during the Summer 2025 Fellowship.  
The majority of the platform (95%) was developed using **AI-driven coding via Lovable and Rosebud AI**, while this script demonstrates the small but essential custom contributions.
Herre is the link to the AI platform: [
](https://preview--book-to-game-verse-65.lovable.app/)---

## 📂 File: `manual_glue_code.py`

This script acts as the glue between AI outputs (Lovable analysis and Rosebud game generation) and the working platform.

### 1. Rosebud Prompt Builder
```python
def build_rosebud_prompt(book_title, chapters):
    ...
```
Takes Lovable’s raw chapter summaries and formats them into a clean, structured prompt for Rosebud.  
This ensures consistency when generating games for any book.

---

### 2. Flask Route: Analysis → Game Link
```python
@app.route("/analyze", methods=["POST"])
def analyze_book():
    ...
```
A lightweight web route that connects user input (*Analyze My Book*) to a result page.  
If the book is *The Wizard of Oz*, it provides a special **“Play in 3D”** link.

---

### 3. NPC Dialogue Cleaner
```python
def clean_npc_dialogue(dialogue_list, max_len=150):
    ...
```
AI often produces very long dialogues. This function trims them for usability inside the game.

---

### 4. Event Translator
```python
def translate_event(event_type):
    ...
```
Maps AI-generated story events (like *fight*, *meet_npc*, *find_item*) into recognized Rosebud actions (*start_combat()*, *spawn_npc()*, etc.).

---

### 5. Logging for Debugging
```python
def log_ai_output(response, label="lovable"):
    ...
```
Saves AI responses as JSON logs. This allowed the team to review, debug, and improve AI outputs during testing.

---

## 🧩 Example Usage
When run directly, the script demonstrates:
- Generating a Rosebud prompt for *The Wizard of Oz*
- Cleaning dialogue samples
- Translating a sample game event
- Logging an AI output

---

## ✨ Summary
This script illustrates the **5% manual coding contribution** that bridged AI-generated components into a working product.  
It reflects practical engineering: formatting, integration, event handling, and debugging — all critical for ensuring the platform functioned smoothly.
