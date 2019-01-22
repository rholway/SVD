import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def print_titles(topic, n):
    indx = np.argsort(topic)
    rv_indx = indx[::-1]
    for idx in pv.columns[rv_indx[:n]]:
        try:
            print(books.loc[idx]['Book-Title'] + " : " + books.loc[idx]['Book-Author'])
        except Exception:
            continue

if __name__ == '__main__':
    ratings = pd.read_csv('../../data/book_reviews.csv')
    # pivot out table
    pv = ratings.pivot(index='User-ID', columns='ISBN', values='Book-Rating').fillna(-1)
    # create three component matrices
    U,Sigma,VT = np.linalg.svd(pv.as_matrix())
    # create elbow plot to see explained variance
    plt.plot((Sigma ** 2)[:20])
    plt.savefig('../images/elbow_plot')
    # plot which number of components plot 90% of the explained variance
    cumulative = np.cumsum(Sigma ** 2)
    plt.plot(cumulative)
    plt.savefig('../images/cumsum')
    # find what that exact number is
    total_energy = np.sum(Sigma ** 2)
    threshold = total_energy * .9
    gt = cumulative > threshold
    indices = [i for i, v in enumerate(gt) if v == True]
    indices[0]
    # Looks like 441


    # Create latent topics for U and V matrix (books and users)
    V_5 = VT[:5,:]
    U_5 = U[:,:5]
    books = pd.read_csv('../../data/book_meta.csv', sep=';', error_bad_lines=False, encoding='latin-1')
    books = books.set_index('ISBN')

    for i in range(len(V_5)):
        print(f"Topic #{i} :")
        print("\n")
        print_titles(V_5[i], 5)
        print("\n")
