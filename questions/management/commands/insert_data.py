import json
import requests
from django.core.management.base import BaseCommand, CommandError
from questions.models import Board, Class, Subject, Chapter, Topic
from questions.choices import BOARD_CHOICES, CLASS_CHOICES, PUNJAB

class Command(BaseCommand):
    help = 'Inserts the relevant models data scraped from brainbooks.pk'

    def add_arguments(self, parser):
        parser.add_argument('args', nargs='*', type=str)

    def handle(self, *args, **options):
        insert_data(*args)



def insert_data(*args):
    args = list(args)

    payload = {}

    headers={
            "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }

    def json_response(url, payload):
        try:
            response = requests.post(url, data=payload, headers=headers)
            if response.status_code == 200:
                return json.loads(response.text)

        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)

    if 'boards' in args:
        for board in dict(BOARD_CHOICES).keys():
            board_obj, created = Board.objects.get_or_create(name=board,id=board)
            if created:
                print("Created board with id:{}".format(board))
            else:
                print("Board already exists")

    if 'classes' in args:
        board_obj, created = Board.objects.get_or_create(name=PUNJAB)
        for key,value in dict(CLASS_CHOICES).items():
            obj, created = Class.objects.get_or_create(name=key,board=board_obj,id=key)
            if created:
                print("Class Object created with class {} created successfully.".format(key))
            else:
                print("Class Object already exists")

    if 'subjects' in args:
        url = 'https://brainbooks.pk/api/subjectsjsonlist'
        for each_class in range(1, 5):
            payload['class_id'] = each_class
            json_data = json_response(url, payload)
            for data in json_data['data']:
                subject = Subject()
                if data.get('subject_id'):
                    subject.subject_id = data['subject_id']
                if data.get('board_id'):
                    board_obj, created = Board.objects.get_or_create(id=data['board_id'])
                    subject.board = board_obj
                if data.get('class_id'):
                    class_id = data['class_id']
                    class_obj, created = Class.objects.get_or_create(name=class_id)
                    subject.class_name = class_obj
                if data.get('subject'):
                    subject.name = data['subject']
                if data.get('total_type_questions'):
                    subject.total_type_questions = data['total_type_questions']
                try:
                    subject.save()
                except Exception as e:
                    print(e)

    if 'chapters' in args:
        url = 'https://brainbooks.pk/api/chapterjsonlistwithtopic'
        subject_ids = Subject.objects.values('subject_id')
        for subject_id in subject_ids:
            payload['subject_id'] = subject_id['subject_id']
            payload['question_status'] = 2
            json_data = json_response(url, payload)
            if json_data.get('data'):
                for data in json_data['data']:
                    chapter = Chapter()
                    if data.get('ch_id'):
                        chapter.chapter_id = data['ch_id']
                    if data.get('subject_id'):
                        subject_obj, created = Subject.objects.get_or_create(subject_id=data['subject_id'])
                        chapter.subject = subject_obj
                    if data.get('board_id'):
                        board_obj, created = Board.objects.get_or_create(id=data['board_id'])
                        chapter.board = board_obj
                        chapter.board_id = data['board_id']
                    if data.get('class_id'):
                        # chapter.class_name_id = data['class_id']
                        class_id = data['class_id']
                        class_obj, created = Class.objects.get_or_create(name=class_id)
                        chapter.class_name = class_obj
                    if data.get('chapter'):
                        chapter.chapter = int(data['chapter'])
                    if data.get('title'):
                        chapter.title = data['title']
                    try:
                        chapter.save()
                    except Exception as e:
                        print(e)

    if 'topics' in args:
        url = 'https://brainbooks.pk/api/chapterjsonlistwithtopic'
        subject_ids = Subject.objects.values('subject_id')
        for subject_id in subject_ids[::-1]:
            payload['subject_id'] = subject_id['subject_id']
            payload['question_status'] = 2
            json_data = json_response(url, payload)
            if json_data.get('data'):
                for data in json_data['data']:
                    topic = Topic()
                    if data.get('board_id'):
                        board_obj, created = Board.objects.get_or_create(id=int(data['board_id']))
                        topic.board = board_obj
                    if data.get('class_id'):
                        class_obj, created = Class.objects.get_or_create(id=int(data['class_id']))
                        topic.class_name = class_obj
                    if data.get('subject_id'):
                        subject_obj, created = Subject.objects.get_or_create(subject_id=int(data['subject_id']))
                        topic.subject = subject_obj
                    if data.get('chapter_id'):
                        chapter_obj, created = Chapter.objects.get_or_create(chapter=int(data['ch_id']))
                        topic.chapter = chapter_obj

                    if data.get('topics'):
                        topics = data['topics']
                        for tp in topics:
                            if tp.get('topic_id'):
                                topic.topic_id = int(tp['topic_id'])
                            if tp.get('topic'):
                                topic.topic = tp['topic']
                            if tp.get('title'):
                                topic.title = tp['title']

                            try:
                                topic.save()
                                print("Created successfully")
                            except Exception as e:
                                print("Already exists")
                                print(e)