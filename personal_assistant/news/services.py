"""Module services.py."""

# Version: 2021.10.17

import logging
import cloudinary
import requests
from django.shortcuts import render
from django import forms
from news.models import NewsSummary
from cloudinary.uploader import upload


class CategoryForm(forms.Form):
    """Class CategoryForm representing a person"""

    CATEGORY_CHOICES = [
        ("business", "Business"),
        ("entertainment", "Entertainment"),
        ("general", "General"),
        ("health", "Health"),
        ("science", "Science"),
        ("sports", "Sports"),
        ("technology", "Technology"),
    ]
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES, required=False, label="Category"
    )


class NewsService:
    """Class NewsService representing a person"""

    def __init__(self, api_key, base_url="https://newsapi.org/v2"):
        self.api_key = api_key
        self.base_url = base_url
        self.logger = logging.getLogger(__name__)

    def fetch_news(
        self,
        category=None,
        country="us",
        page_size=15,
        language="en",
        from_date=None,
        to_date=None,
        user=None,
    ):
        """Function fetch_news printing python version."""
        url = f"{self.base_url}/top-headlines"
        params = {
            "apiKey": self.api_key,
            "country": country,
            "pageSize": page_size,
            "language": language,
        }

        if category:
            params["category"] = category
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            articles = response.json().get("articles", [])

            for article in articles:
                NewsSummary.objects.create(
                    user=user,
                    title=article["title"],
                    content=article.get("description", ""),
                    date=article["publishedAt"][:10],
                )

            return articles
        except requests.exceptions.RequestException as e:
            self.logger.error("Error fetching news: %s", e)
            return []

    def fetch_sources(self):
        """Function fetch_sources printing python version."""
        url = f"{self.base_url}/sources"
        params = {"apiKey": self.api_key}

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json().get("sources", [])
        except requests.exceptions.RequestException as e:
            self.logger.error("Error fetching sources: %s", e)
            return [
                {"name": "Source 1", "description": "Description 1"},
                {"name": "Source 2", "description": "Description 2"},
            ]


def news_list_view(request):
    """Function news_list_view printing python version."""
    form = CategoryForm(request.GET)
    news = []

    if form.is_valid():
        selected_category = form.cleaned_data.get("category")
        if selected_category:
            news_service = NewsService(api_key="your_api_key")
            news = news_service.fetch_news(category=selected_category)
    else:

        news = NewsSummary.objects.all().order_by("-date")

    return render(request, "news/news_list.html", {"news": news, "form": form})


def upload_images_to_cloudinary():
    """Function upload_images_to_cloudinary printing python version."""
    image_files = [
        "https://res.cloudinary.com/dxcgfa3e2/image/upload/v1737404075/images/ftopxylji1twl9o4kfmh.png",
        "https://res.cloudinary.com/dxcgfa3e2/image/upload/v1737404076/images/nwmmcd1xfsokpk1brhdl.png",
        "https://res.cloudinary.com/dxcgfa3e2/image/upload/v1737404076/images/udb11ue7ytxwccrxq6mm.png",
        "https://res.cloudinary.com/dxcgfa3e2/image/upload/v1737404077/images/k6ofawgnhty1mdsxusf7.png",
        "https://res.cloudinary.com/dxcgfa3e2/image/upload/v1737404078/images/orabb09asjwykxqftade.png",
    ]
    descriptions = [
        "Александр Шевелёв Tim Новини та погода и style.",
        "Максим Регуш Scram Авторизація та автентифікація и style",
        "Нікіта Коршомний Dev Нотатки з тегами и style",
        "Максим Бойчук Dev Вигрузка файлів на хмару и style",
        "Олег Суслинець Dev Книга контактів и style",
    ]
    about_me = [
        "Привет! Да, у меня действительно много мыслей в голове. Недавно я начал задумываться о своих целях и мечтах на будущее. Я понял, что хочу достичь успеха в своей карьере и стать профессионалом в своей области. Также, я задумался о том, какой я хочу быть человеком и каким вкладом я могу принести в этот мир. Возможно, ты можешь поделиться своими мыслями и опытом по этим вопросам? Наверное, у меня сейчас путаница в голове. Но я постараюсь разобраться и принять решение. Возможно, мне нужно надеть свою самую умную шляпу и придумать план действий. Я не должен забывать быть уверенным и сильным, чтобы преодолеть любые трудности. Возможно, мне пригодится поддержка и одобрение окружающих. Я должен идти вперед и шагать к своей цели.",
        "About me",
        "About me",
        "About me",
        "About me",
    ]
    links = [
        "https://github.com/Vasilivi4",
        "https://github.com/Vojdpenguin",
        "https://github.com/NikKorYT",
        "https://github.com/Xeljndjhtw",
        "https://github.com/OlegKan888",
    ]
    image_data = []

    for i, image in enumerate(image_files):
        try:
            if image.startswith("https://res.cloudinary.com"):
                print(f"Пропускаем загрузку: {image}")
                image_data.append(
                    {
                        "url": image,
                        "description": descriptions[i],
                        "link": links[i],
                        "about_me": about_me[i],
                    }
                )
            else:
                result = upload(image, folder="images", resource_type="image")
                image_url = result["secure_url"]
                image_data.append(
                    {"url": image_url, "description": descriptions[i], "link": links[i]}
                )
        except (requests.exceptions.RequestException, cloudinary.exceptions.Error) as e:
            print(f"Processing error {image}: {e}")

    print(f"Downloaded data: {image_data}")
    return image_data
