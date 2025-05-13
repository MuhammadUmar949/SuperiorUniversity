#  Activity Selection
def activity_selection(activities):
    activities.sort(key=lambda x: x[1])  # Sort by finish time
    selected = [activities[0]]
    
    for current_start, current_finish in activities[1:]:
        last_finish = selected[-1][1]
        if current_start >= last_finish:
            selected.append((current_start, current_finish))
    
    return selected

# Test
activities = [(1, 3), (2, 5), (3, 9), (6, 8), (8, 11)]
print("Selected activities:", activity_selection(activities))