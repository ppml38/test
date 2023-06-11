import base64

file = open('cv.pdf', 'rb')
file_content = file.read()

with open("b64.txt","w") as f:
    f.write(base64.b64encode(file_content).decode("ascii"))
