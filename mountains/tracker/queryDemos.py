# # returns all mountains from mountain table
# mountains = Mountain.objects.all()

# # returns first mountain in table
# firstMountain = Mountain.objects.first()

# # returns last mountain in table
# lastMountain = Mountain.objects.last()

# # returns single mountain by name
# mountainByName = Mountain.objects.get(name='Seefin')

# # returns single mountain by id
# mountainByName = Mountain.objects.get(id='3')

# # returns mountains from mountain table filtered by area
# mountains = Mountain.objects.filter(area='Dublin/Wicklow')

# # order/sort mountains by date_climbed
# mountains = Mountain.objects.all().order_by('date_climbed')

# # order/sort mountains by height starting with lowest
# mountains = Mountain.objects.all().order_by('-height')

