import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students_results.csv", sep=";", encoding="utf-8-sig")
df = df.fillna(0)

df["average"] = df[["algebra", "python", "ai"]].mean(axis=1)
df["status"] = df["average"].apply(lambda x: "PASS" if x >= 35 else "FAIL")


def show_all():
    print(df)


def best_student():
    best = df.loc[df["average"].idxmax()]
    print(best["name"], best["average"])


def weak_students():
    print(df[df["average"] < 35]["name"].tolist())


def subject_stats():
    for sub in ["algebra", "python", "ai"]:
        print("\n====================")
        print(sub.upper())
        print("====================")
        print("Average:", df[sub].mean())
        print("Max:", df[sub].max())
        print("Min:", df[sub].min())

        print("\nTop 3 students:")
        top = df.sort_values(sub, ascending=False)[["name", sub]].head(3)
        print(top.to_string(index=False))


def graph_hanr():
    plt.figure(figsize=(10, 5))
    plt.bar(df["name"], df["algebra"])
    plt.xticks(rotation=90)
    plt.title("Algebra")
    plt.tight_layout()
    plt.show()


def graph_python():
    plt.figure(figsize=(10, 5))
    plt.bar(df["name"], df["python"])
    plt.xticks(rotation=90)
    plt.title("Python")
    plt.tight_layout()
    plt.show()

la la la la la la
la
la la la


