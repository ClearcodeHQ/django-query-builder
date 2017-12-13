from querybuilder import field_operators
from querybuilder.fields import SimpleField
from querybuilder.query import Query

from querybuilder.tests.query_tests import QueryTestCase
from querybuilder.tests.models import Account


class OperatorFieldTest(QueryTestCase):

    def _assert_query(self, field, expected_query):
        query = Query().from_table(table=Account, fields=[field])
        self.assertEqual(query.get_sql(), expected_query)

    def test_cast_operator_field(self):
        field = field_operators.OperatorField(
            SimpleField('foo'),
            SimpleField('bar'),
            cast='INT',
        )
        expected_query = (
            'SELECT CAST((foo) DEFINE_OPERATOR (bar) AS INT) FROM tests_account'
        )
        self._assert_query(field, expected_query)

    def test_alias_operator_field(self):
        field = field_operators.OperatorField(
            SimpleField('foo'),
            SimpleField('bar'),
            alias='barfoo',
        )
        expected_query = (
            'SELECT (foo) DEFINE_OPERATOR (bar) AS "barfoo" FROM tests_account'
        )
        self._assert_query(field, expected_query)

    def test_alias_and_cast_operator_field(self):
        field = field_operators.OperatorField(
            SimpleField('foo'),
            SimpleField('bar'),
            alias='barfoo',
            cast='INT'
        )
        expected_query = (
            'SELECT CAST((foo) DEFINE_OPERATOR (bar) AS INT) AS "barfoo" '
            'FROM tests_account'
        )
        self._assert_query(field, expected_query)

    def test_add_operator_field(self):
        field = field_operators.AddField(
            SimpleField('first_name'),
            SimpleField('last_name'),
        )
        expected_query = 'SELECT (first_name) + (last_name) FROM tests_account'
        self._assert_query(field, expected_query)

    def test_sub_operator_field(self):
        field = field_operators.SubField(
            SimpleField('first_name'),
            SimpleField('last_name'),
        )
        expected_query = 'SELECT (first_name) - (last_name) FROM tests_account'
        self._assert_query(field, expected_query)

    def test_mul_operator_field(self):
        field = field_operators.MulField(
            SimpleField('first_name'),
            SimpleField('last_name'),
        )
        expected_query = 'SELECT (first_name) * (last_name) FROM tests_account'
        self._assert_query(field, expected_query)

    def test_div_operator_field(self):
        field = field_operators.DivField(
            SimpleField('first_name'),
            SimpleField('last_name'),
        )
        expected_query = 'SELECT (first_name) / (last_name) FROM tests_account'
        self._assert_query(field, expected_query)

    def test_and_operator_field(self):
        field = field_operators.AndField(
            SimpleField('first_name'),
            SimpleField('last_name'),
        )
        expected_query = (
            'SELECT (first_name) AND (last_name) FROM tests_account'
        )
        self._assert_query(field, expected_query)

    def test_or_operator_field(self):
        field = field_operators.OrField(
            SimpleField('first_name'),
            SimpleField('last_name'),
        )
        expected_query = 'SELECT (first_name) OR (last_name) FROM tests_account'
        self._assert_query(field, expected_query)

    def test_eq_operator_field(self):
        field = field_operators.EqField(
            SimpleField('first_name'),
            SimpleField('last_name'),
        )
        expected_query = 'SELECT (first_name) = (last_name) FROM tests_account'
        self._assert_query(field, expected_query)

    def test_not_eq_operator_field(self):
        field = field_operators.NotEqField(
            SimpleField('first_name'),
            SimpleField('last_name'),
        )
        expected_query = 'SELECT (first_name) != (last_name) FROM tests_account'
        self._assert_query(field, expected_query)

    def test_less_than_operator_field(self):
        field = field_operators.LtField(
            SimpleField('first_name'),
            SimpleField('last_name'),
        )
        expected_query = 'SELECT (first_name) < (last_name) FROM tests_account'
        self._assert_query(field, expected_query)

    def test_greater_than_operator_field(self):
        field = field_operators.GtField(
            SimpleField('first_name'),
            SimpleField('last_name'),
        )
        expected_query = 'SELECT (first_name) > (last_name) FROM tests_account'
        self._assert_query(field, expected_query)

    def test_less_equal_operator_field(self):
        field = field_operators.LteField(
            SimpleField('first_name'),
            SimpleField('last_name'),
        )
        expected_query = 'SELECT (first_name) <= (last_name) FROM tests_account'
        self._assert_query(field, expected_query)

    def test_greater_equal_operator_field(self):
        field = field_operators.GteField(
            SimpleField('first_name'),
            SimpleField('last_name'),
        )
        expected_query = 'SELECT (first_name) >= (last_name) FROM tests_account'
        self._assert_query(field, expected_query)


class FieldMethodOperatorTestCase(QueryTestCase):

    def setUp(self):
        super(FieldMethodOperatorTestCase, self).setUp()
        self.field_a = SimpleField('foo')
        self.field_b = SimpleField('bar')

    def _assert_fields(self, field, cls):
        """
        Assert field if operator field has
        :type field:
        :type cls: type(cls)
        """
        self.assertIs(type(field), cls)
        self.assertIs(field.first_field, self.field_a)
        self.assertIs(field.second_field, self.field_b)

    def test_add_operator(self):
        self._assert_fields(
            field=self.field_a + self.field_b,
            cls=field_operators.AddField,
        )

    def test_sub_operator(self):
        self._assert_fields(
            field=self.field_a - self.field_b,
            cls=field_operators.SubField,
        )

    def test_mul_operator(self):
        self._assert_fields(
            field=self.field_a * self.field_b,
            cls=field_operators.MulField,
        )

    def test_div_operator(self):
        self._assert_fields(
            field=self.field_a / self.field_b,
            cls=field_operators.DivField,
        )

    def test_floordiv_operator(self):
        self._assert_fields(
            field=self.field_a // self.field_b,
            cls=field_operators.DivField,
        )

    def test_eq_operator(self):
        self._assert_fields(
            field=self.field_a == self.field_b,
            cls=field_operators.EqField,
        )

    def test_not_eq_operator(self):
        self._assert_fields(
            field=self.field_a != self.field_b,
            cls=field_operators.NotEqField,
        )

    def test_less_than_operator(self):
        self._assert_fields(
            field=self.field_a < self.field_b,
            cls=field_operators.LtField,
        )

    def test_greater_than_operator(self):
        self._assert_fields(
            field=self.field_a > self.field_b,
            cls=field_operators.GtField,
        )

    def test_less_than_and_equal_operator(self):
        self._assert_fields(
            field=self.field_a <= self.field_b,
            cls=field_operators.LteField,
        )

    def test_greater_than_and_equal_operator(self):
        self._assert_fields(
            field=self.field_a >= self.field_b,
            cls=field_operators.GteField,
        )
