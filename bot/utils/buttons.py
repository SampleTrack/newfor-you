from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def deal_button(link):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    '🛒 Buy Now',
                    url=link
                )
            ]
        ]
    )
