import pandas as pd

In = []
Uit = []
df = pd.read_csv("", sep=";", decimal=",")
# print(df.columns)

df.set_index("Naam / Omschrijving", inplace=True)
# print(df)

bedrag = df[["Af Bij", "Bedrag (EUR)"]]
# print(bedrag)

uitgave = bedrag[bedrag["Af Bij"] == "Af"]
print(uitgave)
Bedrag_uit = uitgave["Bedrag (EUR)"].iloc[:]
for i in Bedrag_uit:
    Uit.append(float(i))
    totale_uitgave = (sum(Uit))
print(f"Totale uitgave: {totale_uitgave}")

inkomsten = bedrag[bedrag["Af Bij"] == "Bij"]
print(inkomsten)
Bedrag_in = inkomsten["Bedrag (EUR)"].iloc[:]
for i in Bedrag_in:
    In.append(float(i))
    totale_inkomsten = (sum(In))
print(f"Totale inkomsten: {totale_inkomsten}")
