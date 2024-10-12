from transformers import MarianMTModel, MarianTokenizer

class TranslatorBase:
    def __init__(self):
        self._model = None  
        self._tokenizer = None

    def load_model(self, model_name):
        """Load the translation model and tokenizer"""
        self._model = MarianMTModel.from_pretrained(model_name)
        self._tokenizer = MarianTokenizer.from_pretrained(model_name)

    def translate(self, text):
        raise NotImplementedError("Subclasses should implement this method!")

# English to French Translator
class EnglishToFrenchTranslator(TranslatorBase):
    def __init__(self):
        super().__init__()
        self.load_model('Helsinki-NLP/opus-mt-en-fr')  # Load the English to French model

    def translate(self, text):
        inputs = self._tokenizer(text, return_tensors="pt", padding=True)
        translated = self._model.generate(**inputs)
        return self._tokenizer.decode(translated[0], skip_special_tokens=True)

# French to English Translator
class FrenchToEnglishTranslator(TranslatorBase):
    def __init__(self):
        super().__init__()
        self.load_model('Helsinki-NLP/opus-mt-fr-en')  # Load the French to English model

    def translate(self, text):
        inputs = self._tokenizer(text, return_tensors="pt", padding=True)
        translated = self._model.generate(**inputs)
        return self._tokenizer.decode(translated[0], skip_special_tokens=True)

# Spanish to English Translator
class SpanishToEnglishTranslator(TranslatorBase):
    def __init__(self):
        super().__init__()
        self.load_model('Helsinki-NLP/opus-mt-es-en')  # Load the Spanish to English model

    def translate(self, text):
        inputs = self._tokenizer(text, return_tensors="pt", padding=True)
        translated = self._model.generate(**inputs)
        return self._tokenizer.decode(translated[0], skip_special_tokens=True)

# French to Spanish Translator (Example, can be added as needed)
class FrenchToSpanishTranslator(TranslatorBase):
    def __init__(self):
        super().__init__()
        self.load_model('Helsinki-NLP/opus-mt-fr-es')  # Load the French to Spanish model

    def translate(self, text):
        inputs = self._tokenizer(text, return_tensors="pt", padding=True)
        translated = self._model.generate(**inputs)
        return self._tokenizer.decode(translated[0], skip_special_tokens=True)

