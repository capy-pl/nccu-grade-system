from django.test import TestCase, Client
from django.shortcuts import reverse

from apps.course.models import Course, ScoringSubject
from .utils import DUMMY_COURSES, DUMMY_SCORING_SUBJECTS, CourseDummyHandler, ScoringSubjectDummyHandler
from apps.staff.models import  Teacher
from apps.staff.utils import DUMMY_TEACHERS, TeacherDummyHandler

# Create your tests here.

class CourseModelTestCase(TestCase):
    def setUp(self):
        COURSE_INFO = [
            {   
                'course_number': 1234,
                'course_name': 'Economics',
                'description': 'This is a bad course',
            },
            {
                'course_number': 5678,
                'course_name': 'Manage Information System',
                'description': 'This is a bad course',
            },
            {
                'course_number': 4456,
                'course_name': 'Chinese Literature',
                'description': 'This is a bad course',
            },
            {
                'course_number': 8953,
                'course_name': 'Apple Economics',
                'description': 'This is a bad course',
            },
            {
                'course_number': 5983,
                'course_name': 'Bad Course',
                'description': 'This is a bad course',
            },
        ]
        for info in COURSE_INFO:
            Course.create(**info)

    def tearDown(self):
        pass

    def test_course_scoring_subject_removed(self):
        self.assertEqual(0 , 0, 'Assert zero is equal to zero')

class CourseOwnerPrivilegeCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up teacher.
        cls.teachers = TeacherDummyHandler().bulk_create(DUMMY_TEACHERS[:2])
        cls.teacher1 = cls.teachers[0]
        cls.teacher2 = cls.teachers[1]
        
        for index, COURSE in enumerate(DUMMY_COURSES):
            COURSE['teacher'] = cls.teachers[index % 2]
        
        cls.courses = CourseDummyHandler().bulk_create(DUMMY_COURSES)

    def test_course_detail(self):
        teacher1 = Client()
        teacher1.force_login(CourseOwnerPrivilegeCase.teacher1.user)
        teacher2 = Client()
        teacher2.force_login(CourseOwnerPrivilegeCase.teacher2.user)

        for index, course in enumerate(CourseOwnerPrivilegeCase.courses):
            if index % 2 == 0:
                res2 = teacher2.get(
                    reverse('course:detail', kwargs={'pk': course.pk}))
                self.assertEqual(res2.status_code, 403)
            else:
                res1 = teacher1.get(
                    reverse('course:detail', kwargs={'pk': course.pk}))
                self.assertEqual(res1.status_code, 403)

    def test_course_update(self):
        teacher1 = Client()
        teacher1.force_login(CourseOwnerPrivilegeCase.teacher1.user)
        teacher2 = Client()
        teacher2.force_login(CourseOwnerPrivilegeCase.teacher2.user)

        for index, course in enumerate(CourseOwnerPrivilegeCase.courses):
            if index % 2 == 0:
                res2 = teacher2.get(
                    reverse('course:update', kwargs={'pk': course.pk}))
                self.assertEqual(res2.status_code, 403)
            else:
                res1 = teacher1.get(
                    reverse('course:update', kwargs={'pk': course.pk}))
                self.assertEqual(res1.status_code, 403)    

    def test_course_delete(self):
        teacher1 = Client()
        teacher1.force_login(CourseOwnerPrivilegeCase.teacher1.user)
        teacher2 = Client()
        teacher2.force_login(CourseOwnerPrivilegeCase.teacher2.user)

        for index, course in enumerate(CourseOwnerPrivilegeCase.courses):
            res1 = teacher1.get(reverse('course:delete', kwargs={'pk': course.pk}))
            res2 = teacher2.get(reverse('course:delete', kwargs={'pk': course.pk}))
            # Only admin can delete the course.
            if index % 2 == 0:
                self.assertEqual(res1.status_code, 403)
                self.assertEqual(res2.status_code, 403)
            else:
                self.assertEqual(res1.status_code, 403)
                self.assertEqual(res2.status_code, 403)

    def test_get_subject_create_form(self):
        teacher1 = Client()
        teacher1.force_login(CourseOwnerPrivilegeCase.teacher1.user)
        teacher2 = Client()
        teacher2.force_login(CourseOwnerPrivilegeCase.teacher2.user)

        for index, course in enumerate(CourseOwnerPrivilegeCase.courses):
            if index % 2 == 0:
                res2 = teacher2.get(
                    reverse('course:subject_create', kwargs={'pk': course.pk}))
                self.assertEqual(res2.status_code, 403)
            else:
                res1 = teacher1.get(
                    reverse('course:subject_create', kwargs={'pk': course.pk}))
                self.assertEqual(res1.status_code, 403)

    @classmethod
    def tearDownClass(cls):
        for teacher in cls.teachers:
            teacher.delete()

        for course in cls.courses:
            course.delete()

class SubjectOwnerPrivilegeCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up teacher.
        cls.teachers = TeacherDummyHandler().bulk_create(DUMMY_TEACHERS[:2])

        cls.teacher1 = cls.teachers[0]
        cls.teacher2 = cls.teachers[1]
        
        for index, course in enumerate(DUMMY_COURSES):
            course['teacher'] = cls.teachers[index % 2]
        
        cls.courses = CourseDummyHandler().bulk_create(DUMMY_COURSES)
        
        for course in cls.courses:
            for subject in DUMMY_SCORING_SUBJECTS:
                course.add_new_subject(**subject)

    def test_subject_detail(self):
        teacher1 = Client()
        teacher1.force_login(SubjectOwnerPrivilegeCase.teacher1.user)
        teacher2 = Client()
        teacher2.force_login(SubjectOwnerPrivilegeCase.teacher2.user)

        for index, course in enumerate(SubjectOwnerPrivilegeCase.courses):
            for subject in course.scoringsubject_set.all():
                res1 = teacher1.get(
                    reverse('course:subject', kwargs={'pk': subject.pk}))
                res2 = teacher2.get(
                    reverse('course:subject', kwargs={'pk': subject.pk}))
                if index % 2 == 0:
                    self.assertEqual(res1.status_code, 200)
                    self.assertEqual(res2.status_code, 403)
                else:
                    self.assertEqual(res1.status_code, 403)
                    self.assertEqual(res2.status_code, 200)

    def test_subject_register(self):
        teacher1 = Client()
        teacher1.force_login(SubjectOwnerPrivilegeCase.teacher1.user)
        teacher2 = Client()
        teacher2.force_login(SubjectOwnerPrivilegeCase.teacher2.user)

        for index, course in enumerate(SubjectOwnerPrivilegeCase.courses):
            for subject in course.scoringsubject_set.all():
                if index % 2 == 0:
                    res2 = teacher2.get(
                        reverse('course:register', kwargs={'pk': subject.pk}))
                    self.assertEqual(res2.status_code, 403)
                else:
                    res1 = teacher1.get(
                        reverse('course:register', kwargs={'pk': subject.pk}))
                    self.assertEqual(res1.status_code, 403)

    def test_subject_score(self):
        teacher1 = Client()
        teacher1.force_login(SubjectOwnerPrivilegeCase.teacher1.user)
        teacher2 = Client()
        teacher2.force_login(SubjectOwnerPrivilegeCase.teacher2.user)

        for index, course in enumerate(SubjectOwnerPrivilegeCase.courses):
            for subject in course.scoringsubject_set.all():
                if index % 2 == 0:
                    res2 = teacher2.get(
                        reverse('course:subject_score', kwargs={'pk': subject.pk}))
                    self.assertEqual(res2.status_code, 403)
                else:
                    res1 = teacher1.get(
                        reverse('course:subject_score', kwargs={'pk': subject.pk}))
                    self.assertEqual(res1.status_code, 403)

    def test_subject_delete(self):
        teacher1 = Client()
        teacher1.force_login(SubjectOwnerPrivilegeCase.teacher1.user)
        teacher2 = Client()
        teacher2.force_login(SubjectOwnerPrivilegeCase.teacher2.user)

        for index, course in enumerate(SubjectOwnerPrivilegeCase.courses):
            for subject in course.scoringsubject_set.all():
                if index % 2 == 0:
                    res2 = teacher2.delete(
                        reverse('course:subject_delete', kwargs={
                                'pk': subject.pk }),
                        HTTP_ACCEPT='application/json'
                    )
                    self.assertEqual(res2.status_code, 403)
                else:
                    res1 = teacher1.delete(
                        reverse('course:subject_delete', kwargs={
                                'pk': subject.pk, }),
                        HTTP_ACCEPT='application/json'
                    )
                    self.assertEqual(res1.status_code, 403)
