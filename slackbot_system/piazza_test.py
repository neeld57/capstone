from piazza_function import get_post_attr, pretty_print
import unittest

class TestMethods(unittest.TestCase):
    def test_no_children_post(self):
        piazza_post = [{'history': [{'subject': 'Final Exam Grading',
                        'content':'Some example text to test with'}],
                        'children': [],
                        'created': '2020-11-15T20:20:20Z'}]
        all_post_attr = get_post_attr(piazza_post)
        my_text = ""
        for post in all_post_attr:
            my_text += pretty_print(post)
        self.assertEqual(my_text, "\n*Final Exam Grading | Written on 2020-11-15*```Some example text to test with```\n")

    def test_1_level_children_post(self):
        self.maxDiff = None
        piazza_post = [{'history': [{'subject': 'Final Exam Grading',
                                     'content': 'Some example text to test with'}],
                        'children': [
                            {
                                'history': [
                                    {'subject': 'Final Exam Grading',
                                     'content': 'Additional example text to test with'}
                                ],
                                'children': [],
                                'created': '2020-11-16T20:20:20Z',
                                'type': 's_answer'
                            }
                        ],
                        'created': '2020-11-15T20:20:20Z'}]
        all_post_attr = get_post_attr(piazza_post)
        my_text = ""
        for post in all_post_attr:
            my_text += pretty_print(post)
        self.assertEquals(my_text, "\n*Final Exam Grading | Written on 2020-11-15*```Some example text to test with```\n>```Additional example text to test with```\n\n")

    def test_2_level_children_post(self):
        self.maxDiff = None
        piazza_post = [{'history': [{'subject': 'Final Exam Grading',
                                     'content': 'Some example text to test with'}],
                        'children': [
                            {
                                'history': [
                                    {'subject': 'Final Exam Grading',
                                     'content': 'Additional example text to test with'}
                                ],
                                'children': [
                                    {
                                        'history': [
                                            {
                                                'subject': 'Final Exam Grading',
                                                'content': '2nd level example text'
                                            }
                                        ],
                                        'children': [],
                                        'created': '2020-11-16T23:22:45Z',
                                        'type': 's_answer'
                                    }
                                ],
                                'created': '2020-11-16T20:20:20Z',
                                'type': 's_answer'
                            }
                        ],
                        'created': '2020-11-15T20:20:20Z'}]
        all_post_attr = get_post_attr(piazza_post)
        my_text = ""
        for post in all_post_attr:
            my_text += pretty_print(post)
        self.assertEquals(my_text, "\n*Final Exam Grading | Written on 2020-11-15*"
                                   "```Some example text to test with```\n>```"
                                   "Additional example text to test with```\n\n"
                                   ">`2nd level example text`\n\n")


# For smoke testing

def test_no_children_post():
    piazza_post = [{'history': [{'subject': 'Final Exam Grading',
                    'content':'Some example text to test with'}],
                    'children': [],
                    'created': '2020-11-15T20:20:20Z'}]
    all_post_attr = get_post_attr(piazza_post)
    my_text = ""
    for post in all_post_attr:
        my_text += pretty_print(post)
    assert my_text == "\n*Final Exam Grading | Written on 2020-11-15*```Some example text to test with```\n"

def test_1_level_children_post():
    piazza_post = [{'history': [{'subject': 'Final Exam Grading',
                                 'content': 'Some example text to test with'}],
                    'children': [
                        {
                            'history': [
                                {'subject': 'Final Exam Grading',
                                 'content': 'Additional example text to test with'}
                            ],
                            'children': [],
                            'created': '2020-11-16T20:20:20Z',
                            'type': 's_answer'
                        }
                    ],
                    'created': '2020-11-15T20:20:20Z'}]
    all_post_attr = get_post_attr(piazza_post)
    my_text = ""
    for post in all_post_attr:
        my_text += pretty_print(post)
    assert my_text == "\n*Final Exam Grading | Written on 2020-11-15*```Some example text to test with```\n>```Additional example text to test with```\n\n"

def test_2_level_children_post():
    piazza_post = [{'history': [{'subject': 'Final Exam Grading',
                                 'content': 'Some example text to test with'}],
                    'children': [
                        {
                            'history': [
                                {'subject': 'Final Exam Grading',
                                 'content': 'Additional example text to test with'}
                            ],
                            'children': [
                                {
                                    'history': [
                                        {
                                            'subject': 'Final Exam Grading',
                                            'content': '2nd level example text'
                                        }
                                    ],
                                    'children': [],
                                    'created': '2020-11-16T23:22:45Z',
                                    'type': 's_answer'
                                }
                            ],
                            'created': '2020-11-16T20:20:20Z',
                            'type': 's_answer'
                        }
                    ],
                    'created': '2020-11-15T20:20:20Z'}]
    all_post_attr = get_post_attr(piazza_post)
    my_text = ""
    for post in all_post_attr:
        my_text += pretty_print(post)
    assert my_text == ("\n*Final Exam Grading | Written on 2020-11-15*"
                               "```Some example text to test with```\n>```"
                               "Additional example text to test with```\n\n"
                               ">`2nd level example text`\n\n")


if __name__ == '__main__':
    unittest.main()

