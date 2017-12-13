from querybuilder.fields import Field


class OperatorField(Field):
    OPERATOR = 'DEFINE_OPERATOR'

    def __init__(self, first_field, second_field, cast=None, alias=None):
        """

        :param first_field:
        :type first_field: Field
        :param second_field:
        :type second_field: Field
        """
        self.first_field = first_field
        self.second_field = second_field
        self._set_field_attrs(
            cast=cast,
            alias=alias,
        )

    def _set_field_attrs(self, cast=None, alias=None):
        self.name = self.first_field.name
        self.alias = alias
        self.table = self.first_field.table
        self.auto_alias = None
        self.ignore = False
        self.auto = False
        self.cast = cast

    def get_select_sql(self):
        first_sql = self.first_field.get_select_sql()
        second_sql = self.second_field.get_select_sql()

        return "({first}) {op} ({second})".format(
            first=first_sql,
            second=second_sql,
            op=self.OPERATOR
        )


class AddField(OperatorField):
    OPERATOR = '+'


class SubField(OperatorField):
    OPERATOR = '-'


class MulField(OperatorField):
    OPERATOR = '*'


class DivField(OperatorField):
    OPERATOR = '/'


class AndField(OperatorField):
    OPERATOR = 'AND'


class OrField(OperatorField):
    OPERATOR = 'OR'


class EqField(OperatorField):
    OPERATOR = '='


class NotEqField(OperatorField):
    OPERATOR = '!='


class LtField(OperatorField):
    OPERATOR = '<'


class GtField(OperatorField):
    OPERATOR = '>'


class LteField(OperatorField):
    OPERATOR = '<='


class GteField(OperatorField):
    OPERATOR = '>='
