def parse_int(string):
    string = string.split()[::-1]
    
    def ident(deci):
        num = {'zero': 0, 'one': 1, 'tw': 2, 'th': 3, 'fo': 4,
               'fi': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
               'ten': 10, 'eleven': 11, 'twelve': 12}
        num_k = num.keys()
        for n in num_k:
            if n in deci:
                return num[n]
        return None
    
    print(string)
    sum = 0
    carrion = 1
    for x in string:
        if (x == 'hundred') & (sum < 1000):
            carrion = 100
        elif (x == 'hundred') & (sum > 1000):
            carrion = 100000
        elif x == 'thousand':
            carrion = 1000
            
        print(carrion)
        if '-' in x:
            print('-')
            dec = x.split('-')
            sum += (ident(dec[0]) * 10 + ident(dec[1])) * carrion
            carrion = 1
        elif 'teen' in x:
            print('teen')
            sum += (ident(x) + 10) * carrion
            carrion = 1
        elif 'ty' in x:
            print('ty')
            sum += (ident(x) * 10) * carrion
            carrion = 1
        elif ident(x):
            print('solo')
            sum += ident(x) * carrion
            carrion = 1
        
        print(sum)
    return sum