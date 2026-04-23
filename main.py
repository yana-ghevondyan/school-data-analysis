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


def graph_algebra():
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


def graph_ai():
    plt.figure(figsize=(10, 5))
    plt.bar(df["name"], df["ai"])
    plt.xticks(rotation=90)
    plt.title("AI")
    plt.tight_layout()
    plt.show()


def menu():
    while True:
        print("\n1. all data")
        print("2. best student")
        print("3. weak students")
        print("4. subject stats + top 3")
        print("5. algebra graph")
        print("6. python graph")
        print("7. ai graph")
        print("0. exit")

        c = input("choose: ")

        if c == "1":
            show_all()
        elif c == "2":
            best_student()
        elif c == "3":
            weak_students()
        elif c == "4":
            subject_stats()
        elif c == "5":
            graph_algebra()
        elif c == "6":
            graph_python()
        elif c == "7":
            graph_ai()
        elif c == "0":
            break

menu()