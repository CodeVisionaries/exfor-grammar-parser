import pytest
from typing import Optional, Union

from lark import Lark

from exfor_grammar_parser.ebnf_grammar import grammar
from exfor_grammar_parser.evaluation import eval_arith_expr

# @pytest.fixture
# def arith_parser():
#     return Lark(grammar, parser="lalr", start="arith_expr")

class TestArith:
    parser = Lark(grammar, parser="lalr", start="arith_expr")

    def parse_and_eval(self,expression: str, env: Optional[Union[None, dict]] = None) -> Union[int, float]:
        tree = self.parser.parse(expression)
        res = eval_arith_expr(tree, {} if env is None else env)
        return res

    def _parse_and_assert(self,expression: str, expected: Union[int, float]) -> None:
        res = self.parse_and_eval(expression)
        assert expected == res

    def test_integer_addition(self):
        self._parse_and_assert("3 + 5", 8)
        self._parse_and_assert("5 + 3", 8)
        self._parse_and_assert("9999999999999999 + 555555555555555", 10555555555555554)



