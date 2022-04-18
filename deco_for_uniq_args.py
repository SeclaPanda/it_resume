class Answer:
    def RepeatDecorator(func):
        store = set()
        def wrapper(*args):
            if args in store:
                print('Функция с такими аргументами уже запускалась!')
            else:
                store.add(args)
        return wrapper