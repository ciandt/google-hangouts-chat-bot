import pytest

from google_hangouts_chat_bot.responses import (
    create_text_response,
    create_card_header,
    create_card_paragraph,
    create_card_key_value,
    create_card_image,
    create_card,
    create_cards_response,
)


def test_create_text_response():
    assert create_text_response("hello") == {"text": "hello"}


def test_create_invalid_text_response():
    with pytest.raises(ValueError):
        create_text_response(None)


def test_create_card_header_with_invalid_title():
    with pytest.raises(ValueError):
        create_card_header(None, "Subtitle", "http://server.com/image.png")


def test_create_card_header_with_invalid_subtitle():
    with pytest.raises(ValueError):
        create_card_header("Title", None, "http://server.com/image.png")


def test_create_card_header_with_invalid_image():
    with pytest.raises(ValueError):
        create_card_header("Title", "Subtitle", None)


def test_create_card_header_with_default_style():
    expected = {
        "header": {
            "title": "Title",
            "subtitle": "Subtitle",
            "imageUrl": "http://server.com/image.png",
            "imageStyle": "IMAGE",
        }
    }

    assert (
        create_card_header("Title", "Subtitle", "http://server.com/image.png")
        == expected
    )


def test_create_card_header_with_image_style():
    expected = {
        "header": {
            "title": "Title",
            "subtitle": "Subtitle",
            "imageUrl": "http://server.com/image.png",
            "imageStyle": "IMAGE",
        }
    }

    assert (
        create_card_header("Title", "Subtitle", "http://server.com/image.png", "IMAGE")
        == expected
    )


def test_create_card_header_with_avatar_style():
    expected = {
        "header": {
            "title": "Title",
            "subtitle": "Subtitle",
            "imageUrl": "http://server.com/image.png",
            "imageStyle": "AVATAR",
        }
    }

    assert (
        create_card_header("Title", "Subtitle", "http://server.com/image.png", "AVATAR")
        == expected
    )


def test_create_card_header_with_invalid_style():
    with pytest.raises(ValueError):
        create_card_header(
            "Title", "Subtitle", "http://server.com/image.png", "INVALID"
        )


def test_create_invalid_card_paragraph():
    with pytest.raises(ValueError):
        create_card_paragraph(None)


def test_create_card_paragraph():
    expected = {"textParagraph": {"text": "hello"}}

    assert create_card_paragraph("hello") == expected


def test_create_card_key_value_with_invalid_top_label():
    with pytest.raises(ValueError):
        create_card_key_value(None, "Content")


def test_create_card_key_value_with_invalid_content():
    with pytest.raises(ValueError):
        create_card_key_value("Top Label", None)


def test_create_simple_card_key_value():
    expected = {"keyValue": {"topLabel": "Top Label", "content": "Content"}}

    assert create_card_key_value("Top Label", "Content") == expected


def test_create_card_key_value_with_bottom_label():
    expected = {
        "keyValue": {
            "topLabel": "Top Label",
            "content": "Content",
            "bottomLabel": "Bottom Label",
        }
    }

    assert (
        create_card_key_value("Top Label", "Content", bottom_label="Bottom Label")
        == expected
    )


def test_create_card_key_value_with_icon():
    expected = {
        "keyValue": {
            "topLabel": "Top Label",
            "content": "Content",
            "icon": "BUILT-IN ICON",
        }
    }

    assert (
        create_card_key_value("Top Label", "Content", icon="BUILT-IN ICON") == expected
    )


def test_create_card_key_value_with_on_click():
    expected = {
        "keyValue": {
            "topLabel": "Top Label",
            "content": "Content",
            "onClick": {"openLink": {"url": "https://url.com"}},
        }
    }

    assert (
        create_card_key_value("Top Label", "Content", on_click="https://url.com")
        == expected
    )


def test_create_invalid_card_image():
    with pytest.raises(ValueError):
        create_card_image(None)


def test_create_card_image():
    expected = {"image": {"imageUrl": "https://server.com/image.png"}}

    assert create_card_image("https://server.com/image.png") == expected


def test_create_card_image_with_link():
    expected = {
        "image": {
            "imageUrl": "https://server.com/image.png",
            "onClick": {"openLink": {"url": "http://link.com"}},
        }
    }

    assert (
        create_card_image("https://server.com/image.png", "http://link.com") == expected
    )


def test_create_invalid_card():
    with pytest.raises(TypeError):
        assert create_card(None)


def test_create_invalid_card_with_empty_list():
    with pytest.raises(ValueError):
        assert create_card([None, None])

    with pytest.raises(ValueError):
        assert create_card([])


def test_create_card():
    widgets = [create_card_paragraph("Hello")]

    expected = {"sections": [{"widgets": [{"textParagraph": {"text": "Hello"}}]}]}

    assert create_card(widgets) == expected


def test_create_card_with_multiple_widgets():
    widgets = [
        create_card_paragraph("Hello"),
        create_card_image("http://server.com/image.png"),
    ]

    expected = {
        "sections": [
            {
                "widgets": [
                    {"textParagraph": {"text": "Hello"}},
                    {"image": {"imageUrl": "http://server.com/image.png"}},
                ]
            }
        ]
    }

    assert create_card(widgets) == expected


def test_create_card_with_header():
    widgets = [
        create_card_paragraph("Hello"),
        create_card_image("http://server.com/image.png"),
    ]

    header = create_card_header("Title", "Subtitle", "http://server.com/header.png")

    expected = {
        "header": {
            "title": "Title",
            "subtitle": "Subtitle",
            "imageUrl": "http://server.com/header.png",
            "imageStyle": "IMAGE",
        },
        "sections": [
            {
                "widgets": [
                    {"textParagraph": {"text": "Hello"}},
                    {"image": {"imageUrl": "http://server.com/image.png"}},
                ]
            }
        ],
    }

    assert create_card(widgets, header=header) == expected


def test_create_invalid_cards_response():
    with pytest.raises(TypeError):
        assert create_cards_response(None)


def test_create_invalid_cards_response_with_empty_list():
    with pytest.raises(ValueError):
        assert create_cards_response([None, None])

    with pytest.raises(ValueError):
        assert create_cards_response([])


def test_create_cards_response():
    header = create_card_header("Title", "Subtitle", "http://server.com/header.png")

    widgets = [
        create_card_paragraph("Hello"),
        create_card_image("http://server.com/image.png"),
    ]

    card1 = create_card(widgets, header=header)

    card2 = create_card(
        [create_card_paragraph("World"), create_card_key_value("Label", "Content")]
    )

    expected = {
        "cards": [
            {
                "header": {
                    "title": "Title",
                    "subtitle": "Subtitle",
                    "imageUrl": "http://server.com/header.png",
                    "imageStyle": "IMAGE",
                },
                "sections": [
                    {
                        "widgets": [
                            {"textParagraph": {"text": "Hello"}},
                            {"image": {"imageUrl": "http://server.com/image.png"}},
                        ]
                    }
                ],
            },
            {
                "sections": [
                    {
                        "widgets": [
                            {"textParagraph": {"text": "World"}},
                            {"keyValue": {"content": "Content", "topLabel": "Label"}},
                        ]
                    }
                ]
            },
        ]
    }

    assert create_cards_response([card1, card2]) == expected
