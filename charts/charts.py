import matplotlib.pyplot as plt

def pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 300, 120]

    fig, ax =plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()