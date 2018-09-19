import math

def getDistanceFromXtoY(lng_a,lat_a, lng_b,  lat_b):
    pk = 180 / math.pi
    a1 = float(lat_a) / pk
    a2 = float(lng_a) / pk
    b1 = float(lat_b) / pk
    b2 = float(lng_b) / pk
    t1 = math.cos(a1) * math.cos(a2) * math.cos(b1) * math.cos(b2)
    t2 = math.cos(a1) * math.sin(a2) * math.cos(b1) * math.sin(b2)
    t3 = math.sin(a1) * math.sin(b1)
    t = t1 + t2 + t3
    if t > 1:
        t = 1
    tt = math.acos(t)
    return 6372800 * tt

lines = open("/Users/caiyang/Desktop/op_move_bike_01.log").readlines()

lines = [eval(item) for item in lines]

# print(lines[1])
# for i in lines[1]:
#     print(i, end=' ')

wf = open("/Users/caiyang/Desktop/op_move_bike_02.log", "w")

for i, item in enumerate(lines[1:]):
    if i == 0:
        continue
    if item[0] == '0' and lines[i-1][0] == '1' and lines[i-1][1] == item[1]:  # 挪车前是订单结束
        if len(item[2].strip()) == 0:  # 没有地址跳过
            continue
        point0 = item[2].split("|")
        point1 = lines[i-1][2].split("|")
        if point1[0] == 'null':  # 地址为空null,跳过
            continue
        t = item[3] - lines[i-1][3]
        distance = int(getDistanceFromXtoY(point0[0], point0[1], point1[1], point1[0]))
        if distance >= 50:
            print(item + lines[i-1] + [t, distance], file=wf)
            print(item + lines[i-1] + [t, distance])
wf.close()



