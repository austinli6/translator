<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Active Translation Website</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    .container {
      text-align: center;
    }
    select {
      margin: 10px;
      padding: 10px;
    }
    .content {
      margin-top: 20px;
      font-size: 18px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Welcome to Active Translation</h1>
    <p>Select a language to translate the text:</p>
    <select id="languageSelector">
      <option value="English">English</option>
      <option value="Spanish">Spanish</option>
      <option value="French">French</option>
      <option value="German">German</option>
      <option value="Chinese">Chinese</option>
      <option value="Arabic">Arabic</option>
      <option value="Bulgarian">Bulgarian</option>
      <option value="Russian">Russian</option>
      <option value="Greek">Greek</option>
      <option value="Italian">Italian</option>
    </select>
    <div class="content" id="content">
      Hello! This is a sample text for translation.
    </div>
  </div>
  <script>
    const contentElement = document.getElementById("content");
    const languageSelector = document.getElementById("languageSelector");
---
layout: default
title: Basic Translation with Textbox
---

    // Function to handle language changes
    function translateContent() {
      const selectedLanguage = languageSelector.value;
      const originalText = "Hello! This is a sample text for translation.";
<div class="container">
  <h1 id="title">Welcome to Translation with a Textbox</h1>
  <p id="subtitle">Select a language to translate the content and the textbox text:</p>

      // Google Translate API simulation using a translation object
      const translations = {
        "en": "Hello! This is a sample text for translation.",
        "es": "¡Hola! Este es un texto de muestra para traducción.",
        "fr": "Bonjour! Ceci est un texte d'exemple pour la traduction.",
        "de": "Hallo! Dies ist ein Beispieltext zur Übersetzung.",
        "zh-CN": "你好！这是用于翻译的示例文本。"
        "arabic":"مرحباً بكم! هذا نموذج نص للترجمة."
      };
  <!-- Language Selector -->
  <select id="languageSelector">
    <option value="en">English</option>
    <option value="es">Spanish</option>
    <option value="fr">French</option>
    <option value="de">German</option>
    <option value="zh-CN">Chinese</option>
    <option value="arabic">Arabic</option>
  </select>

      // Update the content with the translated text
      contentElement.textContent = translations[selectedLanguage] || originalText;
    }
  <!-- Text Content -->
  <div class="content">
    <p id="paragraph">
      Hello! This is an example of translation functionality. Select a language from the dropdown above.
    </p>
    <p id="textbox-label">Enter text below (translated content will reflect the selected language):</p>
    <textarea id="userTextbox" rows="5" cols="50">
Hello! This text will also be translated dynamically.
    </textarea>
  </div>
</div>

    // Add event listener to the dropdown
    languageSelector.addEventListener("change", translateContent);
  </script>
</body>
</html>
<script src="{{ '/assets/js/basic-translation-textbox.js' | relative_url }}"></script>
