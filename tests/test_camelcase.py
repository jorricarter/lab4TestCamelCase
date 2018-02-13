import unittest
from CamelCase import camelcase


class TestCamelCase(unittest.TestCase):

    def test_camel_case_case(self):

        self.assertEqual('helloWorld', camelcase.camelcase("Hello World"))

        self.assertEqual('helloWorld', camelcase.camelcase("HeLlO WoRlD"))

        self.assertEqual('helloWorld', camelcase.camelcase("HELLO World"))

    def test_camel_case_spaces(self):

        self.assertEqual('helloWorld', camelcase.camelcase("HelloWorld"))

        self.assertEqual('helloWorldHowAreYou', camelcase.camelcase("Hello world how are you"))

        self.assertEqual('hellOWOrld', camelcase.camelcase("Hell o W orld"))
