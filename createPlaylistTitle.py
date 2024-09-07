from datetime import date

today = date.today()
week_number = today.isocalendar().week
week_year = today.isocalendar().year


def create_playlist_title():
    return f"Discover {week_year} - w{week_number}"
