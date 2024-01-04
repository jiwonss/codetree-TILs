password = input()
rule = input()

rule_dict = {rule[i] : chr(i + 97) for i in range(26)}

for p in password:
    if p == ' ':
        print(p, end='')
    else:
        print(rule_dict[p], end='')