import pandas as pd


reviews = pd.read_csv("C:\\Users\\satvi\\Documents\\DDDM\\Project\\Review_Table.csv", encoding="latin")


def plot_pie_reviews(pos, neg):
    if pos == 0 and neg == 0:
        return
    import matplotlib.pyplot as plt
    labels = ['Positive', 'Negative']
    sizes = [pos, neg]
    colors = ['lightgreen', 'red']
    if pos > neg:
        explode = [0.1, 0]
    else:
        explode = [0, 0.1]
    plt.figure(1)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=150)
    plt.title('How people feel about this Issuer')
    plt.axis('equal')
    plt.show()


def plot_pie_expense_indicator(pos, neg):
    if pos == 0 and neg == 0:
        return
    import matplotlib.pyplot as plt
    labels = ['Affordable', 'Expensive']
    sizes = [pos, neg]
    colors = ['lightgreen', 'red']
    explode = [0, 0.1]
    plt.figure(2)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=120)
    plt.title('Expense indicator')
    plt.axis('equal')
    plt.show()

plot_pie_reviews(reviews['Pos_Count'][19], reviews['Neg_Count'][19])
plot_pie_expense_indicator(reviews['Low_Count'][19], reviews['High_Count'][19])