def solution(n, arr1, arr2):
    bin1 = []
    bin2 = []
    for i in arr1:
        bin1.append(format(i, 'b'))
    for i in arr2:
        bin2.append(format(i, 'b'))
    
    bin3 = []
    bin4 = []
    for i in bin1:
        if len(i) < n:
                for j in range(n - len(i)):
                    i = '0' + i
        bin3.append(i)     
        
    for i in bin2:
        if len(i) < n:
                for j in range(n - len(i)):
                    i = '0' + i
        bin4.append(i) 
    
    final = []
    for i,j in zip(bin3, bin4):
        fin = ''
        for k in range(len(i)):
            if(i[k] == '0' and j[k] == '0'):
                fin += ' '
            else:
                fin += '#'
        final.append(fin)

    return final