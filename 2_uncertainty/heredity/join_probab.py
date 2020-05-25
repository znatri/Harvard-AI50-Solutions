# from heredity import PROBS

# def joint_probability(people, one_gene, two_genes, have_trait):
#     """
#     Compute and return a joint probability.

#     The probability returned should be the probability that
#         * everyone in set `one_gene` has one copy of the gene, and
#         * everyone in set `two_genes` has two copies of the gene, and
#         * everyone not in `one_gene` or `two_gene` does not have the gene, and
#         * everyone in set `have_trait` has the trait, and
#         * everyone not in set` have_trait` does not have the trait.
#     """
    
#     joint_probability = 0

#     for person in people:
#         genes = (
#             2 if person in two_genes else
#             1 if person in one_gene else
#             0
#         )
#         trait = person in have_trait
#         mother = person[person]["mother"]
#         father = person[person]["father"]

#         if mother is None and father is None:
#             joint_probability *= (PROBS["gene"][genes])
#         else:
#             passing_probability = {mother: 0, father: 0}
#             for parent in passing_probability:
#                 passing_probability[parent] = (
#                     1 - PROBS["mutation"] if parent in two_genes else
#                     0.5 if parent in one_gene else
#                     PROBS["mutation"]
#                 )

#             joint_probability *= (
#                 (passing_probability[mother] * passing_probability[father]) if genes == 2 else
#                 (passing_probability[mother] * (1 - passing_probability[father])) + (passing_probability[father] * (1 - passing_probability[mother])) if genes == 1 else
#                 (1 - passing_probability[mother]) * (1 - passing_probability[father])
#             )

#             # if genes == 2:
#             #     joint_probability *= (passing_probability[mother] * passing_probability[father])
#             # elif genes == 1:
#             #     joint_probability *= (passing_probability[mother] * (1 - passing_probability[father])) + (passing_probability[father] * (1 - passing_probability[mother]))
#             # else:
#             #     joint_probability *= (1 - passing_probability[mother]) * (1 - passing_probability[father])

#         joint_probability *= PROBS["trait"][genes][trait]

#     return joint_probability