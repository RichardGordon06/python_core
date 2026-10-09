class Doctor:
    def treat(self):
        return 'Я лечу людей'

class Patient():
    def __init__ (self, treatment_plan):
        self.treatment_plan = treatment_plan
        self.doctor = None

class Dantist(Doctor):
    def treat(self): #Специально переопределяем, как нужно в задании
        return 'Я лечу зубы людям'

class Surgeon(Doctor):
    def treat(self):
        return 'Я лечу людей хирургически'

class Therapist(Doctor):
    def treat(self):
        return 'А я лечу людям всё'

    def assign_doctor(self, patient):
    # Выбираем врача в зависимости от кода
        assigned_doctor = Therapist()
        if patient.treatment_plan == 1:
            assigned_doctor = Surgeon()
        elif patient.treatment_plan == 2:
            assigned_doctor = Dantist()
    # Сохраняем объект врача в атрибут пациента
        patient.doctor = assigned_doctor
    # Вызываем у назначенного врача метод treat()
        patient.doctor.treat()

# Вывод использования объектов
head_therapist = Therapist()
print("СЛУЧАЙ 1:")
patient_1 = Patient(treatment_plan=5)
head_therapist.assign_doctor(patient_1)
treat_1 = patient_1.doctor.treat()
print(f"Проверка: Пациенту назначен врач: {type(patient_1.doctor).__name__}, и он говорит: \"{treat_1}\"\n")

print("СЛУЧАЙ 2:")
patient_2 = Patient(treatment_plan=1)
head_therapist.assign_doctor(patient_2)
treat_2 = patient_2.doctor.treat()
print(f"Проверка: Пациенту назначен врач: {type(patient_2.doctor).__name__}, и он говорит: \"{treat_2}\"\n")

print("СЛУЧАЙ 3:")
patient_3 = Patient(treatment_plan=2)
head_therapist.assign_doctor(patient_3)
treat_3 = patient_3.doctor.treat()
print(f"Проверка: Пациенту назначен врач: {type(patient_3.doctor).__name__}, и он говорит: \"{treat_3}\"\n")