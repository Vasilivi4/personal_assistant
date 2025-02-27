<img src="https://res.cloudinary.com/dxcgfa3e2/image/upload/v1738503208/zbpfhqtza4vpojchvlhb.png">
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
git clone https://github.com/Vasilivi4/personal_assistant
cd personal_assistant
```

2. **Set up a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate # For Windows: venv\Scripts\activate
```
3. **Install poety:**
```bash
poetry init
poetry install
poetry shell
```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

5. **Apply migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Run the development server:**
```bash
python manage.py runserver
```

7. **Open the application in a browser:**
Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### Environment variables

Create a `.env` file in the root folder of the project and add the following variables to it:
```env
NEWS_API_KEY=news_api_key
ALLOWED_HOSTS=127.0.0.1, localhost
WEATHER_API_KEY=your_weather_api_key
CURRENCY_API_KEY=currency_api_key

POSTGRES_DB=testdatabase
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

MAIL_FROM=email_from
MAIL_PASSWORD=email_password
MAIL_SERVER=email_server

your_api_key=your_api_key
your_api_secret=your_api_secret

CLOUDINARY_URL=cloudinary://<your_api_key>:<your_api_secret>@name
```

## Deployment

- To deploy the application to Heroku, Render or any other platform, follow the official instructions of the chosen hosting.
- https://prominent-debora-personal-assistant-c261ddb2.koyeb.app/

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
