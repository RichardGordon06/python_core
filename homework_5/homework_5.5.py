import json
from asyncio.windows_events import NULL
from functools import reduce

class InvalidTestStatusError(Exception):
    pass

def test_results():
    file_name = "test_data.json"
    report = 'report.json'
    correct_statuses = {"PASS", "FAIL", "SKIP"}

    try:
        with open(file_name, "r", encoding="utf-8") as file: #Чтение файла
            data = json.load(file)
            tests = data.get("tests", [])
            if tests:
                print('Проверка на список прошла успешно')
            else:
                raise KeyError(f'Список тестов несформировался, проверьте файл {file_name}')

            for test in tests: #Отлов некорректных статусов в файле данных
                if test.get("status") not in correct_statuses:
                    raise InvalidTestStatusError(
                        f"В файле обнаружен некорректный статус '{test.get('status')}' в тесте '{test.get('name')}'"
                    )
                elif test.get("name") is None or test.get("name") == '':
                    raise KeyError('В файле содержится некорректный параметр "name"')
                elif test.get("duration") is None or test.get("duration") == '':
                    raise KeyError('В файле содержится некорректный параметр "duration"')


            failed_tests = list(filter(lambda test: test["status"] == "FAIL", tests)) #Список упавших тестов
            failed_titles = list(map(lambda test: test["name"], failed_tests)) #Список с названиями упавших тестов
            total_tests = len(tests)

            total_duration = reduce(lambda total, test: total + test["duration"], tests, 0.0) #Общее время всех тестов
            duration_tests = [test["duration"] for test in tests] #Список таймингов тестов
            high_time = max(duration_tests)

            pass_count = sum(1 for test in tests if test["status"] == "PASS")
            fail_count = sum(1 for test in tests if test["status"] == "FAIL")
            skip_count = sum(1 for test in tests if test["status"] == "SKIP")

        print("--- Статистика автотестов ---")
        print(f'Общее количество тестов: {total_tests}')
        print(f"Количество FAIL: {fail_count}")
        print(f'Количество PASS: {pass_count}')
        print(f'Количество SKIP: {skip_count}')
        print(f"Названия упавших тестов (FAIL): {failed_titles}")
        print(f'Самый длительный тест имеет продолжительность: {high_time}')
        print("Общее время выполнения всех тестов:", int(total_duration), "сек.")
        print(f'\nДанные отчёта были записаны в отдельный файл: {report}')

        report_data = {
            "Общее количество тестов": total_tests,
            "Количество FAIL": fail_count,
            "Количество PASS": pass_count,
            "Количество SKIP": skip_count,
            "Названия упавших тестов (FAIL)": failed_titles,
            "Самый длительный тест имеет продолжительность": high_time,
            "Общее время выполнения всех тестов (сек.)": int(total_duration)
        }

        with open(report, "w", encoding="utf-8") as report_file: #Запись данных в файл, ensure чтобы кириллицу обрабатывал
            json.dump(report_data, report_file, ensure_ascii=False, indent=4)

    except FileNotFoundError: #Если файл не найден
        print(f"Ошибка: Файл '{file_name}' не найден. Убедитесь, что он лежит в той же папке.")

    # Обработка ошибки: файл не является валидным JSON
    except json.JSONDecodeError as e:
        print(f"Критическая ошибка: Невозможно прочитать содержимое как JSON. Подробности: {e}")

    except ValueError: #Некорректные параметры в json
        print(f'Некорректные данные в {file_name}. Не могу прочитать данные')

    except InvalidTestStatusError as e: #Ошибка в одном из статусов
        print(f"Неверно указан статус одного из тестов: {e}")

test_results()