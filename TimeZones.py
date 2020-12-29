t1 = "Sun 10 May 2015 13:54:36 -0700"
t2 = "Sun 10 May 2015 13:54:36 -0000"

def time_delta():
    from datetime import datetime as dt
    for _ in range(int(input())):
        t1 = dt.strptime(input(), "%a %d %b %Y %X %z")
        t2 = dt.strptime(input(), "%a %d %b %Y %X %z")
        print(abs(int((t1-t2).total_seconds())))

def time_delta2(t1, t2):
    months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
              'September': 9, 'October': 10, 'November': 11, 'December': 12}
    t1_l = t1.split(" ")
    t2_l = t2.split(" ")
    hms1 = list(map(int, t1_l[4].split(":")))
    hms2 = list(map(int, t2_l[4].split(":")))
    if t1_l[5][0] == "-":
        a = -1
    else:
        a = 1
    if t2_l[5][0] == "-":
        b = -1
    else:
        b = 1
    tzn_hm1 = [a * int(t1_l[5][1:3]), a * int(t1_l[5][3:5])]
    tzn_hm2 = [b * int(t2_l[5][1:3]), b * int(t2_l[5][3:5])]
    yr_diff = int(t1_l[3]) - int(t2_l[3])
    month_diff = months[t1_l[2]] - months[t2_l[2]]
    day_diff = int(t1_l[1]) - int(t2_l[1])
    hour_diff = int(hms1[0]) - int(hms2[0]) + tzn_hm1[0] - tzn_hm2[0]
    min_diff = int(hms1[1]) - int(hms2[1]) + tzn_hm1[1] - tzn_hm2[1]
    sec_diff = int(hms1[2]) - int(hms2[2])
    print(t1_l)
    print(t2_l)
    print(yr_diff)
    print(month_diff)
    total_sec_diff = int(
        abs((((((yr_diff + month_diff / 12) * 365 + day_diff) * 24 + hour_diff) * 60 + min_diff) * 60 + sec_diff)))
    print(total_sec_diff)

time_delta()
