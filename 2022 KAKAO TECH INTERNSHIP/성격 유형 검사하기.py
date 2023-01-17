survey = ["TR", "RT", "TR"]	 #["AN", "CF", "MJ", "RT", "NA"]
choices = [7, 1, 3]	 #[5, 3, 2, 7, 5]
#result is "TCMA"

def change_num(num):
    if num == 1 or num == 7:
        return 3
    if num == 2 or num == 6:
        return 2
    if num == 3 or num == 5:
        return 1
    if num == 4:
        return 0

def solution(survey, choices):
    answer = ''
    n = len(survey)
    mbti = {"R": 0, "T": 0, "C": 0, "F":0, "J":0, "M":0, "A":0, "N":0}
    for i in range(n):
        left = survey[i][0]
        right = survey[i][1]
        if not left in mbti.keys():
            mbti[left]=0
            mbti[right]=0
        if choices[i]<4:
            mbti[left]+=change_num(choices[i])
        if choices[i]>4:
            mbti[right]+=change_num(choices[i])
    ll = ["RT","CF","JM","AN"]
    for word in ll:
        f = word[0]
        s = word[1]
        if mbti[s] > mbti[f]:
            answer += s
        else:
            answer += f
    return answer


print(solution(survey, choices))