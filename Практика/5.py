class Queue(list):
    def front(self):
        elem = self.pop(0)
        return f'Ушел из очереди: {elem}. В очереди: {", ".join(self)}'

    def get_info(self):
        return f'В очереди {len(self)} человек: {", ".join(self)}. Следующий в очереди: {self[0]}'


lst = Queue()
for _ in range(int(input())):
    lst.append(input())
print(lst.front())
print(lst.front())
print(lst.get_info())
