# Mendel's First Law

# DOCUMENTATION:
#
# https://susannahgo.files.wordpress.com/2015/11/rosalind-iprb.pdf


from argparse import ArgumentParser

parser = ArgumentParser(description="name of the input file")
parser.add_argument(
    "-file", "--file_name", type=str, help="name of document with the example input"
)
args = parser.parse_args()


with open(f"./inputs/{args.file_name}", "r") as file:
    INPUT = list(map(int, file.read().strip().split()))
    # [0] -> k -> individuals are homozygous dominant for a factor
    # [1] -> m -> are heterozygous
    # [2] -> n -> are homozygous recessive.


def firts_law_medel(organisms: list = INPUT) -> float:
    population = sum(organisms)

    # k -> AA
    # m -> Ab
    # n -> bb

    return


def take_two(n):
    """Calcula la combinación de 2 elementos de un conjunto de n elementos."""
    return n * (n - 1) // 2

def main(input_str="2 2 2"):
    """Calcula la probabilidad de descendencia con un alelo dominante."""
    numbers = list(map(int, input_str.split()))  # Convierte la entrada en una lista de números
    total_pairs = take_two(sum(numbers))  # Combinaciones totales de parejas

    dominant_pairs = (
        take_two(numbers[0])  # Dos homocigotos dominantes
        + 3 / 4 * take_two(numbers[1])  # Dos heterocigotos
        + numbers[0] * numbers[1]  # Un homocigoto dominante y un heterocigoto
        + numbers[0] * numbers[2]  # Un homocigoto dominante y un homocigoto recesivo
        + 1 / 2 * numbers[1] * numbers[2]  # Un heterocigoto y un homocigoto recesivo
    )

    probability = dominant_pairs / total_pairs
    print(probability)

main()

# with open(f"./outputs/output_{args.file_name}", "w") as output_file:
#     output_file.write()
