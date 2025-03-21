# lead-generation-chatbot
# Chatbot Application Overview

This document provides an overview of the chatbot application, detailing its components and functionality.

## 1. Flask Application (`pipe_app.py`)

The `pipe_app.py` file is responsible for running the Flask-based web application. It serves as the main entry point for handling user input and returning responses.

### Key Components:
- **Flask Setup**: Initializes the Flask app.
- **Routes**:
  - `/`: Renders the `index.html` template.
  - `/api/chat` (POST): Accepts user input as JSON and processes it through the `AppLogic` class.
- **Response Handling**: Calls `execute()` from `AppLogic` to process user input and return a response.

## 2. Logic Handling (`pipeline.py`)

The `pipeline.py` file defines the `AppLogic` class, which processes user input and interacts with different modules.

### Dependencies:
The script imports multiple external modules to handle various tasks:
- **`program_response`**: Extracts categories from user input.
- **`writer`**: Generates text output.
- **`DB_logic`**: Handles database interactions.
- **`Scrapper`**: Extracts information from external sources.
- **`DataSheetChecker`**: Checks and updates an Excel sheet (`data.xlsx`).
- **`logic_scrap`**: Handles additional scraping logic.

### `AppLogic` Class:
- **`process_prompt(user_input)`**:
  - Calls `program_response` to categorize input.
  - Returns the identified category.

- **`execute(user_input)`**:
  - Calls `process_prompt()` to classify input into "Scrapper" or "Generation".
  - **If "Scrapper" category:**
    - Uses `logic_scrap` to extract data.
    - Checks `data.xlsx` for existing data.
    - If found, returns stored data.
    - If not found, scrapes data, updates `data.xlsx`, and returns scraped details.
  - **If "Generation" category:**
    - Calls `writer` to generate content.
    - Returns the generated response.

## 3. Data Flow
1. User sends input via `/api/chat`.
2. `pipe_app.py` forwards input to `AppLogic.execute()`.
3. `execute()` determines whether to scrape or generate content.
4. Response is sent back to the user via JSON.

## 4. File Dependencies
- `Gemma/`: Contains modules for handling prompts, generation, and database logic.
- `call_api/`: Handles web scraping and API data fetching.
- `data.xlsx`: Stores previously fetched data to avoid redundant scraping.

## 5. Future Enhancements
- Improve error handling and logging.
- Support additional chatbot functionalities.
- Optimize database interactions for performance improvements.

