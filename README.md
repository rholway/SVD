# Singular Value Decomposition

## Comparing Books and Users
For an assignment of ours, we used Singular Value decomposition (SVD) to deconstruct a feature matrix and perform a dimensionality reduction.

We looked at a data set of book reviews where each row corresponds to a given user's rating of a book.  There are approximately 6100 books and 2500 users. We utilized SVD using matrix decomposition in order to reduce the dimensionality of the matrix. Using numpy's SVD method, we get three component matrices (U, Sigma, and V).

By squaring the singular values (Sigma matrix), we can calculate the power.  The power is the variance of each dimension. Total power is the cumulative sum of the power of each singular value.

Here we plot the power of each singular value:
![Name of plot](images/elbow_plot.png)

We can see an 'elbow' at around one or two. Meaning the first or second singular values account for a majority of the variance in the data.  The latter singular values account for very little variance in the data.

Here we plot the cumulative sum of the singular values:
![Name of plot](images/cumsum.png)

By doing this, we can find out how many singular values we need to account for 90% of the variance in the data, which ends up being 441.

## Creating Latent Topics
We can create *n* latent topics by diving into the U and V matrices. We can find what books cluster in each topic.

When we created five latent topics, these are the books that cluster into each topic:

Topic 0:<br />
Name Der Rose : Umberto Eco<br />
Monsieur Ibrahim und die Blumen des Koran. : Eric-Emmanuel Schmitt<br />
Artemis Fowl. : Eoin Colfer<br />
Novocento, Un Monologo : Alessandro Baricco<br />
Schlafes Bruder : Robert Schneider<br />

Topic 1:<br />
The Red Tent (Bestselling Backlist) : Anita Diamant<br />
The Lovely Bones: A Novel : Alice Sebold<br />
The Da Vinci Code : Dan Brown<br />
Where the Heart Is (Oprah's Book Club (Paperback)) : Billie Letts<br />
Two for the Dough : Janet Evanovich<br />

Topic 2:<br />
Dance upon the Air (Three Sisters Island Trilogy) : Nora Roberts<br />
Face the Fire (Three Sisters Island Trilogy) : Nora Roberts<br />
Heart of the Sea (Irish Trilogy) : Nora Roberts<br />
Jewels of the Sun (Irish Trilogy) : Nora Roberts<br />
Key of Valor (Roberts, Nora. Key Trilogy, 3.) : Nora Roberts<br />

Topic 3:<br />
The Lovely Bones: A Novel : Alice Sebold<br />
The Red Tent (Bestselling Backlist) : Anita Diamant<br />
A Time to Kill : JOHN GRISHAM<br />
The Pilot's Wife : A Novel : Anita Shreve<br />

Topic 4:<br />
The Firm : John Grisham<br />
The Pelican Brief : John Grisham<br />
A Time to Kill : JOHN GRISHAM<br />
Silence of the Lambs : Thomas Harris<br />
The Chamber : John Grisham<br />

### By reducing the dimensionality of the data frame, it is less computationally expensive to run calculations.  It also makes it easier to compare different books to one another, and we can cluster similar books. 
