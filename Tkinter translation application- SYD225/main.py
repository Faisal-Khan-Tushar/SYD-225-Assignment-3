import tkinter as tk
from tkinter import ttk  # Import the themed widget module
from translator import (
    EnglishToFrenchTranslator,
    FrenchToEnglishTranslator,
    SpanishToEnglishTranslator
)
from utils import log_time

class TranslationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Language Translation App - SYD225")  # Include group name in title
        self.geometry("500x400")
        
        # Initialize translators for selected languages
        self.translators = {
            "English to French": EnglishToFrenchTranslator(),
            "French to English": FrenchToEnglishTranslator(),
            "Spanish to English": SpanishToEnglishTranslator()
        }

        for translator in self.translators.values():
            translator.load_model('Helsinki-NLP/opus-mt-en-fr')  # You may need to use appropriate models

        self.create_widgets()

    def create_widgets(self):
        """Create input, buttons, and output display"""
        # Group name display
        self.group_label = tk.Label(self, text="Group Name: SYD225", font=("Arial", 14))
        self.group_label.pack(pady=10)

        # Input label and text box
        self.input_label = tk.Label(self, text="Enter text to translate:", font=("Arial", 12))
        self.input_label.pack()

        self.input_text = tk.Entry(self, width=50)
        self.input_text.pack(pady=5)

        # Language selection dropdown
        self.language_label = tk.Label(self, text="Select language to translate to:", font=("Arial", 12))
        self.language_label.pack()

        self.language_choice = ttk.Combobox(self, values=list(self.translators.keys()), state='readonly')
        self.language_choice.set("English to French")  # Default selection
        self.language_choice.pack(pady=5)

        # Button to trigger translation
        self.translate_button = tk.Button(self, text="Translate", command=self.perform_translation, bg="blue", fg="white", font=("Arial", 12))
        self.translate_button.pack(pady=20)

        # Output label and text
        self.output_label = tk.Label(self, text="Translated Text:", font=("Arial", 12))
        self.output_label.pack()

        self.output_text = tk.Label(self, text="", wraplength=400, font=("Arial", 12))
        self.output_text.pack(pady=5)

    @log_time  # Applying a decorator to track time taken for translation
    def perform_translation(self):
        """Handle translation when the button is clicked"""
        input_text = self.input_text.get()
        selected_translation = self.language_choice.get()

        if input_text:
            # Determine the translator to use based on selected language
            translator = self.translators[selected_translation]
            result = translator.translate(input_text)
            self.output_text.config(text=result)

if __name__ == "__main__":
    app = TranslationApp()
    app.mainloop()
