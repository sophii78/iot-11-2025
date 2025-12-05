from datetime import datetime


class Bug:
    _id_counter = 1

    def __init__(self, description, severity, deadline, status, assignee=None, bug_id=None):

        if bug_id is None:
            self.__id = Bug._id_counter
            Bug._id_counter += 1

        else:
            self.__id = bug_id if bug_id > Bug._id_counter else Bug._id_counter
            Bug._id_counter = max(Bug._id_counter, self.__id + 1)

        self.__description = description
        self.__severity = int(severity)
        self.__deadline = deadline
        self.__status = status
        self.__assignee = assignee
        print(
            f"Створено Bug(id={self.__id}, "
            f"severity={self.__severity}, status={self.__status})"
        )

    def __del__(self):
        print(f"Видаляється Bug(id={self.__id})")

    def get_id(self):
        return self.__id

    def get_description(self):
        return self.__description

    def set_description(self, value):
        self.__description = value

    def get_severity(self):
        return self.__severity

    def set_severity(self, value):
        self.__severity = int(value)

    def get_deadline(self):
        return self.__deadline

    def set_deadline(self, value):
        self.__deadline = value

    def get_status(self):
        return self.__status

    def set_status(self, value):
        self.__status = value

    def get_assignee(self):
        return self.__assignee

    def set_assignee(self, value):
        self.__assignee = value

    def __str__(self):
        dl = self.__deadline.strftime('%Y-%m-%d') if self.__deadline else 'None'
        return (f"Bug(id={self.__id}, desc='{self.__description}', severity={self.__severity}, "
                f"deadline={dl}, status={self.__status}, assignee={self.__assignee})")


class Backlog:
    def __init__(self):
        self.__bugs = []
        print("Порожній беклог створено")

    def __del__(self):
        print("Очищується список багів")
        self.__bugs.clear()

    def add_bug(self, bug):
        self.__bugs.append(bug)
        print(f"Додано {bug}")

    def bugs_resolved(self, assignee):
        result = [
            b for b in self.__bugs
            if (b.get_assignee() == assignee and b.get_status() == 'RESOLVED')
        ]
        print(
            f"Знайдено {len(result)} багів "
            f"для '{assignee}' зі статусом RESOLVED"
        )
        return result


    def sort_by_severity(self):
        self.__bugs.sort(key=lambda b: b.get_severity(), reverse=True)
        print("Беклог відсортований за severity (за спаданням)")


    def display_all(self):
        if not self.__bugs:
            print("Беклог порожній")
            return
        print("Вміст беклогу:")
        for b in self.__bugs:
            print('  -', b)


def main():

    bf = Backlog()

    b1 = Bug('Не відкриваються зображення на сайті', 5,
             datetime(2025, 10, 25), 'OPEN', 'Іван')

    b2 = Bug('Нема доступу до сервера', 2,
             datetime(2025, 11, 5), 'RESOLVED', 'Анна')

    b3 = Bug('Текст на кнопці обрізається', 4,
             None, 'IN_PROGRESS', 'Олег')

    b4 = Bug('Некоректний формат дати', 3,
             datetime(2025, 12, 1), 'RESOLVED', 'Іван')

    bf.add_bug(b1)
    bf.add_bug(b2)
    bf.add_bug(b3)
    bf.add_bug(b4)

    print('\n-- Весь беклог --')
    bf.display_all()

    print('\n-- Баги для Івана зі статусом RESOLVED --')
    resolved_ivan = bf.bugs_resolved('Іван')
    for bug in resolved_ivan:
        print(bug)

    print('\n-- Сортування беклогу за severity --')
    bf.sort_by_severity()
    bf.display_all()


if __name__ == '__main__':
    main()