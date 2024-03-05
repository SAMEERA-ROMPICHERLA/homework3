
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Agglomerative hierarchical clustering gradually groups data points together based on their similarity, while k-means assigns each data point to the nearest cluster center. However, if there are outliers present, k-means might not produce accurate results because it tends to be influenced by them."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means clustering generates different outcomes because of the random selection of initial centroids, while Agglomerative hierarchical clustering consistently produces the same result every time since it follows a deterministic approach."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "While K-means is known for its efficiency in terms of time and memory compared to agglomerative hierarchical clustering, it's important to note that there are other clustering algorithms available. For instance, the leader algorithm presents an alternative approach to clustering."

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "Splitting reduces the sum of squared errors by introducing two centroids for the same dataset, which results in a decrease in the distance to the nearest centroids."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "The sum of squared errors (SSE) serves as an indicator of cluster cohesion, with lower SSE values indicating higher cohesion, and vice versa."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "In the context of k-means clustering, the sum of squares between (SSB) is a metric that quantifies the degree of separation between clusters. Consequently, an increase in SSB corresponds to an increase in cluster separation, and conversely, a decrease in SSB indicates reduced separation between clusters."

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "In k-means clustering, cohesion and separation are independent of each other, meaning that enhancing cohesion does not necessarily lead to improvements in separation, and vice versa."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "In k-means clustering, the total sum of squares (TSS) comprises the sum of the sum of squared errors (SSE) and the sum of squares between (SSB). Additionally, TSS remains constant throughout the k-means clustering process."

    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "The sum of squares between (SSB) quantifies cluster separation, while the sum of squared errors (SSE) serves as an inverse measure of cluster cohesion. Therefore, as cohesion increases and SSE decreases, separation (SSB) also increases."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "As illustrated in the figure, the clusters are situated at a considerable distance from their centroids, making it unlikely for points to be drawn from other clusters towards them."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Given the proximity of the shaded regions, as depicted in the figure, it is anticipated that the clusters will include points from both of these regions."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The centroid at 12.5 is significantly distant from all points, potentially resulting in all other clusters becoming empty."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "(R^2)*4"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4*((a*a) + (b*b) + (c*c))"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "4*((R^2) + ((R/2)^2))"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 0

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Because clusters A and B contain an equal number of points (100 points each), one centroid will be drawn towards cluster A. Consequently, the right side of cluster B (comprising 2/3rd of the portion) will now host the remaining two centroids. On the other hand, despite its initial absence, cluster C, with its significantly larger number of points (100,000 points), ensures the retention of a centroid due to its stronger gravitational pull. Additionally, the even distribution of points in clusters A and B implies that each cluster should attract a centroid owing to their comparable influence."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The centroid will remain at cluster A because of the existing points within A and the absence of a stronger gravitational pull. The stronger pull exerted by cluster C will attract one centroid from cluster B. As a result, each of the three circles will host one centroid, ensuring an equal distribution."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Since circles A and B are closely situated but distanced from circle C, the points from both A and B will likely be assigned to the centroid in A. Meanwhile, the points in circle C will be split between two centroids, each managing 50,000 points. Due to A and B having an equal number of points, the centroid in A will oscillate between the two circles. While the centroids in circle C may move slightly apart, they will still predominantly remain within C, each managing half of the total points."

    return answers

# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {'Group A', 'Group B'}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Group A and B may be combined because the smallest single-link distance is observed between the rightmost point of A and the leftmost point of B."

    # type: set
    answers["(b)"] = {'Group A', 'Group C'}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Group A and C could potentially be merged because the smallest complete-link distance occurs between the rightmost point of A and the farthest point of C."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'B', 'C', 'E', 'F', 'I', 'J', 'L', 'M'}

    # type: set
    answers["(a) boundary"] = {'D', 'G'}

    # type: set
    answers["(a) noise"] = {'A', 'H'}

    # type: set
    answers["(b) cluster 1"] = {'B','C','D','E','F','G'}

    # type: set
    answers["(b) cluster 2"] = {'I','J','L','M'}

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {'I', 'G', 'J', 'E', 'M', 'B', 'L', 'F', 'D', 'C'}

    # type: set
    answers["(c)-a boundary"] = {'A', 'H'}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {'G', 'I', 'H', 'J', 'E', 'M', 'B', 'D', 'F', 'L', 'C'}

    # type: set
    answers["(c)-b cluster 2"] = {'A'}

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 exhibits the highest entropy as a result of a more evenly distributed presence of categories within it."

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 demonstrates low entropy because of its unequal distribution, with the majority of data points belonging to a single category, resulting in high homogeneity." 
    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "Two diagonal entries exhibit a deeper shade of blue and clearer boundaries compared to the other two, suggesting that clusters B and C demonstrate higher cohesion in comparison to clusters A and D."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "The first and third rows correspond to clusters A and C, respectively. This is evident from the distinct colors of the off-diagonal entries for these rows, indicating varying distances between clusters A (or C) and all other clusters. Specifically, cluster A is closest to C (blue off-diagonal), followed by B (green off-diagonal), and furthest from D (yellow off-diagonal). The same explanation applies to cluster C. The second row corresponds to cluster B, where the distances to A and C are identical (green off-diagonal), with the furthest distance from A indicated by the red entry. Lastly, row 4 corresponds to cluster D, where the distances from A and C are the same (yellow off-diagonal), but the furthest distance from B is represented by the red off-diagonal entry."

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "Two diagonal entries appear more vividly blue compared to the other two, suggesting that clusters B and C exhibit stronger cohesion than clusters A and D."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "1. Rows with less distinct diagonal entries (rows 1 and 4) exhibit a variety of colors, suggesting that all other clusters have different distances from these clusters. For example, Cluster A is closest to Cluster B, followed by Cluster C, and then Cluster D. No two clusters share the same distance to Cluster A. 2. Rows with more defined diagonal entries feature two identical colors (besides the diagonal), indicating that they have the same distance to two clusters and are the furthest from one cluster. For instance, Cluster B's distance to Clusters A and C is similar, but it is furthest from Cluster D."

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "Two diagonal entries appear more vividly blue and defined compared to the other two, suggesting that clusters B and C exhibit stronger cohesion than clusters A and D."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "In all rows, there are two off-diagonal entries with similar colors and one with a different color. This pattern indicates that each cluster has two other clusters that are relatively closer to it compared to the remaining one cluster. For example, Cluster B is similarly close to Clusters A and C compared to Cluster D."

    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "The diagonal entry appears less defined, suggesting that the cluster is less cohesive. Additionally, all off-diagonal entries have different colors, indicating that all other clusters have varying distances from it. Specifically, it is closest to Cluster B, followed by Cluster C, and furthest from Cluster A."
    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "The diagonal entry appears more defined, suggesting that the cluster is cohesive. Furthermore, 2 out of 3 off-diagonal entries have the same color, indicating that two other clusters (A and C) are closer to it. However, it is worth noting that the off-diagonal entry indicating distances with Cluster A is less defined. Lastly, the cluster is furthest from one other cluster (D)."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "The explanation mirrors that of row 2."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "The explanation follows a similar pattern as row 1 but in reverse order."

    return answers



# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['Hierarchical', 'Partial', 'Overlapping']

    # type: list
    answers["(b)"] = ['Partitional', 'Exclusive', 'Complete']

    # type: list
    answers["(c)"] = ['Partitional', 'fuzzy', 'complete']


    # type: list
    answers["(d)"] = ['Hierarchical', 'overlapping', 'partial']

    # type: list
    answers["(e)"] = ['Partitional', 'Exclusive', 'Complete']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Letter grades are unique categories that do not overlap. Furthermore, each student is assigned only one grade per class, ensuring that all students in the class receive a grade, without any exceptions."

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}
    
    # type: string
    answers["(a) Figure (a)"] = "No"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "DBSCAN can be applied to identify clusters corresponding to the patterns depicted by the nose, eyes, and mouth. It is suitable for detecting clusters in both low and high-density areas, as well as areas with irregular shapes."

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means is typically better suited for detecting clusters in datasets characterized by uniform density across clusters. However, it can still be effective in higher density areas if the clusters are compact and distinctly separated."

    # type: string
    answers["(c)"] = "I favor DBSCAN clustering because it is versatile enough to be applied in both high and low-density areas, and it can effectively handle datasets with irregular shapes."

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
