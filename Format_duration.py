def format_duration(seconds):
    if seconds != 0:
        time = dict(second = seconds)
        x = 0
        y = 0
        if seconds >= 60:
            time['second'] = y = int(seconds % 60)
            time['minute'] = x = int(seconds / 60)
            if x >= 60:
                y = x
                time['minute'] = y = y % 60
                time['hour']   = x = int(x / 60)
                if x >= 24:
                    y = x
                    time['hour'] = y = y % 24
                    time['day']  = x = int(x / 24)
                    if x >= 365:
                        y = x
                        time['day']  = y = y % 365
                        time['year'] = x = int(x / 365)
        result = []
        for k in time.keys():
            v = time[k]
            if v > 0:
                if v == 1:
                    result.append('1 ' + k)
                else:
                    result.append(str(v) +' '+ k + 's')
        result = result[::-1]
        if len(result) > 1:
            result = ', '.join(result[0:-1]) + " and "+ result[-1]
        else:
            result = ''.join(result)
    else:
        result = 'now'
    return result