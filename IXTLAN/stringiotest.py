import io

input = """problem_description.png: {An infographic showing two clusters of points in a 3D space, labeled 'X' and 'Y', with arrows indicating movement from cluster X to Y, representing the concept of rotating and moving a solid object from one position to another. The style should be clear, with a scientific and instructional look, suitable for a mathematical presentation.}

model_description.png: {A conceptual diagram illustrating two matrices, labeled 'X' and 'Y', each containing points as columns within a grid structure. Include a notation describing an orthogonal transformation equation 'Y = QX + b', highlighting 'Q' as a rotation matrix and 'b' as a translation vector. The style should be educational, with a focus on clarity and precision for a mathematical audience.}

naive_solution.png: {A graphic depicting the process of applying a naive solution for transforming points from one cluster to another. Showcase an initial set of points, a transformation process with intermediary steps labeled 'linear least squares method', and a resulting set of points. The representation should be schematic, emphasizing the method's logical flow, suitable for explaining mathematical concepts to a professional audience.}

kabsch_algorithm.png: {A visual representation of the Kabsch algorithm in action, demonstrating the calculation of rotation matrix 'Q' from two sets of points labeled 'X' and 'Y'. Include the steps of centering the points, calculating covariance matrix, and finding the singular value decomposition. Style should be informative and precise, aiming to elucidate complex computational steps to a scientific audience.}

comparing_results.png: {A side-by-side comparison of the results of the naive solution and the Kabsch algorithm for transforming a set of points from an initial to a final position. Highlight the efficiency and accuracy differences between the two methods with examples of point transformations. The visual style should be comparative and analytical, making it easy to discern the advantages of each method for an educational or professional presentation.}"""

buff = io.StringIO(input)

for line in buff:
    print(line)