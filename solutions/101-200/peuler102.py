# Project Euler - 102
# Date: 18/07/2022'

def det(v1,v2):
    return v1[0]*v2[1]-v2[0]*v1[1]

def get_points(triangle):
    return triangle[:2],triangle[2:4],triangle[4:]

def sign(num):
    if num == abs(num):
        return "+"
    elif num == -abs(num):
        return "-"

def is_inbetween_vectors(v0,v1,v2):
    return sign(det(v1,v0)) == sign(det(v0,v2))

def is_O_in_triangle(triangle):
    points = get_points(triangle)
    a_0 = points[0]
    a_1 = [points[1][0]-points[0][0], points[1][1]-points[0][1]]
    a_2 = [points[2][0]-points[0][0], points[2][1]-points[0][1]]
    b_0 = points[1]
    b_1 = [points[0][0]-points[1][0], points[0][1]-points[1][1]]
    b_2 = [points[2][0]-points[1][0], points[2][1]-points[1][1]]
    c_0 = points[2]
    c_1 = [points[0][0]-points[2][0], points[0][1]-points[2][1]]
    c_2 = [points[1][0]-points[2][0], points[1][1]-points[2][1]]
    return is_inbetween_vectors(a_0,a_1,a_2) == is_inbetween_vectors(b_0,b_1,b_2) == is_inbetween_vectors(c_0,c_1,c_2) == True

if __name__ == "__main__":
    triangles = []

    with open("lib\\101-200\\peuler_resource102.txt","r") as file:
        for row in file:
            triangles.append(row[:-1].split(','))

    for i in range(len(triangles)):
        for j in range(len(triangles[i])):
            triangles[i][j] = int(triangles[i][j])
     
    c=0
    for tri in triangles:
        c+=int(is_O_in_triangle(tri))
    print(c)
