import matplotlib.pyplot as plt

x = [1,5,10,15,20,25,30,35,40,45,50]
y = [0.000091,0.000189,0.000289,0.000429,0.000498,0.00159,0.00444,0.00470,0.00537,0.00672,0.008822]

plt.plot(x, y, '-o')

plt.xlabel('Threads')
plt.ylabel('Time (s)')
plt.title('Conway Game Threads ')
plt.legend()

plt.show()