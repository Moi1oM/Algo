today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

def valid(year, month, day, today):
    res = True
    tyear, tmonth, tday = map(int, today.split("."))
    if tyear > year:
        res = False
    elif tyear < year:
        pass
    else:
        if tmonth > month:
            res = False
        elif tmonth < month:
            pass
        else:
            if tday > day:
                res = False
            elif tday <= day:
                pass
    return res

def solution(today, terms, privacies):
    answer=[]
    termss = {}
    for i in terms:
        a, b = i.split()
        b = int(b)
        termss[a]=b
    index = 0
    for days_term in privacies:
        index += 1
        days, term = days_term.split()
        year, month, day = map(int, days.split('.'))
        month += termss[term]
        day -= 1
        if day == 0:
            day = 28
            month -= 1
        while month>12:
            month -=12
            year +=1
        if not valid(year, month, day, today):
            answer.append(index)

    return answer


print(solution(today, terms, privacies))