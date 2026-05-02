def get_estimated_spread(audiences_followers):
    num_followers = len(audiences_followers) 
    if num_followers == 0:
        return 0

    total = 0
    for i in audiences_followers:
        total += i

    average_audiences_followers = total/num_followers
    return average_audiences_followers * (num_followers ** 1.2)

