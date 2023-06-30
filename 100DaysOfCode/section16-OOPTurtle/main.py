# from turtle import Turtle, Screen
#
# beca = Turtle()
# print(beca)
# beca.shape("turtle")
# beca.color("green")
# beca.forward(100)
# beca.circle(5)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Bulbasaur", "Squirtle", "Weedle"])
table.add_column("Type", ["Grass", "Water", "Bug"])

print(table.align)
table.align = "l"

print(table.junction_char)
table.junction_char = ">"

print(table)
# print(table.get_html_string())
