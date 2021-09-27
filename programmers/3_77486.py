# https://programmers.co.kr/learn/courses/30/lessons/77486
# 다단계 칫솔 판매

def solution(enrolls, referrals, sellers, amounts):
    referrals_of = {}

    for enroll, referral in zip(enrolls, referrals):
        referrals_of[enroll] = [enroll]
        if referral != '-':
            referrals_of[enroll].extend(referrals_of[referral])

    account = {enroll: 0 for enroll in enrolls}
    for seller, amount in zip(sellers, amounts):
        amount *= 100
        for referral in referrals_of[seller]:
            if amount == 0:
                break
            account[referral] += amount - int(0.1*amount)
            amount = int(0.1*amount)
    
    return list(account.values())

print(solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["young", "john", "tod", "emily", "mary"],
    [12, 4, 2, 5, 10]
))
