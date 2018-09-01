from django.test import TestCase,TransactionTestCase
from django.utils import timezone
from django.test import Client
import datetime

from .models import Question
from django.urls import reverse
# Create your tests here.

class QuestionModelTests(TestCase):
    """
    """
    def test_was_published_recently_with_future_question(self):
        """
        """
        #在当前时间的基础上加上30天
        time = timezone.now() + datetime.timedelta(days=30)
        #创建一个来自未来的问题对象
        future_question = Question(pub_date=time)
        #断言
        self.assertIs(future_question.was_published_recently(),False)

    def test_was_published_recently_with_old_question(self):
        """
        """
        #应该把timedelta看成一个绝对值，它是时间轴上一段长度的线段
        #也就是说如果往过去偏移、等同于在当前时间点上减去某一时间长度
        time = timezone.now() - datetime.timedelta(days=1,seconds=1)
        #一个来自24小时之前的问题
        old_question = Question(pub_date=time)
        #断言
        self.assertIs(old_question.was_published_recently(),False)

    def test_was_published_recently_with_recent_question(self):
        """
        """
        #增加一个时间点落在24小时内的Question对象
        time = timezone.now() - datetime.timedelta(hours=23,minutes=59,seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(),True)


def create_question(question_text,days):
    """创建Question对象
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,pub_date=time)


class QuestionIndexViewTests(TransactionTestCase):
    """
    """
    def test_with_no_questions(self):
        """
        """
        #注意TestCase自带Client对象、可以通过self.client方式引用它
        response = self.client.get(reverse("polls:index"))
        self.assertIs(response.status_code,200)
        #response对象的类型为<class 'django.template.response.TemplateResponse'>
        #response.content 在数据库中没有内容的情况下返回 b'<!--\n    <p>No polls are available.</p>\n -->\n<!--\n\n    <p>No polls are available.</p>\n\n-->\n\n\n    <p>No polls are available.</p>\n\n'
        #要测试网页的内容是否包含什么，不能通过self.assertContains(response.content,'No polls are available.')
        #只能是self.assertContains(response,'No polls are available.')

        self.assertContains(response,'No polls are available.')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_with_past_question(self):
        """
        """
        create_question('Past question.',days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertIs(response.status_code,200)
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_with_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )
    
    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )


class QuestionDetailViewTests(TransactionTestCase):
    def test_with_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_with_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
