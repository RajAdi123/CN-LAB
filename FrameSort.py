import random
def sort(frames):
    l = len(frames)
    flag = 0
    for i in range(0, l):
        for j in range(0, l-i-1):
            if int(frames[j][0]) > int(frames[j+1][0]):
                flag = 1
                frames[j], frames[j+1] = frames[j+1], frames[j]
        if flag == 0:
            break
frames = []
n = int(input("Enter no. of frames "))
for i in range(n):
    frame = random.randint(1, n*100)
    data = input("Enter the Data for no. for frame "+str(frame)+": ")
    frames.append([frame, data])
sort(frames)
print("\nFrames after Sorting")
for frame in frames:
    print(str(frame[0])+"---"+str(frame[1]))