import pandas as pd
import matplotlib.pyplot as plt

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

pob = pd.read_csv('https://raw.githubusercontent.com/Ivancvz/platzi_courses/main/data.csv')
country = input('Ingresa el país: ').capitalize()
countries = list(pob['Country'])
a = countries.index(normalize(country))
pob_c = pob.loc[a]
 
def bar_chart(labels,values):
    fig, ax = plt.subplots()
    ax.bar(labels, values, width=0.5)
    ax.set_title('Population of '+country)
    plt.show()
    
if __name__ == '__main__':
    sent = pob_c[['2022 Population','2020 Population','2015 Population','2010 Population','2000 Population','1990 Population','1980 Population','1970 Population']]
    values = list(reversed(sent))
    sentence = ' '.join(dict(sent).keys())
    years = []
    for t in sentence.split():
        try:
            years.append(str(int(t)))
        except ValueError:
            pass
    labels = list(reversed(years))
    bar_chart(labels,values)