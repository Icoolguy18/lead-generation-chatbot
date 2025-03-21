# Scraper Logic Overview

This document provides an overview of the `scrapper_hand.py` file, which handles extracting relevant information from user input for web scraping tasks.

## 1. Scraper Logic (`scrapper_hand.py`)

The `scrapper_hand.py` file defines the `logic_scrap` class, which processes user input to extract structured details for scraping operations.

### Key Components:
- **Uses `Google Generative AI (Gemini)` to extract structured data from user prompts.**
- **`respond(requirement)` Method:**
  - Accepts a user query related to scraping.
  - Generates a structured output containing:
    - `first_name`: Extracted first name (if mentioned in input).
    - `last_name`: Extracted last name (if mentioned in input).
    - `domain`: Extracted domain (if present in input).
  - The function ensures only these details are returned, without any extra text.

## 2. Processing Flow
1. The user provides an input related to web scraping.
2. `logic_scrap` processes the input using a structured prompt.
3. The model extracts and returns only `first_name`, `last_name`, and `domain`.
4. The extracted details can then be used for further scraping tasks.

## 3. Future Enhancements
- Improve extraction accuracy for complex queries.
- Extend extraction to additional attributes like company name or email.
- Add error handling for ambiguous or incomplete inputs.


