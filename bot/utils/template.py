def build_deal_post(title, price, link, tag='#deals'):
    text = f'''
🔥 <b>{title}</b>

💰 Price: <code>{price}</code>

🛒 Buy Now 👇
{link}

{tag}
'''
    return text
