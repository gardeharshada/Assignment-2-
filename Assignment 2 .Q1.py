# convert time entered in hours ,min, and seconds into seconds : 
def time_to_seconds(hours, minutes, seconds):
    total_seconds = (hours * 3600) + (minutes * 60) + seconds 
    return total_seconds

hours = 2
minutes = 20
seconds = 50
print(time_to_seconds(hours, minutes, seconds))