import matplotlib.pyplot as plt

def generate_barchart():
    labels = ['a','b', 'c']
    values = [100,200,80]
    fig, ax = plt.subplots(labels,values)
    ax.bar()
    plt.show()

if __name__ == '__main__':
    generate_barchart()
    
names = {'Nicolas', 'Miguel', 'Juan', 'Nicolas'} 
print(names) 