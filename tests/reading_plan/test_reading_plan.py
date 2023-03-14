from unittest.mock import patch
from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501

import pytest

MOCK_DATABASE = [
    {
        "url": "https://blog.betrybe.com/novidades/noticia-cana",
        "title": "Notícia cana",
        "timestamp": "04/04/2021",
        "writer": "Eu",
        "reading_time": 2,
        "summary": "Algo muito cana aconteceu",
        "category": "Ferramentas",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia-banana",
        "title": "Notícia banana",
        "timestamp": "04/04/2021",
        "writer": "Eu",
        "reading_time": 10,
        "summary": "Algo muito banana aconteceu",
        "category": "Ferramentas",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia-bacana",
        "title": "Notícia bacana",
        "timestamp": "04/04/2021",
        "writer": "Eu",
        "reading_time": 1,
        "summary": "Algo muito bacana aconteceu",
        "category": "Ferramentas",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia-toscana",
        "title": "Notícia toscana",
        "timestamp": "04/04/2021",
        "writer": "Eu",
        "reading_time": 1,
        "summary": "Algo muito toscana aconteceu",
        "category": "Ferramentas",
    },
]


@patch('tech_news.analyzer.reading_plan.find_news')
def test_reading_plan_group_news(mock_find_news):
    mock_find_news.return_value = MOCK_DATABASE

    response = ReadingPlanService.group_news_for_available_time(2)

    assert len(response['readable']) == 3
    assert len(response['unreadable']) == 1
    assert response['readable'][0]["unfilled_time"] == 0

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        assert ReadingPlanService.group_news_for_available_time(0)
