import pytest
from stack.stack_using_list import Stack


def test_exists():
    assert Stack


def test_instantiation():
    assert Stack()


def test_isEmpty():
    mystack = Stack()
    assert mystack.isEmpty() == True


def test_push():
    mystack = Stack()
    mystack.push(1)
    mystack.push(2)
    assert mystack.data[1] == 2


@pytest.fixture
def filled_stack():
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    st.push(5)
    return st


@pytest.fixture
def empty_stack():
    return Stack()


def test_pop(filled_stack, empty_stack):
    m = filled_stack
    assert m.pop() == 5
    assert m.pop() == 4
    assert empty_stack.pop() == None


def test_peek(filled_stack, empty_stack):
    assert filled_stack.peek() == 5
    assert empty_stack.peek() == None


def test_size(filled_stack, empty_stack):
    assert filled_stack.size() == 5
    assert empty_stack.size() == 0
