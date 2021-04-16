def root_ex(a,b,c):

    r1 = (-b + ( b**2 - 4 * a * c)**(1/2)) / (2 * a) 
    r2 = (-b - ( b**2 - 4 * a * c)**(1/2)) / (2 * a) 
    return r1,r2

print('해는',root_ex(1,2,-8))