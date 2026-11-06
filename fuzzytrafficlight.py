def fuzzy_controller(density):

    # Fuzzification
    low = max(0, min(1, (50 - density) / 50))
    medium = max(0, min((density - 25) / 25, (75 - density) / 25, 1))
    high = max(0, min(1, (density - 50) / 50))

    # Rule evaluation
    low_rule = low
    medium_rule = medium
    high_rule = high

    # Output values (green signal duration)
    low_time = 20
    medium_time = 40
    high_time = 60

    # Defuzzification
    total = low_rule + medium_rule + high_rule

    if total == 0:
        return 20

    green_time = (
        low_rule * low_time +
        medium_rule * medium_time +
        high_rule * high_time
    ) / total

    return green_time


density = 80

print("Traffic Density:", density)
print("Green Signal Time:", fuzzy_controller(density), "seconds")