def rgb(r, g, b):
    code_Hex = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F');
    hexa = ''
    RGB = (r,g,b)
    for x in RGB:
        if x < 0:
            hexa = hexa + '00'
        elif x > 255:
            hexa = hexa + 'FF'
        else:
            resid = x % 16
            coci = int(x / 16)
            hexa = hexa + code_Hex[coci] + code_Hex[resid]
    return hexa