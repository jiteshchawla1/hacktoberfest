import matplotlib.pyplot  as plt

def fnplot(list1):
     plt.plot(list1)
     plt.title("graph frequency using list")
     plt.xlabel("radiation")
     plt.ylabel("reaction")
     plt.show()
list1=[50,30,56,80,89,80]
fnplot(list1)
