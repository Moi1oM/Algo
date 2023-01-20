fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
# result is [14600, 34400, 5000]
import math
def cal_money(fees, time):
    bsc_time = fees[0]
    bsc_money = fees[1]
    unit_time = fees[2]
    unit_money = fees[3]
    if time <= bsc_time:
        return bsc_money
    else:
        res = bsc_money
        extra_time = time - bsc_time
        res += math.ceil(extra_time / unit_time) * unit_money
        return res
def solution(fees, records):
    answer = []
    in_dict = {}
    res_dict = {}
    for rcd in records:
        time, num, in_out = rcd.split()
        hour, min = map(int, time.split(":"))
        mins = hour * 60 + min
        if in_out == "IN":
            in_dict[num] = mins
        else:
            total_time = mins - in_dict[num]
            del in_dict[num]
            if num in res_dict.keys():
                res_dict[num]+=total_time
            else:
                res_dict[num] = total_time

    for key, val in in_dict.items():
        if key in res_dict.keys():
            res_dict[key] += (23*60+59) - val
        else:
            res_dict[key] = (23*60+59) - val

    itms = sorted(res_dict.items())

    for num, time in itms:
        answer.append(cal_money(fees, time))

    return answer

print("answer is",solution(fees, records))