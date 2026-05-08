def last_work_experience(work_experiences):
    if len(work_experiences) == 0:
        return None
    end = len(work_experiences) - 1
    return work_experiences[end] 
