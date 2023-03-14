infos = input("").strip("").split(" ")
[total_meters, race_track_size] = map(lambda x: int(x), infos)
print(total_meters % race_track_size)