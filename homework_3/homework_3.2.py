test_cases = ["Login",
              "Registration",
              "Checkout",
              "Logout"]
statuses = ["PASS",
            "FAIL",
            "PASS",
            "SKIP"]

def print_report(test_cases, statuses):
   tests = dict(zip(test_cases, statuses))
   total_count = len(statuses)
   count_pass = statuses.count('PASS')
   count_fail = statuses.count('FAIL')
   print('Всего тестов:', total_count)
   print('Из них неуспешных:', count_fail)
   print('Из них успешных:', count_pass)
   print(tests)
   if int(count_fail) >= 1:
       print('Тестовый прогон выполнен с ошибками, исправьте их в упавших тестах и попробуйте снова')
   else:
       print('Тестовый прогон успешно выполнен')

print_report(test_cases, statuses)