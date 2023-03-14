infos = input("").strip().split(" ")
[competitors_quantity, purchased_paper_quantity, paper_quantity_per_competitor] = [int(item) for item in infos]
print("S" if competitors_quantity * paper_quantity_per_competitor <= purchased_paper_quantity else "N")