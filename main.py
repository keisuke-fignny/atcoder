def make_heights_list(height):
    return [int(height), True]
 
 
tower_len, roads_len = map(int, input().split(' '))
 
heights = [[0, False]]
heights += (list(map(make_heights_list, input().split(' '))))
 
#print(heights)
 
# 塔を基準にして、その塔ごとに繋がる道をリストアップする
roads_highest = list()
for i in range(roads_len):
    start, end = map(int, input().split(' '))
    #print(start, end)
    if heights[start][1] is True and heights[end][0] >= heights[start][0]:
        heights[start][1] = False
        # ng_len += 1
    if heights[end][1] is True and heights[start][0] >= heights[end][0]:
        heights[end][1] = False
        # ng_len += 1
 
good_towers_len = 0
for tower in heights:
    if tower[1]:
        good_towers_len += 1
 
#print(heights)
 
print(good_towers_len)

