class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def scalene(self):
        l = [self.s1, self.s2, self.s3]
        return len(set(l)) == 3

    def isosceles(self):
        l = [self.s1, self.s2, self.s3]
        return len(set(l)) == 2

    def is_triangle(self):
        return self.s1+self.s2>self.s3 and self.s1+self.s3>self.s2 and self.s2+self.s3>self.s1

def IdentifyTriangle(lst):
    if lst is None:
        return -1

    scalene_count = 0
    isosceles_count = 0
    not_triangle_count = 0

    for triangle in lst:
        triangle = Triangle(triangle[0], triangle[1], triangle[2])
        if not triangle.is_triangle():
            not_triangle_count += 1
        elif triangle.scalene():
            scalene_count += 1
        elif triangle.isosceles():
            isosceles_count += 1

    return 3 * scalene_count - (isosceles_count + not_triangle_count)





# lst = list(input().split(','))
lst = eval(input())
print(lst)
result = IdentifyTriangle(lst)
print(result)

