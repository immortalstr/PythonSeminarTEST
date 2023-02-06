scores ={1: 'AEILNORSTUАВЕИНОРСТ',
          2: 'DGДКЛМПУ',
          3: 'BCMPБГЁЬЯ',
          4: 'FHVWYЙЫ',
          5: 'KЖЗХЦЧ',
          8: 'JXШЭЮ',
          10: 'QZФЩЪ'}
          
sum_score = 0
for letter in list(input().upper()):
    for key in scores.keys():
        if letter in scores[key]:
            sum_score += key
            break
print(sum_score)