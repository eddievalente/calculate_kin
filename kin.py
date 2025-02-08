from datetime import datetime, timedelta

def days_difference_excluding_leap_days(date1, date2):
    
    # Sorts dates to always calculate in the correct order
    start_date, end_date = sorted([date1, date2])

    # Initialize counters
    total_days = 0
    current_date = start_date

    while current_date < end_date:
        # Checks if the current day is not February 29th
        if not (current_date.month == 2 and current_date.day == 29):
            total_days += 1
        # Advance to the next day
        current_date += timedelta(days=1)
    
    return total_days

def calculate_kin(birth_date):
    # Tzolkin starts on August 11, 3114 BCE in the Gregorian calendar
    # Reference date for Tzolkin in modern times: Mar 30, 1968, kin 1
    tzolkin_reference_date = datetime(1968, 3, 30)
    tzolkin_reference_kin = 1
    
    # Convert birth_date to datetime object
    try:
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD."

    # Calculate days difference from reference date
    days_difference = days_difference_excluding_leap_days(tzolkin_reference_date, birth_date)

    # Tzolkin cycle has 260 days
    tzolkin_cycle_length = 260

    # Calculate kin number
    kin = (tzolkin_reference_kin + days_difference) % tzolkin_cycle_length
    if kin == 0:
        kin = tzolkin_cycle_length

    return kin

def get_day_name(kin):
    tzolkin_day_names = [
        "Crocodile", "Wind", "Night", "Seed", "Serpent", "Death", "Deer", "Star", "Water", "Dog",
        "Monkey", "Road", "Reed", "Jaguar", "Eagle", "Wisdom", "Earth", "Knife", "Storm", "Sun"
    ]
    day_name_index = (kin - 1) % 20
    day_name = tzolkin_day_names[day_name_index]
    return day_name

def get_tone(kin):
    tzolkin_tones = [
        "Magnetic", "Lunar", "Electric", "Self-Existing", "Overtone", "Rhythmic",
        "Resonant", "Galactic", "Solar", "Planetary", "Spectral", "Crystal", "Cosmic"
    ]
    tone_index = (kin - 1) % 13
    tone = tzolkin_tones[tone_index]
    return tone

def get_glyph(kin):
    tzolkin_glyphs = [
        "Dragon", "Wind", "Night", "Seed", "Serpent", "Death", "Deer", "Star", "Moon", "Dog",
        "Monkey", "Human", "Skywalker", "Wizard", "Eagle", "Warrior", "Earth", "Mirror", "Storm", "Sun"
    ]
    day_name_index = (kin - 1) % 20
    glyph = tzolkin_glyphs[day_name_index]
    return glyph

def get_color(kin):
    tzolkin_colors = ["Red", "White", "Blue", "Yellow"]
    color_index = (kin - 1) % 4
    color = tzolkin_colors[color_index]
    return color

def explain_kin(birth_date):
    # Calculate kin number
    kin = calculate_kin(birth_date)

    # Retrieve Tzolkin elements
    # day_name = get_day_name(kin)
    tone = get_tone(kin)
    glyph = get_glyph(kin)
    color = get_color(kin)

    return kin, f"{glyph} {tone} {color}"

# Example usage
if __name__ == "__main__":
    birth_date = input("Enter your birth date (YYYY-MM-DD): ")
    kin, kin_name = explain_kin(birth_date)
    print(f"Your kin is: {kin} ({kin_name})")
