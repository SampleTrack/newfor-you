def amazon_affiliate(link, tag='yourtag-21'):
    if 'tag=' in link:
        return link

    if '?' in link:
        return f'{link}&tag={tag}'

    return f'{link}?tag={tag}'


def flipkart_affiliate(link, affid='youraffid'):
    if 'affid=' in link:
        return link

    if '?' in link:
        return f'{link}&affid={affid}'

    return f'{link}?affid={affid}'
