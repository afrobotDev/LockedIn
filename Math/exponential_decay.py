def decayed_followers(initial_followers, fractional_lost_daily, days):
    return initial_followers * ((1 - fractional_lost_daily) ** days) 
