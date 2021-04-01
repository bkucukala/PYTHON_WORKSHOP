def convert(milliseconds):
    hours_convert = 60*60*1000
    hours = milliseconds // hours_convert
    left = milliseconds % hours_convert
    minutes_convert = 60*1000
    minutes = left // minutes_convert
    left = left % minutes_convert
    seconds = left // 1000
    print (f'{hours} hour/s'* (hours != 0) + f' {minutes} minute/s'*(minutes != 0) +  f' {seconds} second/s' * (seconds != 0) 
    or f'just {milliseconds} millisecond/s' * (milliseconds < 1000))

milliseconds = int(input("Enter milliseconds  : "))
convert(milliseconds)