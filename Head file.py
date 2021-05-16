import Field

    
size, quan = map(int, input().split())
field = Field.Field(size, quan)
field.matrix_done()
field.folder = f"Size {field.size}\\Variant with {field.queens} queens"
field.creat_folder()


location = f"J:\\Files\\Python\\Homeworks\\Queens\\Variations\\{field.folder}\\Positions.txt"
with open(location, "w") as letsdo:
    field.recursion(0, letsdo)
print("done")  