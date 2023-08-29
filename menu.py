import bisect

def find_position(number, array):
    index = bisect.bisect_left(array, number)
    return index

array = [0, 60, 120, 180, 240, 320]
number = 87

print(find_position(number, array))