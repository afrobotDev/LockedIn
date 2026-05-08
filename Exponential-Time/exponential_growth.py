def exponential_growth(n, factor, days):
    growth_sequence = []
    for i in range(0, days + 1):
        growth_sequence.append(n * ( factor ** i))
    return growth_sequence
