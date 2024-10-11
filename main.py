def polar_calculator() :
    import math
    YN = float(input( 'enter YN coordinate in metres :'))
    XC = float(input ('enter XC X coordinate in metres :'))
    D = float(input('enter distance in metres:'))
    B = float(input('enter direction in degrees:'))
    r = (B/180)*math.pi
    YO = YN + D*math.sin(r)
    XO = YN + D*math.cos(r)
    print(f"YO Y coordinate: {YO} m")
    print(f"XO X coordinate: {XO} m")
polar_calculator()