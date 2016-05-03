import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    stack = [ tmp ]
    points = []
    screen = new_screen()
        
    for command in commands:
        print command
        if command[0]=='push':
            #push
            mpush(stack)
        elif command[0]=='pop':
            #pop
            stack.pop()
        elif command[0]=='move':
            #move
            t=make_translate(command[1], command[2], command[3])
            matrix_mult(stack[-1], t)
            stack[-1]=t
        elif command[0]=='rotate':
            #rotate
            angle=command[2]*(math.pi / 180)
            if command[1]=='x':
                r=make_rotX(angle)
            elif command[1]=='y':
                r=make_rotY(angle)
            elif command[1]=='z':
                r=make_rotZ(angle)
            matrix_mult(stack[-1], r)
            stack[-1]=r
        elif command[0]=='scale':
            #scale
            print 'scale'
            s=make_scale(command[1], command[2], command[3])
            matrix_mult(stack[-1], s)
            stack[-1]=s
        elif command[0]=='box':
            #box
            add_box(points, command[1], command[2], command[3], command[4], command[5], command[6])
            matrix_mult(stack[-1], points)
            draw_polygons(points, screen, color)
            points=[]
        elif command[0]=='sphere':
            #sphere
            add_sphere(points, command[1], command[2], command[3], command[4], 5)
            matrix_mult(stack[-1], points)
            draw_polygons(points, screen, color)
            points=[]
        elif command[0]=='torus':
            #torus
            add_torus(points, command[1], command[2], command[3], command[4], command[5], 5)
            matrix_mult(stack[-1], points)
            draw_polygons(points, screen, color)
            points=[]
        elif command[0]=='line':
            #line
            print 'line'
            add_edge(points, command[1], command[2], command[3], command[4], command[5], command[6])
            matrix_mult(stack[-1], points)
            draw_lines(points, screen, color)
            points=[]
        elif command[0]=='save':
            #save
            print 'save'
            save_extension(screen, command[1])
        elif command[0]=='display':
            #display
            display(screen)
            
