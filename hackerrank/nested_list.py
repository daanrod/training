if __name__ == '__main__':
    names = []
    scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)

    sorted_zip = sorted(zip(scores, names), key=lambda x: x[0])
