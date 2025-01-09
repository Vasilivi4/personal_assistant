# Personal Assistant

## Project Description

**Personal Assistant** is a web application that combines several functions for managing everyday tasks. The application includes modules for working with:
- Contacts (adding, editing and deleting contacts).
- Notes (creating, filtering and deleting notes).
- Files (uploading and sorting by categories).
- Weather (displaying the current weather for the selected city).
- News (viewing news by categories).

## Functional Modules

1. **Contacts**
- Storing and managing a list of contacts.
- Ability to search by name, email and other parameters.

2. **Notes**
- Creating, editing and deleting notes.
- Sorting notes by tags.

3. **Files**
- Uploading files to the application.
- Filtering by categories (images, documents, videos, etc.).

4. **News**
- View news articles by various categories (tech, sports, finance, etc.).
- Ability to sort by category.

5. **Weather**
- Display current weather for a specified city using API.

## Project Startup Instructions

### Steps to Run Locally

1. **Clone the repository:**
```bash
git clone https://github.com/your_username/personal_assistant.git
cd personal_assistant
```

2. **Set up a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate # For Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Apply migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Run the development server:**
```bash
python manage.py runserver
```

6. **Open the application in a browser:**
Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### Environment variables

Create a `.env` file in the root folder of the project and add the following variables to it:
```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1, localhost
WEATHER_API_KEY=your_weather_api_key
```

## Deployment

To deploy the application to Heroku, Render or any other platform, follow the official instructions of the chosen hosting.

## Notes
- Use comments and docstrings only where absolutely necessary.
- Make sure all code is formatted according to PEP8.

## Authors
The development team of the **Personal Assistant** project.
- https://github.com/Vasilivi4
- https://github.com/Vojdpenguin
- https://github.com/NikKorYT
- https://github.com/Xeljndjhtw
- https://github.com/OlegKan888