# from django.core.management.base import BaseCommand, CommandError
# from polls.models import Question as Poll
#
# class Command(BaseCommand):
#     help = 'Closes the specified poll for voting'
#
#     def add_arguments(self, parser):
#         parser.add_argument('args', nargs='*', type=int)
#
#     def handle(self, *args, **options):
#
#
#
#
# def insert_data(*args):
#     a
#     url = 'https://brainbooks.pk/api/subjectsjsonlist'
#     payload = {}
#     for each_class in range(1, 5):
#         payload['class_id'] = each_class
#         response = requests.post(url, data=payload)
#         if response.status_code == 200:
#             json_data = json.loads(response.text)
#             for data in json_data['data']:
#                 subject = Subject()
#                 if data.get('subject_id'):
#                     subject.subject_id = data['subject_id']
#                 if data.get('board_id'):
#                     board_obj, created = Board.objects.get_or_create(id=data['board_id'])
#                     subject.board = board_obj
#                 if data.get('class_id'):
#                     class_id = data['class_id']
#                     class_obj, created = Class.objects.get_or_create(name=class_id)
#                     subject.class_name = class_obj
#                 if data.get('subject'):
#                     subject.name = data['subject']
#                 if data.get('total_type_questions'):
#                     subject.total_type_questions = data['total_type_questions']
#                 try:
#                     subject.save()
#                 except Exception as e:
#                     print(e)