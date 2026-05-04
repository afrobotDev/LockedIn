def get_avg_brand_followers(all_handles, brand_name):
    num_handles = 0
    num_influencers = 0
    for influencer in all_handles:
        num_influencers += 1
        for follower in influencer:
            if brand_name in follower:
                num_handles += 1
    return num_handles/num_influencers
    

