"""VELOCITY LONGFORM - 16:9 chapter lesson, brand and motion constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
FPS = 30

TARGET_CHAPTERS = 8
PHRASES_PER_CHAPTER = 7
TARGET_PHRASES = TARGET_CHAPTERS * PHRASES_PER_CHAPTER

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY HUNGARIAN"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "HUNGARIAN"
HANDLE = "@velocityhungarian"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {'code': 'hu',
 'name': 'Hungarian',
 'native_name': 'Magyar',
 'history_key': 'hungarian',
 'english_voice': 'en-US-AvaNeural',
 'english_fallback_voice': 'en-US-GuyNeural',
 'native_voice': 'hu-HU-TamasNeural',
 'native_fallback_voice': 'hu-HU-NoemiNeural',
 'native_engine': 'edge',
 'native_lang_code': 'hu',
 'english_rate': '-4%',
 'native_rate': '-10%',
 'english_pitch': '+0Hz',
 'native_pitch': '+0Hz',
 'native_label': 'MAGYAR',
 'translit_label': 'SAY IT LIKE',
 'flag': 'hu',
 'greeting': 'Szia!',
 'encouragement': 'Kiváló!',
 'rtl': False,
 'char_tiles': False,
 'script_font': '',
 'glyphs': 'ÁÉÍÓÖŐÚÜŰáéíóöőúüű'}
# ==== LANGUAGE PACK END ====

# ==== CATEGORIES START ====
CATEGORIES = {'Motivation': 'Motiváció',
 'Love': 'Szerelem',
 'Success': 'Siker',
 'Wisdom': 'Bölcsesség',
 'Happiness': 'Boldogság',
 'Self Improvement': 'Önfejlesztés',
 'Gratitude': 'Hála',
 'Friendship': 'Barátság',
 'Hope': 'Remény',
 'Creativity': 'Kreativitás',
 'Inner Peace': 'Belső Béke',
 'Confidence': 'Önbizalom',
 'Perseverance': 'Kitartás',
 'Inspiration': 'Inspiráció',
 'Positive Life': 'Pozitív Élet',
 'Courage': 'Bátorság',
 'Kindness': 'Kedvesség',
 'Patience': 'Türelem',
 'Forgiveness': 'Megbocsátás',
 'Strength': 'Erő',
 'Joy': 'Öröm',
 'Balance': 'Egyensúly',
 'Growth': 'Növekedés',
 'Purpose': 'Cél',
 'Mindfulness': 'Tudatosság',
 'Travel & Airport': 'Utazás és repülőtér',
 'Ordering Food & Dining': 'Ételrendelés és étkezés',
 'Shopping & Prices': 'Vásárlás és árak',
 'Asking for Directions': 'Útvonal kérése',
 'Hotel & Accommodation': 'Szálloda és szállás',
 'Daily Routine': 'Napi rutin',
 'Meeting People & Greetings': 'Emberekkel való találkozás és üdvözlés',
 'Emergency & Health': 'Vészhelyzet és egészség',
 'Public Transportation': 'Tömegközlekedés',
 'Work & Office': 'Munka és iroda',
 'Weather & Small Talk': 'Időjárás és csevegés',
 'Coffee Shop & Bakery': 'Kávézó és pékség',
 'Family & Home': 'Család és otthon',
 'Hobbies & Free Time': 'Hobbi és szabadidő',
 'Dating & Romance': 'Ismerkedés és romantika',
 'Phone Calls & Messages': 'Telefonhívások és üzenetek',
 'Banking & Money': 'Bank és pénz',
 'Doctor & Pharmacy': 'Orvos és gyógyszertár',
 'Sports & Fitness': 'Sport és fitnesz',
 'Celebrations & Parties': 'Ünnepek és partik',
 'Feelings & Emotions': 'Érzések és érzelmek',
 'Agreeing & Disagreeing': 'Egyetértés és egyet nem értés',
 'Making Plans': 'Tervezés',
 'Common Native Slang': 'Gyakori helyi szleng',
 'Cultural Traditions': 'Kulturális hagyományok'}
# ==== CATEGORIES END ====

CATEGORY_NAMES = list(CATEGORIES.keys())

AI_MODEL = os.getenv("AI_MODEL", "openai/gpt-5.4-nano")
AI_FALLBACK_MODEL = os.getenv("AI_FALLBACK_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 7.2
CHAPTER_INTRO_DURATION = 4.4
OUTRO_DURATION = 13.0

EN_CARD_IN = 0.70
GAP_EN_NATIVE = 0.60
NATIVE_CARD_LEAD = 0.40
GAP_BEFORE_REPEAT = 1.00
TAIL_HOLD = 1.30

# ---------------------------------------------------------------- palette

INK = "#30303A"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#7C5CFF"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

# ==== HASHTAGS START ====
HASHTAGS = ['#learnhungarian',
 '#hungarianlessons',
 '#hungarianforbeginners',
 '#languagelearning',
 '#hungarianvocabulary',
 '#velocityhungarian',
 '#dailyhungarian',
 '#hungarian',
 '#learnlanguages',
 '#speakhungarian']
# ==== HASHTAGS END ====
