import matplotlib.pyplot as plt
import numpy as np
import csv


########################## TODO #########################

#convert list to numpy array and use numpy.savetxt()
# for better saving functionality

##########################################################

#Draws soccer pitch based on a matplot grid
def drawPitch():
    #circle = plt.Circle((0.0, 0.0), 9.15, color='white', fill=False)
    #ax.add_artist(circle)
    ax.axis([-55, 55, -35, 35])
    #ax.grid()
    #ax.set_facecolor('green')
    #plt.axvline(x=0, color='white')
    #plt.axvline(x=-52, color='white')
    #plt.axvline(x=52, color='white')
    #plt.axhline(y=34, color='white')
    #plt.axhline(y=-34, color='white')
    #plt.plot(0,0, 'o', color='white')
    im = plt.imread('field.png')
    ax.imshow(im, extent=[-55, 55, -35, 35], aspect='auto')

#Writes list a to data.csv file
def writeToCsv(myList):
    global a

    if(len(a) == 0):
        print('Error: List is empty - No formation recorded yet')

    elif(len(a[len(a)-1])==11):
        print('Writing data to csv file..')

        #np.savetxt('test.out', a, fmt='%.5f')
        with open('./data.csv', 'w') as myFile:
            wr = csv.writer(myFile, quoting=csv.QUOTE_ALL)
            wr.writerow(myList)
    else:
        print('Please specify 10 players and the formation first')

#Adds given formation (10 player coordinates + formation label) to the player positions
def markFormation(formation):
    global a
    global b

    if (len(b) == 10):

        a.append(b)
        a[len(a) - 1].append([formation])
        print('Formation ', formation, ' added \n', a)

        print('Generate 10 samples based on given formation and variance')
        variance = 3
        singleSet = []
        numberOfRandomDatapoints = 10


        for counter in range(0,numberOfRandomDatapoints):
            for i in range(0,10):
                singleSet.append([round(b[i][0] + np.random.uniform(variance*-1, variance),2), round(b[i][1] + np.random.uniform(variance*-1,variance),2)])
                if(len(singleSet) == 10):
                    singleSet.append([formation])
                    print('New datapoint: ', singleSet)
                    a.append(singleSet)
                    singleSet = []

        b = []
        clear()
    else:
        print('Input Error: make sure to specify 10 players and a formation type!')

#Reloads grid for new formation input
def clear():
    ax.clear()
    drawPitch()

#Draw soccer pitch
fig = plt.figure(figsize=(10,6))
fig.suptitle('Formation Data Generation', size='16')
ax = fig.add_subplot(111)

#Draw the pitch
drawPitch()

#Initialize arrays
a = []
b=[]

def onclick(event):
    if(event.xdata == None or event.ydata == None):
        print("Please click again in the grid")
    else:
        print('button=%d, xdata=%f, ydata=%f' % (event.button, event.xdata, event.ydata))

        if(len(b) < 10):
            plt.plot(event.xdata, event.ydata, 'o', color='black')
            fig.canvas.draw()
            b.append([round(event.xdata, 2), round(event.ydata, 2)])
            print(b)
            if(len(b) == 10):
                #a.append(b)
                print('10 players added, pleace specify formation')
        else:
            print('Only 10 players per formation required, please specify the formation type.')

def on_key(event):
    global a
    global b

    if(event.key == '1' or event.key == '2' or event.key == '3'):
        markFormation(float(event.key))

    elif(event.key == '4'):
        writeToCsv(a)

    elif (event.key == 'escape'):
        b=[]
        clear()

cid = fig.canvas.mpl_connect('button_press_event', onclick)
cid = fig.canvas.mpl_connect('key_press_event', on_key)

plt.show()

