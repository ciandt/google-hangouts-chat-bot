def create_text_response(text):
    if not text:
        raise ValueError(f"Invalid text: {text}")

    return {"text": text}


def create_cards_response(cards):
    if not isinstance(cards, list):
        raise TypeError(f"Cards should be a list")

    cards = list(filter(None, cards))
    if len(cards) == 0:
        raise ValueError(f"Cards should not be empty")

    return {"cards": cards}


def create_card_header(title, subtitle, image, image_style="IMAGE"):
    if not title:
        raise ValueError(f"Invalid title: {title}")

    if not subtitle:
        raise ValueError(f"Invalid subtitle: {subtitle}")

    if not image:
        raise ValueError(f"Invalid image: {image}")

    styles = ["IMAGE", "AVATAR"]
    if image_style not in styles:
        raise ValueError(f"Invalid image_style: {image_style}")

    return {
        "header": {
            "title": title,
            "subtitle": subtitle,
            "imageUrl": image,
            "imageStyle": image_style,
        }
    }


def create_card_paragraph(text):
    if not text:
        raise ValueError(f"Invalid text: {text}")

    return {"textParagraph": {"text": text}}


def create_card_key_value(
    top_label, content, bottom_label=None, icon=None, on_click=None
):
    if not top_label:
        raise ValueError(f"Invalid top_label: {top_label}")

    if not content:
        raise ValueError(f"Invalid content: {content}")

    key_value = {"topLabel": top_label, "content": content}

    if bottom_label:
        key_value.update({"bottomLabel": bottom_label})

    if icon:
        key_value.update({"icon": icon})

    if on_click:
        key_value.update({"onClick": {"openLink": {"url": on_click}}})

    return {"keyValue": key_value}


def create_card_image(image_url, link=None):
    if not image_url:
        raise ValueError(f"Invalid image_url: {image_url}")

    image = {
        "imageUrl": image_url,
    }

    if link:
        image.update({"onClick": {"openLink": {"url": link}}})

    return {"image": image}


def create_card_buttons(buttons):
    if not isinstance(buttons, list):
        raise TypeError(f"Buttons should be a list")

    return {"buttons": buttons}


def create_card_text_button(text, *, link=None, action=None, params=None):
    if not text:
        raise ValueError(f"Invalid text: {text}")

    if not link and not action:
        raise ValueError(f"A link or an action should be informed")

    if link and action:
        raise ValueError(f"Link and action informed. Only one should be informed")

    if link:
        on_click = {"openLink": {"url": link}}
    else:
        on_click = {}

        if params:
            if not isinstance(params, dict):
                raise TypeError("params should be a dict")

            on_click.update(
                {
                    "action": {
                        "actionMethodName": action,
                        "parameters": [
                            {"key": key, "value": value}
                            for key, value in params.items()
                        ],
                    }
                }
            )

        else:
            on_click.update({"action": {"actionMethodName": action}})

    button = {"text": text, "onClick": on_click}

    return {"textButton": button}


def create_card(widgets, header=None):
    if not isinstance(widgets, list):
        raise TypeError(f"Widgets should be a list")

    widgets = list(filter(None, widgets))
    if len(widgets) == 0:
        raise ValueError(f"Widgets should not be empty")

    card = {}

    if header is not None:
        card.update(header)

    card.update({"sections": [{"widgets": widgets}]})

    return card


#######
#
#
# INTERACTIVE_TEXT_BUTTON_ACTION = "doTextButtonAction"
# INTERACTIVE_IMAGE_BUTTON_ACTION = "doImageButtonAction"
# INTERACTIVE_BUTTON_PARAMETER_KEY = "param_key"
# BOT_HEADER = 'Card Bot Python'
#
#
# def create_card_response2(event_message):
#     response = dict()
#     cards = list()
#     widgets = list()
#     header = None
#
#     words = event_message.lower().split()
#
#     for word in words:
##
#         elif word == 'interactiveimagebutton':
#             widgets.append({
#                 'buttons': [
#                     {
#                         'imageButton': {
#                             'icon': 'EVENT_SEAT',
#                             'onClick': {
#                                 'action': {
#                                     'actionMethodName': INTERACTIVE_IMAGE_BUTTON_ACTION,
#                                     'parameters': [{
#                                         'key': INTERACTIVE_BUTTON_PARAMETER_KEY,
#                                         'value': event_message
#                                     }]
#                                 }
#                             }
#                         }
#                     }
#                 ]
#             })
#
#         elif word == 'imagebutton':
#             widgets.append({
#                 'buttons': [
#                     {
#                         'imageButton': {
#                             'icon': 'EVENT_SEAT',
#                             'onClick': {
#                                 'openLink': {
#                                     'url': 'https://developers.google.com',
#                                 }
#                             }
#                         }
#                     }
#                 ]
#             })
#
#     if header is not None:
#         cards.append(header)
#
#     cards.append({'sections': [{'widgets': widgets}]})
#     response['cards'] = cards
#
#     return response
