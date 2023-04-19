def breakingRecords(scores):
    # Write your code here
    max_sc, min_sc = scores[0], scores[0]
    max_ans, min_ans = 0,0
    
    for sc in scores :
        if sc > max_sc :
            max_sc = sc
            max_ans +=1
        if sc < min_sc :
            min_sc = sc
            min_ans +=1       
    
    return max_ans, min_ans