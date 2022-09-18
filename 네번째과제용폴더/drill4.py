import turtle

count = 6
a=200
b=200
turtle.penup()
turtle.goto(a,b)
turtle.right(90)
while(count>0):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()    
    a=a+100
    turtle.goto(a,b)   
    count-=1

count = 6
turtle.left(90)
a=200
turtle.goto(200,200)
while(count>0):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()    
    b=b-100
    turtle.goto(a,b)   
    count-=1


    
