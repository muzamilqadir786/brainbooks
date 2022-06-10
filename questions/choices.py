PUNJAB = 1
SINDH = 2
KHYBER_PAKHTUNKHWA = 3
BLOCHISTAN = 4
BOARD_CHOICES = [
    (PUNJAB, 'Punjab'),
    (SINDH, 'Sindh'),
    (KHYBER_PAKHTUNKHWA, 'Khyber Pakhtunkhwa'),
    (BLOCHISTAN, 'Balochistan'),
]

NINTH = 1
TENTH = 2
FIRST_YEAR = 3
SECOND_YEAR = 4
CLASS_CHOICES = [
    (NINTH, 'Class-9'),
    (TENTH, 'Class-10'),
    (FIRST_YEAR, 'Inter Part-I'),
    (SECOND_YEAR, 'Inter Part-II'),
]

QUESTION_TYPES = (
    (1, 'MCQ'),
    (2, 'Short Question'),
    (3, 'Long Question'),
)

OPTION_A = 1
OPTION_B = 2
OPTION_C = 3
OPTION_D = 4

ANSWER_OPTIONS=(
    (OPTION_A,'Option1'),
    (OPTION_B,'Option2'),
    (OPTION_C,'Option3'),
    (OPTION_D,'Option4')
)