monikko = (
    "talvi", "talvi", "kevät",
    "kevät", "kevät", "kesä",
    "kesä", "kesä", "syksy",
    "syksy", "syksy", "talvi"
)

kuukausi = input("Syötä kuukausi: ")

print(monikko[int(kuukausi) - 1])