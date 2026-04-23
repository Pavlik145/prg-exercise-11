import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(seznam_cisel):
    numbers = seznam_cisel[:]
    count = 0
    for x in range(len(numbers)):
        minimalni = min(numbers[count:])
        idx = 0
        for i in range(count, len(numbers)):
            if numbers[i] == minimalni:
                idx = i
                break

        numbers[count], numbers[idx] = numbers[idx], numbers[count]
        count += 1

        # if numbers[count] > minimalni and idx > count:
        #
        #     count += 1
        # elif numbers[count] == minimalni:
        #     numbers[count+1], numbers[idx] = numbers[idx], numbers[count + 1]
        #     count +=

    return numbers

def bubble_sort(seznam):
    plt.ion()
    plt.show()
    copy_seznam = seznam[:]
    for x in range(len(copy_seznam)):
        for i in range(len(copy_seznam)-1):
            if copy_seznam[i] > copy_seznam[i+1]:
                copy_seznam[i],copy_seznam[i+1] = copy_seznam[i+1],copy_seznam[i]

                index_highlight1 = i
                index_highlight2 = i + 1
                colors = ["steelblue"] * len(copy_seznam)
                colors[index_highlight1] = "tomato"
                colors[index_highlight2] = "tomato"
                plt.clf()
                plt.bar(range(len(copy_seznam)), copy_seznam, color=colors)
                plt.title("Bubble Sort")
                plt.pause(0.1)

    plt.ioff()
    plt.show()

    return copy_seznam





if __name__ == "__main__":
    values = random_numbers(10)
    print(values)
    print(selection_sort(values))
    print(bubble_sort(values))