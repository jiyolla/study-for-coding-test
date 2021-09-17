import re

exp = input().lstrip('0')
refined_exp = re.sub(r'\D0+\d', lambda x: x.group(0)[:-1].replace('0', '') + x.group(0)[-1], exp)
terms = refined_exp.split('-')

v = []
if(len(terms) == 1):
    print(eval(terms[0]))
else:
    for i in terms[1:]:
        v.append(eval(i))
    res = eval(terms[0]) - sum(v)
    print(res)
