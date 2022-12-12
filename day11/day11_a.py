"""
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
...
"""

from collections import namedtuple

Monkey = namedtuple("Monkey", "id items operation test")

def parse_monkey(id, items, operation, test, test_true, test_false):
    id = id.split(" ")[1].strip(":")
    items = [int(i) for i in items.split(': ')[1].split(",")]
    operation = operation.split("new = ")[1].strip()
    def do_operation(old):
        eval_operation = operation.replace("old", str(old))
        new = eval(eval_operation)
        return new // 3
    test = test.split("divisible by ")[1].strip()
    test_true = int(test_true.split("throw to monkey ")[1])
    test_false = int(test_false.split("throw to monkey ")[1])
    def test_func(old):
        if not old % int(test):
            return test_true
        return test_false
    return Monkey(id, items, do_operation, test_func)

if __name__ == "__main__":
    data = [[i.strip() for i in monkey.split("\n")] for monkey in open("input.txt").read().split("\n\n")]
    monkeys = [parse_monkey(*monkey) for monkey in data]
    inspections = {monkey.id: 0 for monkey in monkeys}
    for round in range(20):
        print("Round", round)
        for monkey in monkeys:
            print("Monkey", monkey.id)
            for index, item in enumerate(monkey.items):
                print("Item", item, "=>", monkey.operation(item), "=>", monkey.test(monkey.operation(item)))
                item = monkey.operation(item)
                monkeys[monkey.test(item)].items.append(item)
                inspections[monkey.id] += 1
            monkey.items.clear()

    sorted_inspection = sorted((v for v in inspections.values()), reverse=True)
    print("Inspections:", sorted_inspection)
    print(sorted_inspection[0] * sorted_inspection[1])