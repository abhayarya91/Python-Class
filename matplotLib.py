# import matplotlib.pyplot as plt
# import numpy
# from matplotlib import pyplot as plt
# # from matplotlib.pyplot as plt
# import matplotlib.pyplot as plt
# ax= plt.subplots()
# plt.pie([2,5,9,],[4,6,8])
# # plt.bar([2,5,9,],[4,6,8])
# plt.show()

# # # #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 2D matplotlib  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # # import matplotlib.pyplot as plt
# # from matplotlib import pyplot as plt
# # # from matplotlib.pyplot as plt
# # # import matplotlib.pyplot as plt
# # plt.plot([2,5,9,],[4,6,8])
# # plt.title("this is first graph")
# # plt.xlabel("this is x Axis")
# # plt.ylabel("this is y Axis")
# # plt.show()
# # ###########################################################################################################
# import matplotlib.pyplot as plt
# x= [16,8,20]
# y=[4,8,9]
# x2= [3,7,9]
# y2=[9,5,8]
# plt.plot(x,y)
# plt.plot(x2,y2)
# plt.title("this is 2nd graph")
# plt.xlabel("ths is x and x2")
# plt.ylabel("this is y and y2")
# plt.show()




# # #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Multi plots >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # import matplotlib.pyplot as plt
# # fig, ax= plt.subplots(2,2)
# # ax[0,0].plot([7,8,9,4,5],[6,1,2,3,0])
# # ax[0,1].plot([7,8,9,4,5],[6,1,2,3,0])
# # ax[1,0].plot([7,8,9,4,5],[6,1,2,3,0])
# # ax[1,1].plot([7,8,9,4,5],[6,1,2,3,0])
# # plt.show()



# # #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 3D matplotlib >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # import matplotlib.pyplot as plt
# # import numpy as np
# # fig = plt.figure()
# # ax = plt.axes(projection="3d")


# # #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> bar  matplotlib >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# import matplotlib.pyplot as plt
# import numpy as np

# arr1 = np.array([56,46,75,49,85,])
# arr2 = np.array(["OPPS","linux","python","physics","lab"])
# plt.bar(arr1,arr1)
# plt.title("students graph")
# plt.ylabel("marks")
# plt.xlabel("subjects")
# plt.show()


# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(2,2)
# # ax[0,0].bar([7,8,9,4,5],[6,1,2,3,0])
# # ax[0,1].bar([7,8,9,4,5],[6,1,2,3,0])
# # ax[1,0].bar([7,8,9,4,5],[6,1,2,3,0])
# # ax[1,1].bar([7,8,9,4,5],[6,1,2,3,0])
# # plt.show()
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(2,2)
# ax[0,0].plot([7,8,9,4,5],[6,1,2,3,0])
# ax[0,1].plot([7,8,9,4,5],[6,1,2,3,0])
# ax[1,0].plot([7,8,9,4,5],[6,1,2,3,0])
# ax[1,1].plot([7,8,9,4,5],[6,1,2,3,0])
# plt.show()






import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(0, 10, 100)
y = np.sin(x)
y2 = np.cos(x)

# 1. Line Chart
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Sine Wave')
plt.plot(x, y2, label='Cosine Wave')
plt.title('Line Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()

# 2. Bar Chart
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

plt.figure(figsize=(10, 6))
plt.bar(categories, values, color='skyblue')
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# 3. Scatter Plot
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)

plt.figure(figsize=(10, 6))
plt.scatter(x_scatter, y_scatter, color='green', marker='o')
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# 4. Histogram
data = np.random.randn(1000)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='purple', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
