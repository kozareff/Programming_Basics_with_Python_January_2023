budget = float(input())

video_cards_volume = int(input())
processors_volume = int(input())
ram_volume = int(input())

VIDEO_CARD_PRICE_ONE = 250

video_cards_price = video_cards_volume * VIDEO_CARD_PRICE_ONE
processors_price = processors_volume * video_cards_price * 0.35
ram_price = ram_volume * video_cards_price * 0.1

total_price = video_cards_price + processors_price + ram_price

if video_cards_volume > processors_volume:
    total_price *= 0.85

if total_price <= budget:
    print(f'You have {budget - total_price:.2f} leva left!')
else:
    print(f'Not enough money! You need {total_price - budget:.2f} leva more!')


