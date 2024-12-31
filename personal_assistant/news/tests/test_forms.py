from news.forms import NewsForm

def test_news_form_valid_data():
    form = NewsForm(data={"title": "Test News", "content": "Content", "category": "finance"})
    assert form.is_valid()

def test_news_form_invalid_data():
    form = NewsForm(data={"title": "", "content": "Content", "category": "finance"})
    assert not form.is_valid()
